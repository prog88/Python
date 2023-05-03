class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""
        self.__number_of_pages = 0
        self.__is_available = True

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
        print(f"Title:{self.__title}; Author: {self.__author}; number of pages: {self.__number_of_pages}; is available: {self.__is_available}")

    def is_available(self):
        return self.__is_available
    
    def borrowed(self):
        if self.is_available():
            self.__is_available = False
        
    def returned(self):
        if not self.is_available():
            self.__is_available = True

book = Book()
book.set_title("Pyhton is Ez")
book.set_author("Prog88")
book.set_number_of_pages(123)
book.descriptions()

book.borrowed()
book.descriptions()

book.returned()
book.descriptions()
