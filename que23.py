s=input("Enter a name:")

if len(s)<2:
    print("Empty string")
else:
    print("Concate string",s[:2]+s[-2:])
        