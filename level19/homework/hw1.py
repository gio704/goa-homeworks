list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
sorted_combined = []
def combine_and_sort_lists(list1, list2):
    combined = list1 + list2
    sorted_combined = sorted(combined) 
    return sorted_combined
print(sorted_combined)