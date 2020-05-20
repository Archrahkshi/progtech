from dataclasses import dataclass, field
from _collections import defaultdict

from data_structures_lab1 import SIZES
from sort import quick_sort
import hash


@dataclass
class Marriage:
    """
    Датакласс, отвечающий за инициализацию объектов типа Marriage.
    Инициализация происходит посредством передачи в конструктор класса параметров ниже.
    """
    groom_name: str                                 # ФИО жениха
    groom_birthday: str                             # Дата рождения жениха
    bride_name: str                                 # ФИО невесты
    bride_birthday: str                             # Дата рождения невесты
    marriage_date: str                              # Дата свадьбы
    registry_number: str                            # Номер ЗАГСа
    hash: int = field(init=False, repr=False)       # Хеш

    def __gt__(self, other):
        """
        Перегрузка оператора ">" для сравнения объектов.
        Сравнение идёт сначала по имени жениха, затем по дате свадьбы, затем по номеру ЗАГСа.
        :param other: объект справа от оператора.
        :return: True, если self > other; False - в обратном случае.
        """
        if self.groom_name > other.groom_name:
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date > other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if int(self.registry_number) > int(other.registry_number):
                    return True
        return False

    def __lt__(self, other):
        """
        Перегрузка оператора "<" для сравнения объектов.
        Сравнение идёт сначала по имени жениха, затем по дате свадьбы, затем по номеру ЗАГСа.
        :param other: объект справа от оператора.
        :return: True, если self < other; False - в обратном случае.
        """
        if self.groom_name < other.groom_name:
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date < other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if int(self.registry_number) < int(other.registry_number):
                    return True
        return False


def fill_from(database):
    """
    Заполняет список объектами типа Marriage.
    :param database: База данных, из которой происходит заполнение.
    :return: Список объектов типа Marriage.
    """
    return [
        Marriage(
            groom_name=' '.join(line_words[:3]),
            groom_birthday=line_words[3],
            bride_name=' '.join(line_words[4:7]),
            bride_birthday=line_words[7],
            marriage_date=line_words[8],
            registry_number=line_words[9]
        ) for line_words in [line.split() for line in database.readlines()]
    ]


# Словарь для списков отсортированных данных с указанием размеров
marriages_sorted = {}
for size in SIZES:
    # Предварительная сортировка данных для бинарного поиска
    with open(f'databases/unsorted/unsorted{size}.txt') as db, \
            open(f'databases/sorted/search/quick{size}.txt', 'w') as file:
        file.writelines(quick_sort(db.readlines()))
    with open(f'databases/sorted/search/quick{size}.txt') as db:
        marriages_sorted[size] = fill_from(db)

# Словарь для списков неотсортированных данных с указанием размеров
marriages_unsorted = {}
for size in SIZES:
    with open(f'databases/unsorted/unsorted{size}.txt') as db:
        marriages_unsorted[size] = fill_from(db)


# Словари для поиска по ключу.
# Ключи - ФИО женихов, значения - объекты типа Marriage.
multimaps = {}

# Хеш-таблицы.
# Ключи - хеши объектов, значения - объекты типа Marriage.
marriages_bad_hash, marriages_good_hash = {}, {}

for size in SIZES:
    # noinspection PyArgumentList,PyArgumentList
    multimaps[size] = defaultdict(list)
    # noinspection PyArgumentList,PyArgumentList
    marriages_bad_hash[size], marriages_good_hash[size] = defaultdict(list), defaultdict(list)
    for marriage in marriages_unsorted[size]:
        multimaps[size][marriage.groom_name].append(marriage)

        marriage.hash = hash.bad(marriage.groom_name)
        marriages_bad_hash[size][marriage.hash].append(marriage)

        marriage.hash = hash.good(marriage.groom_name)
        marriages_good_hash[size][marriage.hash].append(marriage)
