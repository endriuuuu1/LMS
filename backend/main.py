import sqlite3
import random
import uuid


class Book:
    def __init__(self, title: str, author: str, isbn=None) -> None:
        self.author = author
        self.title = title
        self.isbn = isbn
        #self.quantity = quantity

    def display_book_info(self) -> str:
        return f'Title: {self.title}, Author: {self.author}'

    # def check_availability(self) -> bool:
    #     return self.quantity > 0

    # def update_quantity(self, quantity: int) -> None:
    #     self.quantity += quantity

class User:
    def __init__(self, username: str, email: str, uid = None) -> None:
        self.username = username
        self.email = email
        self.user_id = uid
        self.borrowed_books = []

    # a user can borrow a book
    def borrow(self, book: Book):
        # if book.check_availability():
        #     book.update_quantity(-1)
        self.borrowed_books.append(book)

    # a user can return the borrowed book
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)

    # a user can view the list of books it has borrowed
    def view_borrowed_books(self):
        return self.borrowed_books

class Library:
    _library_name = 'Tbilisi GOAT Library'
    _library_books = {} # all books available in library
    _library_users = {} # registered users

    def add_book(self, book_object: Book):
        # check if a book is already in the system
        # if not generate a new isbn13 for the book and add it
        if self.is_book_added(book_object):
            print('Book already in the library')
        else:
            new_isbn = self.generate_isbn13()
            book_object.isbn = new_isbn
            self._library_books[new_isbn] = book_object
            #print('Book added')

    def is_book_added(self, book_object: Book) -> bool:
        for existing_book in self._library_books.values():
            if (existing_book.title.lower() == book_object.title.lower() and
                    existing_book.author.lower() == book_object.author.lower()):
                return True
        return False

    def register_user(self, user_object: User) -> None:
        # check if user is already registered
        # if not generate a new id for the user and register it
        if self.is_user_registered(user_object):
            print('User already registered')
            #raise Exception('User already registered')
        else:
            generated_id = self.generate_user_id()
            user_object.user_id = generated_id # pass the id identifier to the user instance
            self._library_users[generated_id] = user_object
            #print('User registered')


    def is_user_registered(self, user_object) -> bool:
        email = user_object.email
        for value in self._library_users.values():
            if email == value.email:
                return True
        return False

    # def search_book(self, title):
    #     return self._library_books.get(title, None)

    # Display Methods
    def display_library_info(self):
        return self._library_name

    def list_library_books(self):
        books = {}
        for key, value in self._library_books.items():
            books[key] = f"{value.title.title()} by {value.author.title()}"
        return books

    def list_library_users(self):
        #return self._library_users
        users = {}
        for key, value in self._library_users.items():
            users[key] = value.username
        return users

    # Generation Methods:
    @staticmethod
    def generate_user_id() -> str:
        return uuid.uuid4().hex # need it to have a regular string value rather than uuid object for JSON

    @staticmethod
    def generate_isbn13():
        prefixes: list[str] = ['978', '979']
        prefix: str = random.choice(prefixes)

        numbers: list[str] = []
        for _ in range(9):
            num = random.randint(0,9)
            numbers.append(str(num))
        body = ''.join(numbers)
        split_body = '-'.join([body[i:i+3] for i in range(0, len(body), 3)])
        isbn12: str = f'{prefix}-{split_body}'

        checksum = 0
        for i, digit in enumerate(isbn12):
            if digit.isalnum():
                if i % 2 == 0:
                    checksum += int(digit)
                else:
                    checksum += int(digit) * 3
            else:
                continue

        check_digit = (10 - (checksum % 10)) % 10
        isbn13 = f'{isbn12}-{check_digit}'
        return isbn13

def main():
    library = Library()
    book1 = Book('harry potter', 'J.K rowling')
    book2 = Book('cookbook','Gordon Ramsey')
    demo_book = Book('harry potter', 'j.k RoWling')
    demo_book2 = Book('something','bunkeri tukeri')
    user1 = User('andria', 'andria@gmail.com')
    user2 = User('john', 'doe@gmail.com')
    test_user = User('andria', 'andria@gmail.com')
    library.register_user(user1)
    library.register_user(user2)
    library.register_user(test_user)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book1)
    library.add_book(demo_book)
    library.add_book(demo_book2)
    print(library.display_library_info())
    print(library.list_library_books())
    print(library.list_library_users())


if __name__ == '__main__':
    main()

