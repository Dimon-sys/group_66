import random

my_list = [1,2,3,4,5]
list_iterator = iter(my_list)
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))
print(next(list_iterator))

for i in list_iterator:
    print(i)

class RandomIter:
    def __init__(self, limit):
        self.limit = limit
        self.__reload = limit


    def __iter__(self):
        self.limit = self.__reload
        return self
    
    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        
        self.limit -= 1
        return random.randint(0, 100)
    
rand_iter = RandomIter(10)
print(iter(rand_iter))

for rand_int in rand_iter:
    print(rand_int)