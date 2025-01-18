def solution(s):
    return ''.join(f' {w}' if w.isupper() else w for w in s)
