def add_length(str_):
    str = str_.split()
    fin = []
    for i in str:
        fin.append(f"{i} {len(i)}")
    return fin