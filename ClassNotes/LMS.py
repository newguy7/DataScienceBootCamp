'''
Create a simple library management system with the following features:
Each book in the library should have attributes for title, author, genre, and availability status.
Implement methods to borrow and return books.
Implement a method to display the list of available books.
Implement a method to search for books by title or author.
Implement a method to add new books to the library.
 
'''
class Book():

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True

    def borrow_book(self):                
        if self.is_available == True:
            self.is_available = False
        else:
            print("The book is not currently available.")
    

    def return_book(self):
        if self.is_available == False:       
            self.is_available = True
        else:
            print("No book to return.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Availability: {'Available' if self.is_available else 'Not Available'}")


class Library():
    
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def display_available_books(self):
        books_available = [book for book in self.books if book.is_available]
        if books_available:
            print("Available books:")
            for book in books_available:
                book.display_info()
                print("-----------------------")
    
    def search_by_title_or_author(self, search_word):
        books_found = [book for book in self.books if search_word.lower() in book.title.lower() or search_word.lower() in book.author.lower()]
        print("Searching for the book.....")
        if books_found:
            print("Search Result.")
            for book in books_found:
                book.display_info()
                print("-----------------------")
        else:
            print("No books found matching the search criteria.")
    

library = Library()

book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")

# Add the book objects to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# check status of the book 
library.display_available_books()

# borrow the book
book1.borrow_book()

# check status of the book after borrowing
print(book1.is_available)

# try to borrow the same book
book1.borrow_book()

# Display the list of available books
library.display_available_books()

# Return the book
book1.return_book()

library.search_by_title_or_author("The Great Gatsby")

'''
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True
 
    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} by {self.author} has been borrowed.")
        else:
            print(f"{self.title} is not available for borrowing.")
 
    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")
 
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Availability: {'Available' if self.available else 'Not Available'}")
 
 
class Library:
    def __init__(self):
        self.books = []
 
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")
 
    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                book.display_info()
                print("--------------------")
        else:
            print("No books available in the library.")
 
    def search_books(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            print("Search Results:")
            for book in found_books:
                book.display_info()
                print("--------------------")
        else:
            print("No books found matching the search criteria.")
 
 
# Example usage:
library = Library()
 
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic")
 
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
 
library.display_available_books()
 
book1.borrow()
book2.borrow()
book3.borrow()
 
library.display_available_books()
 
library.search_books("Harry Potter")


'''
