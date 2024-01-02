# O(h * w) time | O(w * h) space
def transposeMatrix(matrix):
    result = [[0 for row in range(len(matrix))] for col in range(len(matrix[0]))]
    for row  in range(len(matrix)):
        for col in range(len(matrix[0])):
            result[col][row] = matrix[row][col]
    return result
