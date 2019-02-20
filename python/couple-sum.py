def couple_sum(number_list, target):
    num_to_index = {}
    for index, num in enumerate(number_list):
        diff = target - num
        if diff in num_to_index:
            return [num_to_index[diff], index + 1]
        num_to_index[num] = index + 1
    return []
