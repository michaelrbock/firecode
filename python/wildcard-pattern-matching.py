def match(first, second):
    f_index, s_index = 0, 0
    while f_index < len(first) and s_index < len(second):
        if first[f_index] == '*':
            f_index += 1
            while s_index < len(second) and second[s_index] != first[f_index]:
                s_index += 1
        elif first[f_index] == '?':
            f_index += 1
            s_index += 1
        else:
            if first[f_index] != second[s_index]:
                return False
            f_index += 1
            s_index += 1
    return f_index == len(first) and s_index == len(second)
