try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result = a / b
    print("Result:", result)
    #missing valueError handling 
except ValueError:
    print("Invalid input.")
    
except ZeroDivisionError:
    print("cannot divide by zero.")
    #missing zeroDivisionError handling
         
    