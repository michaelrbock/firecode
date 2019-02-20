def bubble_sort(a_list):
    for i in range(len(a_list) - 1):
        for j in range(i+1, len(a_list)):
            if a_list[i] > a_list[j]:
                a_list[i], a_list[j] = a_list[j], a_list[i]
    return a_list
