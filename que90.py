while True:
    try:
        num = int(input("Enter an odd number: "))
        if num % 2 != 1:
            raise ValueError("Input is not an odd number!")
        print("Thank you! You entered",num)
    except ValueError as e:
        print(e)
        
