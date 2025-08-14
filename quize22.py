import library


def main():
    #lib = library.Library()
    #lib.add_book("1984", "George Orwell")
    #lib.add_book("To Kill a Mockingbird", "Harper Lee")
    #print(lib.show_books())
    #lib.remove_book("1984")
    #print(lib.show_books())
    #print(lib.search_book("To Kill a Mockingbird"))

    lib = library.Library()
    lib.add_book()
    lib.show_books()
    lib.search_book()
    lib.remove_book()
    lib.show_books()
    

if __name__ == "__main__":
    main()
