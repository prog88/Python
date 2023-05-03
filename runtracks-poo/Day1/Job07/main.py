class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__number_of_pages = 0

    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_number_of_pages(self):
        return self.__number_of_pages
    
    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, new_author):
        self.__author = new_author
    
    def set_number_of_pages(self, new_number_of_pages):
        if new_number_of_pages >= 0 and isinstance(new_number_of_pages, int):
            self.__number_of_pages = new_number_of_pages
        else:
            print("Number of pages should be a positive Integer.")

    def descriptions(self):
        print(f"Title:{self.__title}; Author: {self.__author}; number of pages: {self.__number_of_pages}.")

book = Book()
book.set_title("Pyhton is Ez")
book.set_author("Prog88")
book.set_number_of_pages(123)
book.descriptions()

book.set_number_of_pages(-1)
book.set_number_of_pages(2.5)
