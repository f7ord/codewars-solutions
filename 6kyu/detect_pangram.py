def is_pangram(st):
    return len(set(''.join(i.lower() for i in st if i.isalpha()))) == 26
