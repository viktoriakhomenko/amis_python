print ("Програма для визначення часу \nВведіть кількість хвилин")
x=int (input())
y=0
while x>59:
    x=x-60
    y=y+1
while y>23:
    y=y-24
print ("Кількість хвилин дорівнює:",x,"\nКількість годин дорівнює:",y)
k=int(input())
