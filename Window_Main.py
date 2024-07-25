from tkinter import *

from Window_Contents import Window_User
from Window_Contents import Window_Borrow
from Window_Contents import Window_Book
from Window_Contents import Window_Category
from Window_Contents import Window_Publisher


#이쯤에서 데이터 불러오기?


#===========================================================================
#메인 윈도우
#===========================================================================
class Window_Main():
    #생성자
    def __init__(self) :
        self.main = Tk()
        self.main.title('도서관 출납 관리자')
        self.main.geometry('560x560') #540x540
        self.main.configure(bg='lightgrey')

        #컨텐츠 프레임 생성
        self.frame_user = Frame(self.main)
        self.frame_borrow = Frame(self.main)
        self.frame_book = Frame(self.main)
        self.frame_category = Frame(self.main)
        self.frame_publisher = Frame(self.main)


        #버튼 프레임 생성
        self.frame_icons = Frame(self.main, bg='lightgrey')        
        self.frame_icons.pack(side='left')
        #카운트 변수로 위젯생성제어
        self.btns_count = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
        self.buttons()

        self.main.mainloop()

    #버튼 위젯 생성
    def buttons(self):
        self.icons = [
            PhotoImage(file='./icon/icon_user.png'),
            PhotoImage(file='./icon/icon_borrow.png'),
            PhotoImage(file='./icon/icon_book.png'),
            PhotoImage(file='./icon/icon_category.png'),
            PhotoImage(file='./icon/icon_publisher.png')
        ]
        icons = self.icons

        button0 = Button(self.frame_icons, image=icons[0], command=self.show_page_user)
        button0.image = icons[0] # 참조를 유지하기 위해 필요함
        button0.grid(row=0, column=0, padx=2, pady=2)
        button1 = Button(self.frame_icons, image=icons[1], command=self.show_page_borrow)
        button1.image = icons[1]
        button1.grid(row=1, column=0, padx=2, pady=2)
        button2 = Button(self.frame_icons, image=icons[2], command=self.show_page_book)
        button2.image = icons[2]
        button2.grid(row=2, column=0, padx=2, pady=2)
        button3 = Button(self.frame_icons, image=icons[3])
        button3.image = icons[3]
        button3.grid(row=3, column=0, padx=2, pady=2)
        button4 = Button(self.frame_icons, image=icons[4])
        button4.image = icons[4]
        button4.grid(row=4, column=0, padx=2, pady=2)

    #페이지 전환 메서드
    def show_page_user(self):
        print('사용자 정보창')
        self.frame_borrow.pack_forget()
        self.frame_book.pack_forget()
        self.frame_category.pack_forget()
        self.frame_publisher.pack_forget()
        self.frame_user.pack(fill='both', expand=True)

        if self.btns_count['a'] == None:#카운트 및 위젯 생성
            Window_User(self.frame_user)
            self.btns_count['a'] = True

    def show_page_borrow(self):
        print('대여/반납 정보창')
        self.frame_user.pack_forget()
        self.frame_book.pack_forget()
        self.frame_category.pack_forget()
        self.frame_publisher.pack_forget()
        self.frame_borrow.pack(fill='both', expand=True)

        if self.btns_count['b'] == None:#카운트 및 위젯 생성
            Window_Borrow(self.frame_borrow)
            self.btns_count['b'] = True
        
    def show_page_book(self):
        print('도서 정보창')
        self.frame_user.pack_forget()
        self.frame_borrow.pack_forget()
        self.frame_category.pack_forget()
        self.frame_publisher.pack_forget()
        self.frame_book.pack(fill='both', expand=True)

        if self.btns_count['c'] == None:#카운트 및 위젯 생성
            Window_Book(self.frame_book)
            self.btns_count['c'] = True

    def show_page_category(self):
        self.frame_user.pack_forget()
        self.frame_borrow.pack_forget()
        self.frame_book.pack_forget()
        self.frame_publisher.pack_forget()
        self.frame_category.pack(fill='both', expand=True)

        if self.btns_count['d'] == None:#카운트 및 위젯 생성
            Window_Category(self.frame_category)
            self.btns_count['d'] = True

    def show_page_publisher(self):
        self.frame_user.pack_forget()
        self.frame_borrow.pack_forget()
        self.frame_book.pack_forget()
        self.frame_category.pack_forget()
        self.frame_publisher.pack(fill='both', expand=True)

        if self.btns_count['e'] == None:#카운트 및 위젯 생성
            Window_Publisher(self.frame_publisher)
            self.btns_count['e'] = True

    

