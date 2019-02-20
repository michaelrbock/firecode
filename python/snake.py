def find_spiral(matrix):
    output = []
    top, left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    while len(output) < len(matrix) * len(matrix[0]):
        # Add top row.
        for i in range(left, right + 1):
            output.append(matrix[top][i])
        top += 1
        # Add right col.
        for i in range(top, bottom + 1):
            output.append(matrix[i][right])
        right -= 1
        # Add bottom row.
        if top <= bottom:
            for i in range(right, left - 1, -1):
                output.append(matrix[bottom][i])
            bottom -= 1
        # Add left col.
        if left <= right:
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
    return output
