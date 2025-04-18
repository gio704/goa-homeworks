list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
def combine_and_sort_lists(list1, list2):
    combined = list1 + list2

    n = len(combined)
    for i in range(n):
        for j in range(0, n - i - 1):
            if combined[j] > combined[j + 1]:
                combined[j], combined[j + 1] = combined[j + 1], combined[j]

    return combined
