# 11. Class Methods
# Assignment:Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the 
# count when a new book is added.

class Book:
    total_book = 0

    def __init__(self):
        Book.total_book += 1 

    @classmethod
    def  increment_book_count(cls):
        print(f"Total books Counts is {cls.total_book}")

book1 = Book()
book2 = Book()
book3 = Book()
book4 = Book()

Book.increment_book_count()
