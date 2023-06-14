some_dict = {
    (1,2,3) : 'Hello'
}

a =some_dict[(1,2,3)]
print(a)

some_turple = (1,2,3)
print(some_turple, type(some_turple))

some_list = list(some_turple)
print(some_list, type(some_list))

some_tuple= ([1,2,3], 'qwe')
print(some_tuple)

some_tuple[1].replace('qwe', 'rte')
some_tuple[0].append(4)
print(some_tuple)

b = tuple('Hello, world!')
print(b)

c = [1,2,3,4]
d = ['a','b','c','d']
for x in zip(c, d):
    print(x, type(x))