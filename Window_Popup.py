from tkinter import *
from tkinter import ttk
import pandas as pd

from Manage import Manage

USERS_FILE = 'users.csv'
BOOKS_FILE = 'books.csv'
BORROW_FILE = 'borrow.csv'

#========================================================================================
#사용자 명단 띄우기
#========================================================================================
class UserList:
    def __init__(self):
        #Manage 호출, 초기화
        self.manage = Manage()
        self.users = self.manage.users

        self.main = Tk()
        self.main.title('사용자 명단')
        self.main.geometry('540x400')
        self.main.configure(bg='grey')
        
        self.create_widgets()

        self.main.mainloop()

    def create_widgets(self):
        #버튼이 들어갈 레이블프레임
        lableframe = LabelFrame(self.main, padx=5, pady=5)
        lableframe.pack(side='bottom')

        #[ 선택 ] [ 닫기 ] 버튼
        btn1 = Button(lableframe, text='선택')
        btn1.pack(side='left')
        btn2 = Button(lableframe, text='닫기', command=self.exit_window)
        btn2.pack(side='right')

        #사용자 명단에 Treeview 넣기
        tree = ttk.Treeview(self.main)
        data = pd.DataFrame(self.users)

        #열 이름 설정
        tree['columns'] = data.columns.tolist()
        tree["show"] = "headings"

        # 각 열에 대해 헤더 설정
        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        # Treeview 위젯 배치
        tree.pack(expand=True, fill='both')

        # Treeview에 스크롤바 넣기
        scroll1 = Scrollbar(tree)
        scroll1.pack(side='right', fill='y')
        scroll2 = Scrollbar(tree)
        scroll2.pack(side='bottom', fill='x')

    

        


    # [ 선택 ] 버튼 기능




    # [ 닫기 ] 버튼 기능
    def exit_window(self):
        self.main.quit()
        self.main.destroy()

#========================================================================================
# 도서 추가 페이지 띄우기
#========================================================================================
class AddBook:
    def __init__(self):
        #Manage 호출, 초기화
        self.manage = Manage()
        self.users = self.manage.users
        self.books = self.manage.books

        self.main = Tk()
        self.main.title('도서 추가')
        self.main.geometry('540x400')
        self.main.configure(bg='grey')

        self.create_widgets()

        self.main.mainloop()

    def create_widgets(self):
        label1 = Label(self.main, text='제목')
        label1.grid(row=0, column=0)
        label2 = Label(self.main, text='ISBN')
        label2.grid(row=1, column=0)
        label3 = Label(self.main, text='저자')
        label3.grid(row=2, column=0)
        label4 = Label(self.main, text='출판사')
        label4.grid(row=3, column=0)
        label5 = Label(self.main, text='추가할 권 수')
        label5.grid(row=4, column=0)

        entry1 = Entry(self.main)
        entry1.grid(row=0, column=1)
        entry2 = Entry(self.main)
        entry2.grid(row=1, column=1)
        entry3 = Entry(self.main)
        entry3.grid(row=2, column=1)
        entry4 = Entry(self.main)
        entry4.grid(row=3, column=1)
        entry5 = Entry(self.main)
        entry5.grid(row=4, column=1)
        
        btn1 = Button(self.main, text='추가', 
                      command=self.add_(entry1, entry2, entry3, entry4, entry5))
        btn1.grid(row=5, column=0)
        btn2 = Button(self.main, text='닫기', command=self.exit_window)
        btn2.grid(row=5, column=1)
        

    #[ 추가 ] 버튼 기능
    def add_(self, entry1, entry2, entry3, entry4, entry5):
        try:
            isbn = entry2.get()
            title = entry1.get()
            author = entry3.get()
            publisher = entry4.get()
            quantity = int(entry5.get())
        except Exception as e:
            return e
        print(isbn, title, author, publisher, quantity)

        if (isbn == None) or (title == None) or (author == None) or \
             (publisher == None) or (quantity == None):
            print('빈 칸을 채워주세요')
        else:
            Manage.add_book(isbn, title, author, publisher, quantity)

    #[ 닫기 ] 버튼 기능
    def exit_window(self):
        self.main.quit()
        self.main.destroy()


        




        



        
        
        




