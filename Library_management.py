class Book:
    def __init__(self, title, author, isbn, shelf):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.shelf = shelf

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Shelf: {self.shelf}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book removed: {book}")
                return
        print("Book not found.")

    def search_book(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Books found:")
            for book in found_books:
                print(book)
        else:
            print("No books found with that title.")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")


