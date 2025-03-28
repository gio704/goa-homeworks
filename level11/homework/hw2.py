def string_clean(s):
    n = ''
    for i in s:
        if i not in '0123456789':
            n += i
    return n