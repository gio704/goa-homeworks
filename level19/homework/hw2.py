def list_with_greater_sum(list1, list2):
    if sum(list1) > sum(list2):
        return list1
    elif sum(list2) > sum(list1):
        return list2
    else:
        return