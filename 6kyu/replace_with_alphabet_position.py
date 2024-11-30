from string import ascii_lowercase

def alphabet_position(text):
    return ' '.join(str(ascii_lowercase.index(x.lower()) + 1) for x in text if x.isalpha())


# other solution
import string

def alphabet_position(text):
    letters = '.' + string.ascii_lowercase
    return ' '.join(str(letters.index(x.lower())) for y in text.split() for x in y if x.isalpha())

