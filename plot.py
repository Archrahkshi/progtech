from matplotlib import pyplot as plt

from data_structures import SIZES


def sort(timing):
    plt.figure(figsize=(16, 9))
    plt.plot(SIZES, timing['selection'], label='Выбором')
    plt.plot(SIZES, timing['shaker'], label='Шейкер')
    plt.plot(SIZES, timing['quick'], label='Быстрая')
    plt.grid()
    plt.legend(fontsize=16)
    plt.xlabel('Объём входных данных')
    plt.ylabel('Время сортировки, с')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('lab1_sort_timing.pdf')


def search(timing):
    plt.figure(figsize=(16, 9))
    plt.plot(SIZES, timing['Прямой поиск'], label='Прямой поиск')
    plt.plot(SIZES, timing['Бинарный поиск'], label='Бинарный поиск')
    plt.plot(SIZES, timing['Сортировка и бинарный поиск'], label='Сортировка и бинарный поиск')
    plt.plot(SIZES, timing['Поиск по ключу'], label='Поиск по ключу')
    plt.grid()
    plt.legend(fontsize=16)
    plt.xlabel('Объём входных данных')
    plt.ylabel('Время поиска, мкс')
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('lab2_search_timing.pdf')
