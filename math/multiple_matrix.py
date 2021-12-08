matrix_1 = [[1, 4, 5], [4, 5, 6], [2, 4, 1]]
matrix_2 = [
    [4, 5, 8],
    [2, 7, 8],
    [4, 5, 6],
]

result = [[0 for x in range(3)] for y in range(3)]  # create 3x3 matrix multiplication
for i in range(len(matrix_1)):
    for j in range(len(matrix_2[0])):
        for k in range(len(matrix_2)):
            result[i][j] += matrix_1[i][k] * matrix_2[k][j]

for r in result:
    print(r)
