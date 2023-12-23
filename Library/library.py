# Library Class
class Library:
    def __init__(self):
        self.__available_books = []
        self.__records = []

    def add_book(self, book):
        self.__available_books.append(book)

    def remove_book(self, book):
        self.__available_books.remove(book)

    def add_record(self, record):
        self.__records.append(record)

    def status(self, book):
        if book in self.__available_books:
            print(f"{book} is available.")
        else:
            for record in self.__records:
                if record.is_active() and record.book is book:
                    print(record)

    def search_books(self, genre=None, subject=None):
        for book in self.__available_books:
            if genre is None and subject is None:
                print(book)
            elif subject and isinstance(book, TextBook) and book.subject == subject:
                print(book)
            elif genre and isinstance(book, StoryBook) and book.genre == genre:
                print(book)

# BorrowRecord Class
class BorrowRecord:
    def __init__(self, borrower, book, date_borrowed):
        self.__borrower = borrower
        self.__book = book
        self.__date_borrowed = date_borrowed
        self.__date_returned = None

    @property
    def book(self):
        return self.__book

    @property
    def borrower(self):
        return self.__borrower

    @property
    def date_borrowed(self):
        return self.__date_borrowed

    @property
    def date_returned(self):
        return self.__date_returned

    def is_active(self):
        return self.__date_returned is not None

    def close(self, date_returned):
        if date_returned is None:
            self.__date_returned = date_returned

    def __repr__(self):
        if self.date_returned is not None:
            return f"{self.book} borrowed by {self.borrower} on {self.date_borrowed} and returned on {self.date_returned}"
        else:
            return f"{self.book} borrowed by {self.borrower} on {self.date_borrowed}"

# Book Classes
class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __repr__(self):
        return f"{self.name} by {self.author.name}"

class TextBook(Book):
    def __init__(self, name, author, subject):
        super().__init__(name, author)
        self.__subject = subject

    @property
    def subject(self):
        return self.__subject

class StoryBook(Book):
    def __init__(self, name, author, genre):
        super().__init__(name, author)
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre

# Person Classes
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return f"{self.name}, {self.age} years old"

class Author(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__books = []

    @property
    def books(self):
        return self.__books

class Borrower(Person):
    def __init__(self, name, age, library):
        super().__init__(name, age)
        self.__records = []
        self.__library = library

    @property
    def records(self):
        return self.__records

    def return_book(self, book, date_returned):
        for record in self.records:
            if record.is_active() and record.book is book:
                record.close(date_returned)
                break
        self.__library.add_book(book)

    def borrow_book(self, book, date_borrowed):
        record = BorrowRecord(self, book, date_borrowed)
        self.__records.append(record)
        self.__library.add_record(record)






