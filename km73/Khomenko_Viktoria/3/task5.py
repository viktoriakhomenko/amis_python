'''
Умова: Напишіть програму, яка зчитує ціле число і друкує його попереднє і наступне значення за форматом:	
The next number for the number 179 is 180.
The previous number for the number 179 is 178.
'''
n = int(input('n='))
print('The next number for the number', n, 'is', n+1, '\n', 'The previous number for the number', n, 'is', n-1)
