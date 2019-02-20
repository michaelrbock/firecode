def merge_ranges(input_range_list):
    if not input_range_list: return []
    merged_ranges = [input_range_list[0]]
    for i in range(1, len(input_range_list)):
        if merged_ranges[-1].upper_bound >= input_range_list[i].lower_bound:
            merged_ranges[-1].upper_bound = input_range_list[i].upper_bound
        else:
            merged_ranges.append(input_range_list[i])
    return merged_ranges
