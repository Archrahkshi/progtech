from sys import setrecursionlimit
import numpy as np
from time import time, sleep
from threading import Thread

from generator import generate
from data_structures import SIZES, MarriageOld
from sort import selection_sort, shaker_sort, quick_sort
import plot

setrecursionlimit(5000)


generate()


# Создание неотсортированных массивов объектов
marriages = np.empty(len(SIZES), dtype=np.ndarray)
for i, size in enumerate(SIZES):
    with open(f'databases/unsorted/unsorted{size}.txt') as db:
        marriages[i] = np.empty(size, dtype=MarriageOld)
        for j, string in enumerate(db.read()[:-1].split('\n')):
            data = string.split()
            marriages[i][j] = MarriageOld(
                groom_name=' '.join(data[:3]),
                groom_birthday=data[3],
                bride_name=' '.join(data[4:7]),
                bride_birthday=data[7],
                marriage_date=data[8],
                registry_number=data[9]
            )


# Сортировка и вывод
timing = {'selection': [], 'shaker': [], 'quick': []}
for i, size in enumerate(SIZES):
    marriages_copy = marriages[i].copy()

    def sort_and_output(algorithm):
        check = time()
        if algorithm == 'selection':
            marriages_sorted = selection_sort(marriages_copy)
        elif algorithm == 'shaker':
            marriages_sorted = shaker_sort(marriages_copy)
        elif algorithm == 'quick':
            marriages_sorted = quick_sort(marriages_copy)
        check = time() - check
        timing[algorithm].append(check)
        with open(f'databases/sorted/{algorithm}/{algorithm}{size}.txt', 'w') as file:
            # noinspection PyUnboundLocalVariable
            file.write('\n'.join(map(' '.join, map(lambda e: e.__dict__.values(), marriages_sorted))))
        print('Размер: {:<6}\t\tСортировка: {:<9}\t\tВремя работы: {:<}'.format(size, algorithm, check))


    thread1 = Thread(target=sort_and_output, args=('selection',))
    thread2 = Thread(target=sort_and_output, args=('shaker',))
    thread3 = Thread(target=sort_and_output, args=('quick',))
    thread1.start()
    sleep(.5)
    thread2.start()
    sleep(.5)
    thread3.start()
    sleep(.5)
    thread1.join()
    thread2.join()
    thread3.join()


plot.sort(timing)
