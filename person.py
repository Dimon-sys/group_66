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

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age
        
person = Person('Иван', 2)
print(person.name)
print(person.age)
person.name = 'Данил'
person.age = 21
print(person.name)
print(person.age)
        