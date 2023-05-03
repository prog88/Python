class Car:
    def __init__(self):
        self.__brand = ""
        self.__model = ""
        self.__year = ""
        self.__mileage = 0
        self.__running = True
        self.__tank = 50

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_milage(self):
        return self.__mileage
    
    def get_running(self):
        return self.__running
    
    def __get_tank(self):
        return self.__tank
    
    def is_tank_full(self):
        return self.__tank == 100

    def set_mileage(self, new_mileage):
        if new_mileage >= 0 and isinstance(new_mileage, int):
            self.__mileage = new_mileage
        else:
            print("mileage must be positive integer")

    def start_engine(self):
        if not self.__running and self.__get_tank() >= 5 :
            self.__running = True
    
    def is_started(self):
        return self.__running
    
    def stop_engine(self):
        if self.is_started():
            self.__running = False
