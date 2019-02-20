def min_jumps(arr):
    # Strategy: DFS.
    def min_jumps_rec(arr, current, jumps):
        if arr[current] == 0:
            return 0
        if current == len(arr) - 1:
            return jumps
        for jump_size in range(arr[current], -1, -1):
            next_current = current + jump_size
            if next_current < len(arr):
                return min_jumps_rec(arr, next_current, jumps + 1)
    return min_jumps_rec(arr, 0, 0)
