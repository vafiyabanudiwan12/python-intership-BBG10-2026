marks =[80, 75, 90, 65, 70]
total =0
for mark in marks:
    # Error : Incorrect assignment operator (=)
    total += mark
    Percentage =total / (len(marks)* 100)*100
    if Percentage >= 35:
        result ="PASS"
    else:
        result ="FALL"
        print("Total:", total)
        print("percentage:",Percentage)
        print("Result:",result)