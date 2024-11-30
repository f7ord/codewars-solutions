def find_it(seq):
    for num in set(seq):
        if seq.count(num) % 2:
            return num
