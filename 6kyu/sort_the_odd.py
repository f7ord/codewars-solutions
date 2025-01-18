def sort_array(source_array):
    sorted_odd = sorted([x for x in source_array if x%2])
    for i, j in enumerate(source_array):
        if not j % 2:
            sorted_odd.insert(i, j)
    return sorted_odd
