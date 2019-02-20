def insert_and_merge(input_range_list, new_range):
    if not input_range_list: return [new_range]
    if new_range.lower_bound < input_range_list[0].lower_bound:
        merged = [new_range]
        start = 0
    else:
        merged = [input_range_list[0]]
        start= 1
    merged_in = False
    for i in range(start, len(input_range_list)):
        if new_range.lower_bound <= merged[-1].upper_bound:
            merged[-1].upper_bound = max(merged[-1].upper_bound, new_range.upper_bound)
            merged_in = True
        elif new_range.lower_bound > merged[-1].upper_bound and new_range.upper_bound < input_range_list[i].lower_bound:
            merged.append(new_range)
            merged_in = True

        if input_range_list[i].lower_bound <= merged[-1].upper_bound:
            merged[-1].upper_bound = max(merged[-1].upper_bound, input_range_list[i].upper_bound)
        else:
            merged.append(input_range_list[i])
    if not merged_in:
        merged.append(new_range)
    return merged
