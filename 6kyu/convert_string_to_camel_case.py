def to_camel_case(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join(word.title() for word in words[1:])
