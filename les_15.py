#1 способ
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
m = []
m.append(n_1)
m.append(n_2)
m.append(n_3)
print(max(m))

#2 способ
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
m = []

lena = len(m) 
for i in range(1, lena): 
    for j in range(lena - 1, i - 1, -1): 
        if m[j - 1] > m[j]: 
            m[j - 1], m[j] = m[j], m[j - 1] 
print(*m)