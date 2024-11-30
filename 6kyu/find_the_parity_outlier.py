def find_outlier(integers):
    odd, even = 0, 0
    for i in integers:
        if i%2:
            odd += 1
        else:
            even += 1
    for i in integers:
        if odd > 1 and not i % 2:
            return i
        elif even > 1 and i % 2:
            return i