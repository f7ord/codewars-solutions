def comp(array1, array2):
    if not array1 or not array2:
        return array1 == array2
    for x in array1:
        if x*x in array2:
            array2.remove(x*x)
        else:
            return False
    return not array2


def comp(array1, array2):
    if not array1 or not array2:
        return array1 == array2
    return sorted(x*x for x in array1) == sorted(array2)
