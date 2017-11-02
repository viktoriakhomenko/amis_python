'''
Умова: Дано три цілих числа. Визначте, скільки з них дорівнюють один одному. Програма повинна виводити одне з чисел:
3 (якщо всі числа однакові), 2 (якщо два з них дорівнюють один одному, а третє відрізняється) або 0 (якщо всі числа різні).
'''
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
c=int(input('Enter third number:'))
if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)
    

