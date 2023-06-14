import time
my_range = range(1, 10)
print(my_range)
print(list(my_range))

my_iter = [time.sleep(x) for x in range(1,3)]
#print(my_iter)

my_iter_1 = (time.sleep(x) for x in range(1, 3))
#print(my_iter_1)

def my_lazy_calc(items):
    for item in items:
        yield item

for item in my_lazy_calc([1,2,3,4,5]):
    print(item)

def my_lazy_func(items):
    yield from items

items = ['Яблоко', 'Банан', 'Апельсин']
for i in my_lazy_func(items):
    print(i)