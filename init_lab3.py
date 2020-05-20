import pickle
import numpy as np
from time import time

from data_structures_lab23 import SIZES, marriages_unsorted
from search import hash_table_search
import plot


with open('timing', 'rb') as f:
    timing = pickle.load(f)
timing.update({
    'Плохая хеш-функция': [],
    'Хорошая хеш-функция': []
})

for size in SIZES:
    # Случайно выбираем ФИО жениха для поиска
    random_groom = marriages_unsorted[size][np.random.randint(size)].groom_name
    print('\nРазмер: {:<6}\t\tИщем:'.format(size), random_groom)

    # Счётчики времени поиска (в секундах)
    bad_hash_time, good_hash_time = 0, 0

    # Находим среднее время поиска по хешу по 50000 попыткам

    for _ in range(50000):
        check = time()
        hash_table_search(size, 'bad', random_groom)
        bad_hash_time += time() - check
    bad_hash_time *= 20
    print('Поиск в плохой хеш-таблице.\t\t\t\t\tВремя (мкс):  %.2f' % bad_hash_time)
    print('Результат:', *hash_table_search(size, 'bad', random_groom), sep='\n')
    timing['Плохая хеш-функция'].append(bad_hash_time)

    for _ in range(50000):
        check = time()
        hash_table_search(size, 'good', random_groom)
        good_hash_time += time() - check
    good_hash_time *= 20
    print('Поиск в хорошей хеш-таблице.\t\t\t\tВремя (мкс):  %.2f' % good_hash_time)
    print('Результат:', *hash_table_search(size, 'good', random_groom), sep='\n')
    timing['Хорошая хеш-функция'].append(good_hash_time)

plot.search(timing, hash=True)
