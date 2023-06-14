class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    def get_days(self):
        return self.__days
    
    def get_season(self):
        return self.__season
    
    def set_days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception('Некорректное значение')
        
    def set_season(self, season):
        self.__season = season


year = Year(365, 'зима')
print(year.get_days())
print(year.get_season())
year.set_days(366)
year.set_season('осень')
print(year.get_days())
print(year.get_season())




class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age <= 0:
            raise ValueError('Некорректное значение')
        self.__age = age

person = Person('Иван', 2)
print(person.name)
print(person.age)
person.name = 'Данил'
person.age = 21
print(person.name)
print(person.age)
        