string1 = "abc"
string2 = "xyz"

swapped_string1 = string2[:2] + string1[2:]
swapped_string2 = string1[:2] + string2[2:]

result = swapped_string1 + " " + swapped_string2

print(result)