class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title = None, author = None):
        # add a book to the library
        # read the title and author form terminal
        if title is None:
            title = input("Enter book title: ")
        if author is None:
            author = input("Enter book author: ")
        self.books.append({"title": title, "author": author})

    def remove_book(self, title = None):
        # remove a book from the library
        if title is None:
            title = input("Enter book title to remove: ")
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"The book '{title}' has been removed.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title = None):
        if title is None:
            title = input("Enter book title to search: ")
            # show the name of book and author if is available if not write not found
            for book in self.books:
                if book["title"] == title:
                    print(f"Found: {book['title']} by {book['author']}")
                    return book
            print("Not Found")

    def show_books(self):
        # show the books in the library
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}")
        print("Total books:", len(self.books))
        return self.books
