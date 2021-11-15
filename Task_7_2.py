


#Task_7_2
n = input("Выберите один из переводов, введите цифру от 1 до 12: ")
print(n)
while True:
    print("Выход из программы 0")
    if n == "1":
        x = float(input('Введите число дюймов: '))
        def inch(x):
            z = x * 2.54
            return z
        z = inch(x)
        print(z, "сантиметров")
        if x == 0:
            break
    elif n == "2":
        x = float(input('Введите число сантиметров: '))
        def sm(x):
            z = x * 0.393701
            return z
        z = sm(x)
        print(z, "дюйм")
        if x == 0:
            break
    elif n == "3":
        x = float(input('Введите число миль: '))
        def mile(x):
            z = x * 1.609344869046
            return z
        z = mile(x)
        print(z, "километров")
        if x == 0:
            break
    elif n == "4":
        x = float(input('Введите число километров: '))
        def km(x):
            z = x * 0.6213715277778704138
            return z
        z = km(x)
        print(z, "миль")
        if x == 0:
            break
    elif n == "5":
        x = float(input('Введите число фунтов: '))
        def funt(x):
            z = x * 0.453592
            return z
        z = funt(x)
        print(z, "килограмм")
        if x == 0:
            break
    elif n == "6":
        x = float(input('Введите число килограмм: '))
        def kg(x):
            z = x * 2.204620823516057
            return z
        z = kg(x)
        print(z, "фунтов")
        if x == 0:
            break
    elif n == "7":
        x = float(input('Введите число унций: '))
        def unc(x):
            z = x * 28.34950000001049375
            return z
        z = unc(x)
        print(z, "грамм")
        if x == 0:
            break
    elif n == "8":
        x = float(input('Введите число грамм: '))
        def gram(x):
            z = x * 0.035273933176256912214
            return z
        z = gram(x)
        print(z, "унций")
        if x == 0:
            break
    elif n == "9":
        x = float(input('Введите число галлонов: '))
        def gallon(x):
            z = x * 3.78541
            return z
        z = gallon(x)
        print(z, "литров")
        if x == 0:
            break
    elif n == "10":
        x = float(input('Введите число литров: '))
        def litr(x):
            z = x * 0.26417192785386
            return z
        z = litr(x)
        print(z, "галлон")
        if x == 0:
            break
    elif n == "11":
        x = float(input('Введите число пинт: '))
        def pinta(x):
            z = x * 0.47317624999192797741
            return z
        z = pinta(x)
        print(z, "литров")
        if x == 0:
            break
    elif n == "12":
        x = float(input('Введите число литров: '))
        def ltr(x):
            z = x * 2.1133754228308800904
            return z
        z = ltr(x)
        print(z, "пинт")
        if x == 0:
            break
    else:
        print("Выбор неверен. Внимательно читайте условие")
        break







