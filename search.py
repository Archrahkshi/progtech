from typing import List

from data_structures_lab23 import Marriage, marriages_bad_hash, marriages_good_hash
import hash


def linear_search(marriages: List[Marriage], query: str) -> List[Marriage]:
    """
    Алгоритм прямого поиска объекта в списке.
    :param marriages: Список объектов типа Marriage.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    return [marriage for marriage in marriages if marriage.groom_name == query]


def binary_search(marriages: List[Marriage], query: str) -> List[Marriage]:
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
        return [marriages[middle_bound]] if marriages[middle_bound].groom_name == query else []
    else:
        results = []
        flag_left, flag_right = True, True
        for i in range(right_bound-middle_bound):
            if flag_left:
                if marriages[middle_bound - i].groom_name == query:
                    results.append(marriages[middle_bound - i])
                else:
                    flag_left = False
            if flag_right:
                if marriages[middle_bound + i + 1].groom_name == query:
                    results.append(marriages[middle_bound + i + 1])
                else:
                    flag_right = False
        return results


def hash_table_search(size: int, algorithm: str, query: str) -> List[Marriage]:
    """
    Алгоритм поиска объекта по хешу.
    :param size: Размер коллекции для поиска.
    :param algorithm: Алгоритм поиска - плохой или хороший.
    :param query: Строка, содержащая ФИО жениха.
    :return: Список найденных объектов.
    """
    if algorithm == 'bad':
        return marriages_bad_hash[size][hash.bad(query)]
    else:
        return marriages_good_hash[size][hash.good(query)]
