class Rectangle:
    def __init__(self):
        self.__width = 0
        self.__height = 0
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height
    
    def set_values(self, new_width, new_height):
        self.__width = new_width
        self.__height = new_height

    def description(self):
        return f"{self.get_width()}" + " " + f"{self.get_height()}"

rectangle = Rectangle()
print(rectangle.description())

rectangle.set_values(10,5)
print(rectangle.description())
