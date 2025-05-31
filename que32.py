original_list = [1, 2, 2, 3, 4, 4, 5, 1, 6, 7, 7, 8]

unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates:", unique_list)
