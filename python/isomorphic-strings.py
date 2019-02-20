def are_isomorphic(input1, input2):
    if input1 is None or input2 is None:
        return False
    if len(input1) == 0 and len(input2) == 0:
        return True

    one_two = {}
    two_one = {}
    for i in range(len(input1)):
        if input1[i] in one_two and one_two[input1[i]] != input2[i]:
            return False
        if input2[i] in two_one and two_one[input2[i]] != input1[i]:
            return False
        one_two[input1[i]] = input2[i]
        two_one[input2[i]] = input1[i]
    return True
