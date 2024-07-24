import pandas as pd
from datetime import datetime

USERS_FILE = 'users.csv'
BOOKS_FILE = 'books.csv'
BORROW_FILE = 'borrow.csv'

class Manage:
    def __init__(self):
        #사용자
        self.users = self.load_file(USERS_FILE, ['user_num', 'user_name', 'user_birth', 'user_phone', 'user_etc'])
        self.users = self.users.fillna(0)
        #도서
        self.books = self.load_file(BOOKS_FILE, ['isbn', 'title', 'author', 'publisher', 'total_quantity', 'available_quantity'])
        self.books = self.books.fillna(0)
        #대여/반납
        self.borrow = self.load_file(BORROW_FILE, ['user_num', 'user_name', 'borrow_isbn', 'borrow_date', 'return_date', 'returned_date', 'deadline'])
        self.borrow = self.borrow.fillna(0)

    #파일 불러오기(없으면 만들기)
    @staticmethod
    def load_file(file_path, file_columns):
        try:
            print('[ %s ] 파일을 불러옵니다.' % file_path)
            return pd.read_csv(file_path)
        
        except FileNotFoundError:
            print('... 파일이 없습니다. [ %s ] 파일을 생성합니다.' % file_path)
            df = pd.DataFrame(columns=file_columns)
            df.to_csv(file_path, index=False)
            return df

    #데이터 저장하기    
    def save_data(self):
        try:
            self.users.to_csv(USERS_FILE, index=False)
            self.books.to_csv(BOOKS_FILE, index=False)
            self.borrow.to_csv(BORROW_FILE, index=False)
            print('파일이 저장되었습니다.')
        except:
            print('파일을 저장하는 데 실패했습니다.')
            return Exception
        
    #사용자 등록하기
    def add_user(self, user_name, user_birth, user_phone, user_etc):
        #등록된 사용자인지 판별
        if (user_name in self.users['user_name'].values) and (user_birth in self.users['user_birth'].values):
            print('이미 등록된 사용자입니다.')
            
        else:
            #회원번호 생성
            user_id = len(self.users) + 1

            #새 사용자 정보
            new_user = pd.DataFrame({
                'user_num': user_id, 'user_name': user_name, 'user_birth': user_birth, 
                'user_phone': user_phone, 'user_etc': user_etc
            })
            #데이터 삽입 및 저장
            self.users = pd.concat([self.users, new_user], ignore_index=True)
            self.save_data()
            print('사용자 정보가 추가되었습니다.')

    #책 등록하기
    def add_book(self, isbn, title, author, publisher, quantity):
        #새 책 정보
        new_book = pd.DataFrame({
            'isbn': isbn, 'title': title, 'author': author, 'publisher': publisher
        })
        #책이 이미 있는 책이면 수량 증가
        if isbn in self.books['isbn'].values:
            total = self.books.iloc[isbn, [4]].values
            available = self.books.iloc[isbn, [5]].values

            total = total + quantity
            available = available + quantity
            self.save_data()
            print('도서가 %s권 추가되었습니다.' % quantity)

        #새로운 책이면 추가
        else:
            self.books = pd.concat([self.books, new_book], ignore_index=True)
            self.save_data()
            print('새 도서가 추가되었습니다.')

    #대여 처리
    




        







