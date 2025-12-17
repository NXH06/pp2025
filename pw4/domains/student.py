class Student:
    def __init__(self, id, name, dob):
            self.__id = id
            self.__name = name
            self.__dob = dob
    @classmethod
    def empty(cls):
        return cls("", "", "")
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def dob(self):
        return self.__dob
    @id.setter
    def id(self, id):
        self.__id = id
    @name.setter
    def name(self, name):
        self.__name = name
    @dob.setter
    def dob(self, dob):
        self.__dob = dob
    def __str__(self):
        return f"{self.__id} | {self.__name} | {self.__dob}"