print("Кінь")

x1 = int(input("Введіть номер рядку першої клітини: "))
y1 = int(input("Введіть номер стовчика першої клітини: "))
x2 = int(input("Введіть номер рядку другої клітини: "))
y2 = int(input("Введіть номер стовпчика другої клітини: "))


if ((x1-x2 == 1 or x1-x2 == -1) and (y1-y2 == 2 or y1-y2 == -2)) or ((x1-x2 == 2 or x1-x2 == -2) and (y1-y2 == 1 or y1-y2 == -1)):
    print("YES")
else:
    print("NO")

