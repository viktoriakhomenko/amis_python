'''
Умова: Шахова королева рухається по горизонталі, по вертикалі або по діагоналі на будь-яку кількість клітин.
Дано координати двох клітин шахової дошки. Визначити, чи може королева перейти з першої клітини у другу за один хід.
Користувач вводить чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика клітини.
Перші два числа - для першої клітини, останні два числа – для другої. Програма має вивести "YES", якщо хід можливий, або "NO" в іншому випадку.
'''
a=int(input('Enter first number'))
b=int(input('Enter second number'))
c=int(input('Enter third number'))
d=int(input('Enter fourth number'))
if abs(a-c)==abs(b-d) or a==c or b==d:
    print('YES')
else:
    print("NO")
    
