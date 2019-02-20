def look_and_say(sequence_number):
    if sequence_number <= 0: return None
    num = '1'
    for i in range(sequence_number - 1):
        next_num = ''
        digit = num[0]
        index = 1
        count = 1
        while index < len(num):
            if num[index] == digit:
                count += 1
            else:
                next_num += str(count) + str(digit)
                count = 1
                digit = num[index]
            index += 1
        next_num += str(count) + str(digit)
        num = next_num
    return num
