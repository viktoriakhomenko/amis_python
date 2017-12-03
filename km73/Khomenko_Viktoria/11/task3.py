"""
This function reverse list
Args:
    list: list
Returns:
    reverse list
"""
def reverse(list):
    if (len(list) < 2):
        return list
    else:
        mid = len(list) // 2
        return reverse(list[mid:]) + reverse(list[:mid])


list = input("Enter list: ").split()

print(" ".join(reverse(list)))

        
        
