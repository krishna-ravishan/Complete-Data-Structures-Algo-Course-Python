def rotate(matrix):
    # TODO
    matrix1 = [[],
               [],
               []]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix1[i].append(matrix[j][i])
        matrix1[i].reverse()
    matrix = matrix1
    return matrix

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

print(rotate(mat))