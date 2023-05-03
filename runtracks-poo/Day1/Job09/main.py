class Student:
    def __init__(self, name, first_name, student_number):
        self.__name = name
        self.__first_name = first_name
        self.__student_number = student_number
        self.__credit = 0
        self.__level = self.__student_eval()
    
    def get_name(self):
        return self.__name
    
    def get_first_name(self):
        return self.__first_name
    
    def get_student_number(self):
        return self.__student_number
    
    def get_credit(self):
        return self.__credit
    
    def get_level(self):
        return self.__level

    def set_name(self, new_name):
        self.__name = new_name
    
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_student_number(self, new_number):
        self.__student_number = new_number

    def add_credits(self, new_value):
        if new_value > 0 and isinstance(new_value, int):
            self.__credit += new_value
            self.__level = self.__student_eval()
        else:
            print("Value have to be a positive integer.\n")
    
    def descriptions(self):
        return f"{self.get_first_name()} {self.get_name()} have {self.get_credit()} credits\n"
    
    def student_info(self):
        return f"Name = {self.get_name()}\nFirstName = {self.get_first_name()}\nId = {self.get_student_number()}\nLevel = {self.get_level()}\n"

    def __student_eval(self):
        if self.get_credit() >= 90:
            return "Excellent"
        elif self.get_credit() >= 80:
            return "Very good"
        elif self.get_credit() >=70:
            return "Good"
        elif self.get_credit() >= 60:
            return "Fair"
        else:
            return "Poor"

aStudent = Student("Doe", "John", "888")

aStudent.add_credits(50)
print(aStudent.student_info())

aStudent.add_credits(10)
print(aStudent.student_info())

aStudent.add_credits(10)
print(aStudent.student_info())

aStudent.add_credits(-10)

aStudent.add_credits(10)
print(aStudent.student_info())

aStudent.add_credits(10)
print(aStudent.student_info())

