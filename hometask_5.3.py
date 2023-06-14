a = [1, 4, -3, 0, 10]
lena = len(a) 
for i in range(1, lena): 
    for j in range(lena - 1, i - 1, -1): 
        if a[j - 1] > a[j]: 
            a[j - 1], a[j] = a[j], a[j - 1] 
print(*a)