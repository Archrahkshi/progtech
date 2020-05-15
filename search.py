def linear_search(marriages, query):
    """
    Алгоритм прямого поиска объекта в списке.
    :param marriages: Список объектов типа Marriage.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    return [marriage.to_str() for marriage in marriages if marriage.groom_name == query]


def binary_search(marriages, query):
    """
    Алгоритм бинарного поиска объекта в списке.
    :param marriages: Список объектов типа Marriage.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    left_bound = 0
    right_bound = len(marriages) - 1
    middle_bound = right_bound // 2
    while marriages[middle_bound].groom_name != query and left_bound < right_bound:
        if query > marriages[middle_bound].groom_name:
            left_bound = middle_bound + 1
        else:
            right_bound = middle_bound - 1
        middle_bound = (left_bound+right_bound) // 2
    if left_bound > right_bound:
        return []
    elif left_bound == right_bound:
        return [marriages[middle_bound].to_str()] if marriages[middle_bound].groom_name == query else []
    else:
        results = []
        flag_left, flag_right = True, True
        for i in range(right_bound-middle_bound):
            if flag_left:
                if marriages[middle_bound - i].groom_name == query:
                    results.append(marriages[middle_bound - i].to_str())
                else:
                    flag_left = False
            if flag_right:
                if marriages[middle_bound + i + 1].groom_name == query:
                    results.append(marriages[middle_bound + i + 1].to_str())
                else:
                    flag_right = False
        return results
