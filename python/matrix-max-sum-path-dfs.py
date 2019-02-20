# Collections module has already been imported.
def matrix_max_sum_dfs(grid):
    end = len(grid) - 1, len(grid[0]) - 1
    max_total = [0]

    def matrix_max_sum_rec(row, col, total):
        total += grid[row][col]
        if (row, col) == end:
            max_total[0] = max(max_total[0], total)
            return
        if row < len(grid) - 1:
            matrix_max_sum_rec(row + 1, col, total)
        if col < len(grid[0]) - 1:
            matrix_max_sum_rec(row, col + 1, total)

    matrix_max_sum_rec(0, 0, 0)
    return max_total[0]
