def rgb(r, g, b):
    ans = ''
    for val in (r,g,b):
        hex_val = hex(min(255, max(0, val)))[2:]
        ans += hex_val.zfill(2)
    return ans.upper()
