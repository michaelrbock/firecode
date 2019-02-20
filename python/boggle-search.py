DIRECTIONS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def _moves(board, visited, row, col):
  for dy, dx in DIRECTIONS:
    next_row = row + dy
    next_col = col + dx
    if next_row >= 0 and next_row < len(
        board) and next_col >= 0 and next_col < len(
            board[0]) and (next_row, next_col) not in visited:
      yield next_row, next_col


def dfs(board, visited, row, col, word):
  if board[row][col] != word[0]:
    return False
  elif len(word) == 1 and board[row][col] == word[0]:
    return True
  visited.add((row, col))
  for next_row, next_col in _moves(board, visited, row, col):
    if dfs(board, visited, next_row, next_col, word[1:]):
      return True
  return False


def boggle_search(board, word):
  if not board or not board[0] or not word:
    return
  for r_index, row in enumerate(board):
    for c_index, cell in enumerate(row):
      if dfs(board, set(), r_index, c_index, word):
        return True
  return False
