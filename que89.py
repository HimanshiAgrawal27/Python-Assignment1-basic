try:
    n=int(input("Enter a number"))
    n1=int(input("Enter a number 2"))
    
    print("Divsion=",n/n1)
    
except ZeroDivisionError as e:
    print(e)
else:
    print("Executed")
finally:
    print("It will be executed")           