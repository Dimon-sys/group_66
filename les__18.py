def func(a, b, *args, **kwargs):
    c = kwargs.get('c', 3)
    print(a)
    print(b)
    print(args)
    print(kwargs)

age = 18
is_allow = age >= 18
print(is_allow)

div_5_list = []
for x in range(100):
    if x % 5 == 0:
        div_5_list.append(x)

print(div_5_list)

div_5_list = [x for x in range(100) if x % 5 == 0]
print(div_5_list)

print([x for x in range(100)])