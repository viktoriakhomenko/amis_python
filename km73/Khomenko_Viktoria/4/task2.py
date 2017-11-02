'''
Вивести результат функціїsign(x), що визначається наступним чином: 
sign(x) = 1, if x > 0, 
sign(x) = -1, if x < 0, 
sign(x) = 0, if x = 0.
'''
x=float(input("x="))
if x > 0:
    answer="sign(x) = 1"
elif x < 0:
     answer="sign(x) = -1"
else:
    answer="sign(x) = 0"
print(answer)
