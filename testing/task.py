import math


def sort_by_area(array1):
    sorted_list = sorted(array1, key=lambda item: item[0] * item[1] if isinstance(item, list) else math.pi * item ** 2)
    return sorted_list


array = [[4.23, 6.43], 1.23, 3.444, [1.342, 3.212]]
print(sort_by_area(array))


