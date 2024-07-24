from tkinter import *

#===========================================================================
#메인 윈도우
#===========================================================================
class App(Tk):
    def __init__(self):
        super().__init__()
  
        self.title('도서관 출납 관리자')
        self.geometry('980x560') #960x540
        self.configure(bg='grey')
        self.main_canvas = Canvas(self, bg='lightgrey')
        self.main_canvas.pack(fill='both', expand=True)

        self.icons = [
            PhotoImage(file='./icon/icon_user.png'),
            PhotoImage(file='./icon/icon_borrow.png'),
            PhotoImage(file='./icon/icon_book.png'),
            PhotoImage(file='./icon/icon_category.png'),
            PhotoImage(file='./icon/icon_publisher.png')
        ]

        #컨텐츠 프레임 생성
        self.frame_user = Frame(self.main_canvas)
        self.frame_borrow = Frame(self.main_canvas)
        self.frame_book = Frame(self.main_canvas)
        self.frame_category = Frame(self.main_canvas)
        self.frame_publisher = Frame(self.main_canvas)

        #아이콘 프레임 생성
        self.frame_icons = Frame(self.main_canvas, bg='purple')        
        self.frame_icons.grid(row=0, column=0)

        #카운트 변수로 위젯생성제어
        self.btns_count = {'a': None, 'b': None, 'c': None, 'd': None, 'e': None}
        self.buttons()

    #버튼 생성
    def buttons(self):
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
        button3 = Button(self.frame_icons, image=icons[3], command=self.show_page_category)
        button3.image = icons[3]
        button3.grid(row=3, column=0, padx=2, pady=2)
        button4 = Button(self.frame_icons, image=icons[4], command=self.show_page_publisher)
        button4.image = icons[4]
        button4.grid(row=4, column=0, padx=2, pady=2)


    #페이지 전환
    def show_page_user(self):
        self.frame_borrow.grid_forget()
        self.frame_book.grid_forget()
        self.frame_category.grid_forget()
        self.frame_publisher.grid_forget()

        self.frame_user.grid(row=0, column=1)
        self.page_user()

    def show_page_borrow(self):
        self.frame_user.grid_forget()
        self.frame_book.grid_forget()
        self.frame_category.grid_forget()
        self.frame_publisher.grid_forget()

        self.frame_borrow.grid(row=0, column=1)
        self.page_borrow()

    def show_page_book(self):
        self.frame_user.grid_forget()
        self.frame_borrow.grid_forget()
        self.frame_category.grid_forget()
        self.frame_publisher.grid_forget()

        self.frame_book.grid(row=0, column=1)
        self.page_book()

    def show_page_category(self):
        self.frame_user.grid_forget()
        self.frame_borrow.grid_forget()
        self.frame_book.grid_forget()
        self.frame_publisher.grid_forget()

        self.frame_category.grid(row=0, column=1)
        self.page_category()

    def show_page_publisher(self):
        self.frame_user.grid_forget()
        self.frame_borrow.grid_forget()
        self.frame_book.grid_forget()
        self.frame_category.grid_forget()

        self.frame_publisher.grid(row=0, column=1)
        self.page_publisher()

        #페이지 구성요소 생성
    def page_user(self):
        if self.btns_count['a'] == None:
            label_user_num = Label(self.frame_user, text="회원번호", anchor='e')
            label_user_num.pack()
            value_user_num = Entry(self.frame_user)
            value_user_num.pack()

            label_user_name = Label(self.frame_user, text="이름", anchor='e')
            label_user_name.pack()
            value_user_name = Entry(self.frame_user)
            value_user_name.pack()

            label_user_birth = Label(self.frame_user, text="생년월일", anchor='e')
            label_user_birth.pack()
            value_user_birth = Entry(self.frame_user)
            value_user_birth.pack()

            label_user_phone = Label(self.frame_user, text="연락처", anchor='e')
            label_user_phone.pack()
            value_user_phone = Entry(self.frame_user)
            value_user_phone.pack()

            label_user_etc = Label(self.frame_user, text="비고", anchor='e')
            label_user_etc.pack()
            value_user_etc = Entry(self.frame_user)
            value_user_etc.pack()
            
            #생성 카운트
            self.btns_count['a'] = self.frame_user
            
    def page_borrow(self):
        if self.btns_count['b'] == None:
            label = Label(self.frame_borrow, text="This is Page 2")
            label.pack()

            self.btns_count['b'] = self.frame_borrow

    def page_book(self):
        if self.btns_count['c'] == None: 
            label = Label(self.frame_book, text="This is Page 3")
            label.pack()

            self.btns_count['c'] = self.frame_book

    def page_category(self):
        if self.btns_count['d'] == None:
            label = Label(self.frame_category, text="This is Page 4")
            label.pack()

            self.btns_count['d'] = self.frame_category

    def page_publisher(self):
        if self.btns_count['e'] == None:
            label = Label(self.frame_publisher, text="This is Page 5")
            label.pack()

            self.btns_count['e'] = self.frame_publisher


if __name__ == "__main__":
    app = App()
    app.mainloop()