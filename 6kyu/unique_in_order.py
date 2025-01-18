def unique_in_order(sequence):
    if not sequence:
        return []
    ans = [sequence[0]]
    for i in sequence:
        if ans[-1] != i:
            ans.append(i)
    return ans
