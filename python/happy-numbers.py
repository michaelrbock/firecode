def is_happy_number(number):
    seen = set()
    while True:
        total = 0
        while number > 0:
            digit = number % 10
            total += digit * digit
            number = number // 10
        if total == 1:
            return True
        if total in seen:
            return False
        seen.add(total)
        number = total
    return False

