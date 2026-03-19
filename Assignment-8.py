def count_unique_elements(my_list: list) -> int:
    return len(set(my_list))

def remove_duplicates(my_list: list) -> list:
    my_list = set(my_list)
    return list(my_list)

def reverse_list(my_list: list) -> list:
    return my_list[::-1]

def max_value(my_list: list) -> int:
    return max(my_list)

def min_value(my_list: list) -> int:
    return min(my_list)

def sum_values(my_list: list) -> int:
    return sum(my_list)

def average(my_list: list) -> float:
    return sum(my_list) / len(my_list)

def find_index(my_list: list, element: int) -> int:
    if element in my_list:
        return my_list.index(element)
    else:
        return -1

