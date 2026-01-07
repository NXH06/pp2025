class Course:
    def __init__(self, id, name, credits):
        self.__id = id
        self.__name = name
        self.__credits = credits
    @classmethod
    def empty(cls):
        return cls("", "", 0)
    @property
    def id(self):
        return self.__id
    @property
    def name(self):
        return self.__name
    @property
    def credits(self):
        return self.__credits
    @id.setter
    def id(self, id):
        self.__id = id
    @name.setter
    def name(self, name):
        self.__name = name
    @credits.setter
    def credits(self, credits):
        self.__credits = credits
    def __str__(self):
        return f"{self.id} | {self.name} | {self.credits}"