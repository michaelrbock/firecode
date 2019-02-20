def decode_string(msg):
    # memo[i] = number of ways to decode msg[:i]
    memo = [0] * (len(msg) + 1)
    for i in range(len(msg)):
        if i == 0 and msg[i] != '0':
            memo[i] = 1
            memo[i+1] = 1
            continue
        # Take 1.
        memo[i+1] = memo[i-1]
        # Take 2 optionally.
        if msg[i] != '0' and int(msg[i-1:i+1]) > 0 and int(msg[i-1:i+1]) <= 26:
            memo[i+1] += memo[i-2]
    return memo
