'''
Умова: Дано три цілих числа. Вивести найменше з них.
'''
first_number=int(input("Enter first number:"))
second_number=int(input("Enter second number:"))
third_number=int(input("Enter third number:"))
if second_number>=first_number<=third_number:
    answer=first_number
elif first_number>=second_number<=third_number:
    answer=second_number
else:
    answer="third_number"
print(answer)

