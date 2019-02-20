def find_partitions(input_list):
    ranges = []
    start = input_list[0]
    for i in range(1, len(input_list)):
        if input_list[i] != input_list[i-1] + 1:
            if start != input_list[i-1]:
                ranges.append(str(start) + '-' + str(input_list[i-1]))
            else:
                ranges.append(start)
            start = input_list[i]
    if start != input_list[-1]:
        ranges.append(str(start) + '-' + str(input_list[-1]))
    else:
        ranges.append(start)
    return ranges
