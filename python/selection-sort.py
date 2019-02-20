def selection_sort(a_list):
    for i in range(len(a_list)):
        min_index = i
        min_elem = a_list[i]
        for j in range(i, len(a_list)):
            if a_list[j] < min_elem:
                min_elem = a_list[j]
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    return a_list


assert selection_sort([5,4,3,2,1]) == [1,2,3,4,5]