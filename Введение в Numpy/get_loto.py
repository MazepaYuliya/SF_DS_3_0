import numpy as np

def get_loto(num):
    '''
    Напишите функцию генерирующую трёхмерный массив случайных целых чисел от 1 до 100 (включительно). 
    Это поля для игры в лото.

    Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть итоговая форма — (num, 5, 5).
    '''
    return np.random.randint(1, 101, size=(num, 5, 5))


def get_unique_loto(num):
    '''
    Функция аналогична предыдущей, однако теперь на каждом поле 5х5 числа не могут повторяться
    '''
    result = np.zeros((num, 5, 5))
    for ind in range(num):
        result[ind] = np.random.choice(np.arange(1,101), size=(5, 5), replace=False)
    return result

print(get_loto(3))
print(get_unique_loto(3))