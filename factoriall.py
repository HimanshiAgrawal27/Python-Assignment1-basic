n=int(input("Enter number"))

fact=1
i=1
while(i<=n):
    fact=fact*i
    print(i,"*",end=" ")
    i=i+1
print("Factorial=",fact)    