"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*arguments):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    temp_list = list(arguments)
    for i in range(0, len(temp_list)):
        temp_list[i] = temp_list[i] ** 2
    arguments = tuple(temp_list)
    return (arguments)

# filter types
ODD = "odd" # нечетное
EVEN = "even"   # четные
PRIME = "prime" # простое


def is_prime(*arguments):
    my_list = []
    temp_list = arguments[0]
    for i in range(0, len(temp_list)):
        if (temp_list[i] > 1):
            for n in range(2, temp_list[i]):
                if (temp_list[i] % n) == 0:
                    break
            else:
                my_list.append(temp_list[i])
    return (my_list)

def filter_numbers(*arguments):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    my_list = []
    temp_list = arguments[0]
    if arguments[1] == "odd":
        for i in range(0, len(temp_list)):
            if (temp_list[i] % 2) != 0:
                my_list.append(temp_list[i])
    if arguments[1] == "even":
        for i in range(0, len(temp_list)):
            if (temp_list[i] % 2) == 0:
                my_list.append(temp_list[i])
    if arguments[1] == "prime":
        my_list = is_prime(temp_list)
    return (my_list)
