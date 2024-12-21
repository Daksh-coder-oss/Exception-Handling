try:
    num=int(input("Please enter a number"))
    print(num)
except ValueError as ex:
    print("Excpetion occured",ex)