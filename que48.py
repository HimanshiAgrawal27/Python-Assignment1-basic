my_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}

# Sort by value in ascending order
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending order:", sorted_asc)

# Sort by value in descending order
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending order:", sorted_desc)
