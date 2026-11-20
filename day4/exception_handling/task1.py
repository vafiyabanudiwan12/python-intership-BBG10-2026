def safe_division(a,b):
    try:
        return a / b 
    except ZeroDivisionError :
        print("cannot divide by zero!")
        
    except TypeError:
        print("please enter valid numbers!")
        
        print(safe_division(10, 2))
        print(safe_division(10, 2))
        print(safe_division(10, "hello"))
        