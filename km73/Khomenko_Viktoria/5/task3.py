'''
Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз. Елементи потрібно виводити в тому порядку, в якому вони зустрічаються в списку.
'''
X=[int(i) for i in input('Введіть список: ').split()]
a=[]
for n in X:
    if X.count(n)==1:
        a.append(n)
print(a)
    
