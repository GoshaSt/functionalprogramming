def rotate_matrix(matrix):
    rotated_matrix = list(zip(*reversed(matrix)))
    print(rotated_matrix)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_matrix(matrix)
