def remove_non_int(lst):
    if not lst:
        return lst
    type_counts = {}
    for item in lst:
        t = type(item)
        type_counts[t] = type_counts.get(t, 0) + 1
    if len(type_counts) == 2 and int in type_counts and 1 in type_counts.values():
        return [x for x in lst if isinstance(x, int)]
    else:
        return lst