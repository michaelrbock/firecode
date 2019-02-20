def largestContinuousSum(arr):
    if not arr: return 0
    max_sum = float('-inf')
    curr_sum = 0
    for elem in arr:
        curr_sum = max(elem, curr_sum + elem)
        max_sum = max(curr_sum, max_sum)
    return max_sum
