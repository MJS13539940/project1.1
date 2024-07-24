from tkinter import *

from Window_Popup import UserList
from Window_Popup import AddBook
from Manage import Manage

###### 첫번째 버튼을 누르면 열리는 페이지
class Window_User:
    def __init__(self, frame_user):
        self.manage = Manage()
        self.frame_user = frame_user
        self.create_widgets()

        #사용자 정보
    def create_widgets(self):    
        info_box = LabelFrame(self.frame_user, text='사용자 정보', relief="groove")
        info_box.pack(padx=5, pady=5, side='top', fill='both')

        # [ 사용자 명단 ] 버튼
        btn_user_list = Button(info_box, text='사용자 등록', padx=5, pady=5, 
                           command=None)
        btn_user_list.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        # [ 새로 고침 ] 버튼
        btn_clear = Button(info_box, text='새로고침', padx=5, pady=5, width=10, 
                           command=self.clear)
        btn_clear.grid(row=8, column=0, padx=5, pady=5)
        # [ 검색 ] 버튼
        btn_search = Button(info_box, text='사용자 명단', padx=5, pady=5, width=10, 
                            command=UserList)
        btn_search.grid(row=8, column=1, padx=5, pady=5)

        #레이블
        label_user_num = Label(info_box, text="회원번호", anchor='e', justify='right')
        label_user_num.grid(row=2, column=0, padx=5, pady=5)
        value_user_num = Entry(info_box)
        value_user_num.grid(row=2, column=1, padx=5, pady=5)

        label_user_name = Label(info_box, text="이름", anchor='e', justify='right')
        label_user_name.grid(row=3, column=0, padx=5, pady=5)
        value_user_name = Entry(info_box)
        value_user_name.grid(row=3, column=1, padx=5, pady=5)

        label_user_birth = Label(info_box, text="생년월일", anchor='e', justify='right')
        label_user_birth.grid(row=4, column=0, padx=5, pady=5)
        value_user_birth = Entry(info_box)
        value_user_birth.grid(row=4, column=1, padx=5, pady=5)

        label_user_phone = Label(info_box, text="연락처", anchor='e', justify='right')
        label_user_phone.grid(row=5, column=0, padx=5, pady=5)
        value_user_phone = Entry(info_box)
        value_user_phone.grid(row=5, column=1, padx=5, pady=5)

        label_user_etc = Label(info_box, text="비고", anchor='e', justify='right')
        label_user_etc.grid(row=6, column=0, padx=5, pady=5)
        value_user_etc = Entry(info_box)
        value_user_etc.grid(row=6, column=1, padx=5, pady=5)

        self.entries = [value_user_num, value_user_name, value_user_birth, value_user_phone, value_user_etc]
    

    #[ 사용자 등록 ] 기능
    def add_user(self)

    #[ 새로고침 ] 기능
    def clear(self):
        for i in self.entries:
             i.delete(0, 'end')

    #검색 기능
    def search(self):
        pass
         

###### 두번째 버튼을 누르면 열리는 페이지
class Window_Borrow:
    def __init__(self):
        label = Label(frame_borrow, text="대여/반납 정보창")
        label.pack()



###### 세번째 버튼을 누르면 열리는 페이지
class Window_Book:
    def __init__(self, frame_book):
        #Manage 호출
        self.manage = Manage()
        #초기화
        self.frame_book = frame_book
        self.create_widgets()

    def create_widgets(self):
        # [ 도서 추가 ] 버튼
        btn_add_book = Button(self.frame_book, text='도서 추가', 
                              command=AddBook)
        btn_add_book.pack()
        
