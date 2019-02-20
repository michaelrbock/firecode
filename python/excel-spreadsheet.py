# Necessary modules have already been imported.
def excel_column_number_to_name(column_number):
    column_number -= 1
    output = []
    while column_number >= 0:
        digit = column_number % 26
        output.append(chr(digit + ord('A')))
        column_number = column_number / 26 - 1
    return ''.join(reversed(output))
