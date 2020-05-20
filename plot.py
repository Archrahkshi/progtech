from typing import Dict
from matplotlib import pyplot as plt

from data_structures_lab23 import SIZES


def sort(timing: Dict) -> None:
    """
    Построение графиков времени работы алгоритмов сортировки из работы №1.
    :param timing: Словарь с измерениями времени для каждого алгоритма.
    """
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


def search(timing: Dict, hash: bool = False) -> None:
    """
    Построение графиков времени работы алгоритмов поиска из работ №2 и №3.
    :param timing: Словарь с измерениями времени для каждого алгоритма.
    :param hash: Индикатор, влияющий на учёт результатов работы №3.
    """
    plt.figure(figsize=(16, 9))
    plt.plot(SIZES, timing['Прямой поиск'], label='Прямой поиск')
    plt.plot(SIZES, timing['Бинарный поиск'], label='Бинарный поиск')
    plt.plot(SIZES, timing['Сортировка и бинарный поиск'], label='Сортировка и бинарный поиск')
    plt.plot(SIZES, timing['Поиск по ключу'], label='Поиск по ключу')
    if hash:
        plt.plot(SIZES, timing['Плохая хеш-функция'], label='Плохая хеш-функция')
        plt.plot(SIZES, timing['Хорошая хеш-функция'], label='Хорошая хеш-функция')
    plt.grid()
    plt.legend(fontsize=16)
    plt.xlabel('Объём входных данных')
    plt.ylabel('Время поиска, мкс')
    plt.xscale('log')
    plt.yscale('log')
    if hash:
        plt.savefig('lab3_search_timing.pdf')
    else:
        plt.savefig('lab2_search_timing.pdf')
