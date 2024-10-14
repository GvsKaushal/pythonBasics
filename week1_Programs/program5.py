def remove_duplicates_using_sets(lst):
    return list(set(lst))


my_list = [1, 2, 3, 2, 4, 1, 5]
unique_list = remove_duplicates_using_sets(my_list)
print("Original list:", my_list)
print("Unique list:", unique_list)
