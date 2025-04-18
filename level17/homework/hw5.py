list1 = (1, 2, 3, 4, 5)
def manual_remove(a, b):
    list2 = []
    G = 0
    for i in a:
        if i != b and G == 0:
            list2 = list2 + [i]
        elif G == 0:
             G += 1
        else:
            list2 = list2 + [i]
    return list2
print(manual_remove(list1, 2))                 