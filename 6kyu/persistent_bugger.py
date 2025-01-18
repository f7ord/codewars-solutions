def persistence(n):
    if n < 10:
        return 0
    
    temp = 1
    for i in str(n):
        temp *= int(i)
    return 1 + persistence(temp)
