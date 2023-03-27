def matrix_operation(matrix1, matrix2, operator):
    result = []
    for i, row in enumerate(matrix1):
        new_row = []
        for j, value in enumerate(row):
            if operator == "+":
                new_row.append(matrix1[i][j] + matrix2[i][j])
            elif operator == "-":
                new_row.append(matrix1[i][j] - matrix2[i][j])
            elif operator == "*":
                new_row.append(matrix1[i][j] * matrix2[i][j])
        result.append(new_row)

    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

result = matrix_operation(matrix1, matrix2, "+")
print(result)

result = matrix_operation(matrix1, matrix2, "-")
print(result)

result = matrix_operation(matrix1, matrix2, "*")
print(result)
