def linear_search(array, query):
    """
    Алгоритм прямого поиска объекта в списке.
    :param array: Список объектов типа Marriage.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    return [element.to_str() for element in array if element.groom_name == query]


def binary_search(array, query):
    """
    Алгоритм бинарного поиска объекта в списке.
    :param array: Список объектов типа Marriage.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    left_bound = 0
    right_bound = len(array) - 1
    middle_bound = right_bound // 2
    while array[middle_bound].groom_name != query and left_bound < right_bound:
        if query > array[middle_bound].groom_name:
            left_bound = middle_bound + 1
        else:
            right_bound = middle_bound - 1
        middle_bound = (left_bound+right_bound) // 2
    if left_bound > right_bound:
        return []
    elif left_bound == right_bound:
        return [array[middle_bound].to_str()] if array[middle_bound].groom_name == query else []
    else:
        results = []
        flag_left, flag_right = True, True
        for i in range(right_bound-middle_bound):
            if flag_left:
                if array[middle_bound-i].groom_name == query:
                    results.append(array[middle_bound-i].to_str())
                else:
                    flag_left = False
            if flag_right:
                if array[middle_bound+i+1].groom_name == query:
                    results.append(array[middle_bound+i+1].to_str())
                else:
                    flag_right = False
        return results
