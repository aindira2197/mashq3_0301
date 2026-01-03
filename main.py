#1-misol
N = int(input("N ni kiriting: "))

a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b

#2-misol
N = int(input("N ni kiriting: "))

for son in range(2, N + 1):
    tub = True
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            tub = False
            break
    if tub:
        print(son, end=" ")

#3-misol
sonlar = list(map(int, input("Raqamlarni probel bilan kiriting: ").split()))

# Oddiy tanlash (selection sort)
for i in range(len(sonlar)):
    min_index = i
    for j in range(i + 1, len(sonlar)):
        if sonlar[j] < sonlar[min_index]:
            min_index = j
    sonlar[i], sonlar[min_index] = sonlar[min_index], sonlar[i]

print("Saralangan ro'yxat:", sonlar)
