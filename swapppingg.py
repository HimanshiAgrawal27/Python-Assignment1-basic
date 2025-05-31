a=int(input("Enter a"))    #swapping without temporary variable
b=int(input("Enter b"))

a=a+b
b=a-b
a=a-b

print("After swapp a is",a)
print("After swapp b is",b)


#swapping with temporary variable

a=int(input("Enter a"))
b=int(input("Enter b"))

temp=a
a=b
b=temp

print("After swapping value of a=",a)
print("After swapping value of b=",b)