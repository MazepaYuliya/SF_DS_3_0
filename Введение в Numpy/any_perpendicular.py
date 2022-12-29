import numpy as np

def any_normal(*vectors):
    """
    Напишите функцию которая принимает на вход неограниченное число векторов через запятую. 
    Гарантируется, что все векторы, которые передаются, одинаковой длины.

    Функция возвращает True, если есть хотя бы одна пара перпендикулярных векторов. 
    Иначе возвращает False.
    """
    vectors_len = len(vectors)
    is_perpendicular = False
    for ind_left in range(vectors_len):
        for ind_right in range(ind_left+1, vectors_len):
            if np.dot(vectors[ind_left], vectors[ind_right]) == 0:
                return True
    return False

vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3,4])
print(any_normal(vec1, vec2, vec3))