def insert_star_between_pairs(a_string):
    if not a_string: return
    def insert_star_rec(a_string, so_far):
        if len(a_string) <= 1:
            return so_far + a_string
        if a_string[0] == a_string[1]:
            return insert_star_rec(a_string[1:], so_far + a_string[0] + '*')
        else:
            return insert_star_rec(a_string[1:], so_far + a_string[0])
    return insert_star_rec(a_string, '')
