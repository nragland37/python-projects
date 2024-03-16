# ****************************************************************************************************
#
#       This file defines the Employee class.
#
# ****************************************************************************************************


class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id_number(self):
        return self.__id_number

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def __str__(self):
        return (
            f"{self.__name:20}"
            f"{self.__id_number:<20}"
            f"{self.__department:20}"
            f"{self.__job_title:20}"
        )


# ****************************************************************************************************
