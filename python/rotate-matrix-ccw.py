def transpose(matrix):
    for row in range(len(matrix)):
        for col in range(row + 1, len(matrix)):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

def horizontal_flip(matrix):
    for row in range(len(matrix) // 2):
        for col in range(len(matrix)):
            matrix[row][col], matrix[len(matrix)-row-1][col] = matrix[len(matrix)-row-1][col], matrix[row][col]

def rotate_square_image_ccw(matrix):
    transpose(matrix)
    horizontal_flip(matrix)
    return matrix
