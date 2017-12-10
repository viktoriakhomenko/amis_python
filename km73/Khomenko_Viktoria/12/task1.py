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


def second_maximum(list):
    """
    This function finds second maximum in list
    Args:
        list: list
    Returns:
        ValueError, OverflowError, ZerodivisionError
    Examples:
        >>>print(second_maximum([1, 2, 3, 4, 5]))
        "5"
    """
    if len(list) == 0:
        return
    if len(list) == 1:
        return list[0]
    maximum = second_maximum(list[1:])
    return maximum if maximum > list[0] else list[0]


def delete_max(list, iterator):
    """
    This function deletes all maximum element in list
    Args:
        list: list
        iterator: integer, index
    Returns:
        ValueError
    Examples:
        >>>print(delete_max([1, 2, 3, 4], 3))
        "[1, 2, 3]"
        >>>print(delete_max(["sds", 2], 1))
        ValueError
    """
    if iterator == -1:
        return
    if list[iterator] < mx:
        result.append(list[iterator])
    return delete_max(list, iterator - 1)


result = []
list = input("Enter list: ").split()
integer(list, len(list) - 1)
mx = max(list)
delete_max(list, len(list) - 1)

print(second_maximum(result))
