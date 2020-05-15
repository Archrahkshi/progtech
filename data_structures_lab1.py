from dataclasses import dataclass
import numpy as np

SIZES = (100, 500, 1000, 5000, 10000, 50000, 100000)  # Размеры баз данных


@dataclass
class Marriage:
    """
    Датакласс, отвечающий за инициализацию объектов типа MarriageOld.
    Инициализация происходит посредством передачи в конструктор класса параметров ниже.
    """
    groom_name: str       # ФИО жениха
    groom_birthday: str   # Дата рождения жениха
    bride_name: str       # ФИО невесты
    bride_birthday: str   # Дата рождения невесты
    marriage_date: str    # Дата свадьбы
    registry_number: str  # Номер ЗАГСа

    def __gt__(self, other):
        """
        Перегрузка оператора ">" для сравнения объектов.
        Сравнение идёт сначала по номеру ЗАГСа, затем по дате свадьбы, затем по ФИО жениха.
        :param other: объект справа от оператора.
        :return: True, если self > other; False - в обратном случае.
        """
        if int(self.registry_number) > int(other.registry_number):
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date > other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if self.groom_name > other.groom_name:
                    return True
        return False

    def __lt__(self, other):
        """
        Перегрузка оператора "<" для сравнения объектов.
        Сравнение идёт сначала по номеру ЗАГСа, затем по дате свадьбы, затем по ФИО жениха.
        :param other: объект справа от оператора.
        :return: True, если self < other; False - в обратном случае.
        """
        if int(self.registry_number) < int(other.registry_number):
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date < other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if self.groom_name < other.groom_name:
                    return True
        return False

    def __ge__(self, other):
        """
        Перегрузка оператора ">=" для сравнения объектов.
        Сравнение идёт сначала по номеру ЗАГСа, затем по дате свадьбы, затем по ФИО жениха.
        :param other: объект справа от оператора.
        :return: True, если self >= other; False - в обратном случае.
        """
        if int(self.registry_number) >= int(other.registry_number):
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date >= other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if self.groom_name >= other.groom_name:
                    return True
        return False

    def __le__(self, other):
        """
        Перегрузка оператора "<=" для сравнения объектов.
        Сравнение идёт сначала по номеру ЗАГСа, затем по дате свадьбы, затем по ФИО жениха.
        :param other: объект справа от оператора.
        :return: True, если self <= other; False - в обратном случае.
        """
        if int(self.registry_number) <= int(other.registry_number):
            return True
        elif int(self.registry_number) == int(other.registry_number):
            if self.marriage_date <= other.marriage_date:
                return True
            elif self.marriage_date == other.marriage_date:
                if self.groom_name <= other.groom_name:
                    return True
        return False


# Создание неотсортированных массивов объектов
marriages = np.empty(len(SIZES), dtype=np.ndarray)
for i, size in enumerate(SIZES):
    with open(f'databases/unsorted/unsorted{size}.txt') as db:
        marriages[i] = np.empty(size, dtype=Marriage)
        for j, line in enumerate(db.readlines()):
            line_words = line.split()
            marriages[i][j] = Marriage(
                groom_name=' '.join(line_words[:3]),
                groom_birthday=line_words[3],
                bride_name=' '.join(line_words[4:7]),
                bride_birthday=line_words[7],
                marriage_date=line_words[8],
                registry_number=line_words[9]
            )
