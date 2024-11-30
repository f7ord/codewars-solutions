def duplicate_count(text):
    txt = text.lower()
    return sum(1 for i in set(txt) if txt.count(i) > 1)
     