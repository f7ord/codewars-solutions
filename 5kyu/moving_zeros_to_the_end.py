def move_zeros(lst):
    return sorted(lst, key=bool, reverse=True)
