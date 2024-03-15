class Contact:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_phone(self):
        return self.__phone
    
    def set_phone(self, phone):
        self.__phone = phone
    
    def __str__(self):
        return f"{self.__name} : {self.__phone}"