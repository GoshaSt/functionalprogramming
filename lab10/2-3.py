def rotate_matrix(matrix):
    # используем функции zip() и reversed() для поворота матрицы
    rotated_matrix = list(zip(*reversed(matrix)))
    print(rotated_matrix)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_matrix(matrix)
