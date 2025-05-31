str5 = ['abc', 'aba', '1221', 'ashua', 'zuveriyaz']
count=0
for s in str5:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Number of strings with length >= 2 and same first and last character:", count)
