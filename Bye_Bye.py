valid=True
while valid:
    try:
        num=int(input("Please enter a number to be divided by 2"))
        while num%2==0:
            print("Bye")
        valid=False


    except:
        print("Invalid")