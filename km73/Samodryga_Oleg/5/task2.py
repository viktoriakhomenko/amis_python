a=[]
n=int(input("Введить количество элементов "))
d=True
j=0
k=0
l=0
for i in range(n):
    new_element=int(input("Введите новый элемент "))
    a.append(new_element)
while d:
    for j in range(n):
        if j>=1 and a[k]==a[j]:
            l=l+1
    k=k+1
    j=0
    if(k==n):
        d=False
print("Количество пар "+(str)(l/2))
        
    
