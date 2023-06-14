n = int(input())
lst = list()
for i in range(n): lst.append(int(input()))
print(lst)
_min = min(lst)
ind_min = lst.index(_min)
_max = max(lst)
ind_max = lst.index(_max)
lst[ind_min] = _max
lst[ind_max] = _min
print(lst)

