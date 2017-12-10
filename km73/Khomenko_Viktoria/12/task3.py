List = input("Enter list: ").split()
empty_list = []
def groups(list, iterator):
    """
    This function is counting elements
    Args:
        list: list
        iterator: integer number
    Returns:
        max number of elements in "group"
    Raises:
        ValueError
    Examples:
        >>>print(func([1, 1, 1, 1, 2, 3], 0))
        4

        >>>print(func([1, 1, s, 2, 2, 3], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if iterator == len(list):
        return max(empty_list)
    list_two = "".join(list)
    count_of_element = list.count(list[iterator])
    if (count_of_element - iterator)*str(list[iterator]) in list_two:
        empty_list.append(count_of_element - iterator)
    return groups(list, iterator + 1)
print(groups(List, 0))

