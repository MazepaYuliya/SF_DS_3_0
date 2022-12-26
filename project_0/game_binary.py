"""Игра Угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_search(number: int = 1, min_number: int = 1, max_number: int = 1) -> int:
    """Угадывает число, используя бинарный поиск

    Args:
        number (int, optional): загаданное число. Defaults to 1
        min_number (int, optional): левая граница интервала. Defaults to 1
        max_number (int, optional): правая граница интервала. Defaults to 1

    Returns:
        int: количество попыток
    """
    attempts_count = 1
    predict = (min_number + max_number) // 2  # находим середину интервала
    while number != predict:
        attempts_count += 1
        if number > predict:
            min_number = predict + 1  # сдвигаем нижнюю границу интервала
        elif number < predict:
            max_number = predict - 1  # сдвигаем верхнюю границу интервала
        predict = (min_number + max_number) // 2
    return attempts_count  # выход из цикла, если угадали


def score_game(predict_function, iterations=10000, min_number=1, max_number=100) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_function ([type]): используемая функция для угадывания
        iterations (int, optional): количество итераций. Defaults to 1000
        min_number (int, optional): левая граница интервала. Defaults to 1
        max_number (int, optional): правая граница интервала. Defaults to 100

    Returns:
        int: среднее количество попыток
    """
    count_list = []
    np.random.seed(25)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(min_number, max_number, size=iterations)  # загадали список чисел

    for number in random_array:
        count_list.append(predict_function(number, min_number, max_number))

    score = int(np.mean(count_list))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
