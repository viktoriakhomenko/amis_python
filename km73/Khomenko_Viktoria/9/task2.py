"""
Дано действительное положительное число a и целоe число n.

Вычислите an. Решение оформите в виде функции power(a, n).
"""
a = float(input("a = "))
n = int(input("n = "))
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)


print(power(a, n))
