try:
    a,b=eval(input("Enter two numbers to be divided"))
    print("Result=",a/b)
except ZeroDivisionError as z:
    print("Exception occured",z)
except SyntaxError as s:
    print("You hsve missed a comma between two numbers",s)
except:
    print("Wrong input")
else:
    print("No exception occured")
finally:
    print("The exceptions are over")