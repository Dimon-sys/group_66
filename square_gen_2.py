def gen():
    for x in range(1000001):
        yield x
        
for x in gen():
    print(x ** 2)