'''
Умова: Дано два цілих числа. Вивести найменше з них.
'''
first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))
if first_number<second_number:
    print(first_number)
elif second_number<first_number:
    print(second_number)
else:
    print("no data")
    
