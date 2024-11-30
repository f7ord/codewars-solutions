def digital_root(n):
    if n < 10:
        return n
    x = sum(int(i) for i in str(n))
    return digital_root(x)
