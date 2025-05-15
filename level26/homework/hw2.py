def most_common_type(lst):
    type_counts = {}
    
    for item in lst:
        t = type(item)
        type_counts[t] = type_counts.get(t, 0) + 1

    most_common = max(type_counts, key=type_counts.get)
    print(f"ყველაზე ხშირი ტიპია: {most_common.__name__}")