'''
Умова: Дано координати двох клітин шахової дошки. Визначити, чи однакового вони кольору.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
'''
a=int(input("Enter first number:"))
b=int(input("Enter second numer:"))
c=int(input("Enter third number:"))
d=int(input("Enter fourth number:"))
if (a+b+c+d)%2==0:
    print("YES")
else:
    print("NO")
    
    
