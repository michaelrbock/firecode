# Collections module has already been imported.
def generate_ip_address(input):
    # Return type should be a List.
    results = []

    def gen_ip_address_rec(numbers, remaining_periods, so_far):
        print(numbers, remaining_periods, so_far)
        if remaining_periods == 0:
            if not numbers:  # valid IP.
                results.append(so_far)
            return
        for i in range(1, min(4, len(numbers) + 1)):
            if int(numbers[:i]) >= 0 and int(numbers[:i]) <= 255:
                if remaining_periods == 1:
                    gen_ip_address_rec(numbers[i+1:], remaining_periods - 1, numbers[:i] + '.' + so_far)
                else:
                    gen_ip_address_rec(numbers[i+1:], remaining_periods - 1, numbers[:i] + '.' + so_far)

    gen_ip_address_rec(input, 4, '')
    return results
