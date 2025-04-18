list1 = [1, 2, 3, 4, 5]
def manual_reverse(a):
    list2 = []
    for i in a:
        list2 = [i] + list2
    return list2
print (manual_reverse(list1))    