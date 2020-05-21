def bad(key: str) -> int:
    """
    Выполняет хеширование строки key по "плохому" алгоритму с коллизиями.
    :param key: Строка для хеширования.
    :return: Хеш.
    """
    hash = 0
    for _ in range(4):
        for i, el in enumerate(key):
            hash += ((i * ord(el)) ^ hash * 11) & 0xFFFFFFFF
    return hash


def good(key: str) -> int:
    """
    Выполняет хеширование строки key по "хорошему" алгоритму rot13 с малым числом коллизий.
    :param key: Строка для хеширования.
    :return: Хеш.
    """
    hash = 0
    for i in key:
        hash = (hash * 1664525) + ord(i) + 1013904223
    return hash
