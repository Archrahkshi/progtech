import numpy as np
from time import time
import pickle

from data_structures_lab23 import SIZES, marriages_sorted, marriages_unsorted, multimaps
from search import linear_search, binary_search
from sort import quick_sort
import plot


timing = {
    'Прямой поиск': [],
    'Бинарный поиск': [],
    'Сортировка и бинарный поиск': [],
    'Поиск по ключу': []
}
for size in SIZES:
    # Случайно выбираем ФИО жениха для поиска
    random_groom = marriages_sorted[size][np.random.randint(size)].groom_name
    print('\nРазмер: {:<6}\t\tИщем:'.format(size), random_groom)

    # Счётчики времени различных видов поиска (в микросекундах)
    linear_time, binary_time, key_time = 0, 0, 0

    # Находим среднее время прямого и бинарного поисков по 50000 попыткам
    for _ in range(50000):
        check = time()
        linear_search(marriages_sorted[size], random_groom)
        linear_time += time() - check

        check = time()
        binary_search(marriages_sorted[size], random_groom)
        binary_time += time() - check

    linear_time *= 20
    print('Прямой поиск.\t\t\t\t\tВремя (мкс): %.2f' % linear_time)
    print('Результат:', *linear_search(marriages_sorted[size], random_groom))
    timing['Прямой поиск'].append(linear_time)

    binary_time *= 20
    print('Бинарный поиск.\t\t\t\t\tВремя (мкс): %.2f' % binary_time)
    print('Результат:', *binary_search(marriages_sorted[size], random_groom))
    timing['Бинарный поиск'].append(binary_time)

    # Находим время бинарного поиска вместе с сортировкой
    check = time()
    binary_search(quick_sort(marriages_unsorted[size]), random_groom)
    check = (time() - check) * 1e3
    print('Сортировка и бинарный поиск.\tВремя (мс):  %.2f' % check)
    print('Результат:', *binary_search(quick_sort(marriages_unsorted[size]), random_groom))
    timing['Сортировка и бинарный поиск'].append(check * 1e3)

    # Находим среднее время поиска по ключу по 50000 попыткам
    for _ in range(50000):
        check = time()
        multimaps[size][random_groom]
        key_time += time() - check

    key_time *= 20
    print('Поиск по ключу.\t\t\t\t\tВремя (нс):  %.2f' % (key_time * 1e3))
    print('Результат:', *multimaps[size][random_groom])
    timing['Поиск по ключу'].append(key_time)

with open('timing', 'wb') as f:
    pickle.dump(timing, f, pickle.HIGHEST_PROTOCOL)

plot.search(timing)
