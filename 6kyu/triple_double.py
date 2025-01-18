def triple_double(num1, num2):
    # if none of num1 and num2 contains repeating digits, return 0
    if len(set(str(num1))) == len(str(num1)) or len(set(str(num2))) == len(str(num2)):
        return 0
    str_num1 = str(num1)
    # check for straight triple
    for i, int1 in enumerate(str_num1[:-2]):
        if str_num1[i+1] == int1 and str_num1[i+2] == int1:
            # check for straight double
            str_num2 = str(num2)
            for j, int2 in enumerate(str_num2[:-1]):
                if int2 == int1 and str_num2[j+1] == int1:
                    return 1
    return 0


def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])