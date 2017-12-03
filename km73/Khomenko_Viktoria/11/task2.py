"""
This function finds minimum in list
Arfs:
    list: list
    lenght: lenght of list
Returns:
    float number minimum in list
Raises:
    ValueError
"""
def minimum(list, lenght):
    m = max(list)
    if len(list) < 2:
        return float(list[0])
    list.remove(m)
    return minimum(list, lenght - 1)


list = input("Enter list: ").split()
print("The minimum is: ", minimum(list, len(list)))
