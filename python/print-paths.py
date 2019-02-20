def valid_moves(board, row, col):
    if row == len(board) - 1:
        yield (row, col + 1)
    elif col == len(board[0]) - 1:
        yield (row + 1, col)
    else:
        yield (row + 1, col)
        yield (row, col + 1)


def print_paths(board):
    if not board or not board[0]: return []
    results = []
    def print_paths_rec(board, row, col, path_so_far):
        if row == len(board) - 1 and col == len(board[0]) - 1:
            results.append(path_so_far + board[row][col])
            return
        for next_row, next_col in valid_moves(board, row, col):
            print_paths_rec(board, next_row, next_col, path_so_far + board[row][col])

    print_paths_rec(board, 0, 0, '')
    return results
