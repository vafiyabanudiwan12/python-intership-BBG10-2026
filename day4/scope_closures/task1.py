count=0
def my_function():
    global count
    count +=1
    
    my_function()
    my_function()
    my_function()
    print("final count:", count)
    