a = int(input("Введите шестизначное число: "))

summa1 = 0
summa2 = 0
b = a // 1000
c = a % 1000

while b > 0:
    d = b % 10
    b = b // 10
    summa1 += d

while c > 0:
    f = c % 10
    c = c // 10 
    summa2 += f

if summa1 == summa2:
    print("Число счастливое!")
else:
    print("Число несчастливое(")
    

