import numpy as np


def selection_sort(data):
    """
    Алгоритм сортировки выбором.
    :param data: Массив объектов типа Marriage.
    :return: Отсортированный массив объектов типа Marriage.
    """
    for i in range(len(data)):
        min_value = np.min(data[i:])
        min_index = np.where(data[i:] == min_value)[0]
        data[i+min_index] = data[i]
        data[i] = min_value
    return data


def shaker_sort(data):
    """
    Алгоритм шейкер-сортировки.
    :param data: Массив объектов типа Marriage.
    :return: Отсортированный массив объектов типа Marriage.
    """
    for i in range(len(data)-1, 0, -1):
        swapped = False
        for j in range(i, 0, -1):
            if data[j] < data[j-1]:
                data[j], data[j-1] = data[j-1], data[j]
                swapped = True
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                swapped = True
        if not swapped:
            return data


def quick_sort(data):
    """
    Алгоритм быстрой сортировки.
    :param data: Массив объектов типа Marriage.
    :return: Отсортированный массив объектов типа Marriage.
    """
    less, pivot_list, more = [], [], []
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]
        for i in data:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot_list.append(i)
        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot_list + more
