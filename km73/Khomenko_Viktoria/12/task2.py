def maximum_count(list, iterator, sum):
    """
    This function finds the maximum number of elements
    Args:
        list: list
        iterator: integer, index
        sum: integer, 0
    Returns:
        sum: integer, result of the program
    Raises:
        ValueError, OverflowError, ZeroDivisionError
    Examples:
        >>>print(maximum_count([1, 2, 3, 3, 3], 4, 0))
        "3"
    """
    if iterator == -1:
        return sum
    elif list[iterator] == max(list):
        sum += 1
    return maximum_count(list, iterator - 1, sum)


def integer(list, iterator):
    """
    This function converts the elements of list
    Args:
        list: list
        iterator: integer, index
    """
    if iterator == -1:
        return
    list[iterator] = int(list[iterator])
    return integer(list, iterator - 1)


list = input("Enter list: ").split()
integer(list, len(list) - 1)
print(maximum_count(list, len(list) - 1, 0))


        
