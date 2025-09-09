import random

import numpy as np

n = 3
m = 2


def create_matrix(n: int = 3, m: int = 2) -> np.ndarray:
    return np.array([[random.randint(0, 1) for _ in range(m)] for _ in range(n)])


def multiply_numpy(matrix_1: np.ndarray, matrix_2: np.ndarray) -> np.ndarray:
    # return np.matmul(matrix_1, matrix_2)
    # return matrix_1 @ matrix_2
    return np.dot(matrix_1, matrix_2)


def multiply(matrix_1: np.ndarray, matrix_2: np.ndarray) -> np.ndarray:
    if matrix_1.shape[1] != matrix_2.shape[0]:
        raise ValueError("Matrices of given shapes cant be multiplied")
    
    result = np.zeros(shape=(matrix_1.shape[0], matrix_2.shape[1]))
    for i in range(matrix_1.shape[0]):
        for j in range(matrix_2.shape[1]):
            for k in range(matrix_1.shape[1]):
                result[i][j] += matrix_1[i][k]*matrix_2[k][j]
    return result


matrix_1 = create_matrix(n, m)
matrix_2 = create_matrix(m, n)

print(multiply(matrix_1, matrix_2))
