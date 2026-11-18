def invoice( student_name, *args, **kwargs):
    print("Student: {student_name}")
    
    total = sum(args)
    print("total items price:", total)
    
    print("extra details:")
    for key,value in kwargs. items():
        print(key,":",value)
        
    
    