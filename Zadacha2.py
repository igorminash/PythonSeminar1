a = int(input("Введите трехзначное число: "))

summa = 0

while a > 0:
    b = a % 10
    a = a // 10
    summa += b

print(summa)

# Второй способ
#print(a // 100 + a // 10 % 10 + a % 10)


# Могли бы вы в комментарии к ДЗ рассказать как внедрить данную проверку в Python
# выдает ошибку object of type int has no len()
# if len(a) != 3: print("Введено неверное число!")