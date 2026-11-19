def make_validator(min_value):
    
 def validator(number):
    if number >= min_value:
     return True
    else: 
        return False
    
    return validate
validator1 = make_validator
validator2 = make_validator

print(validator1(20))
print(validator1(15))
print(validator1(18))

print(validator2(60))
print(validator2(40))
print(validator2(50))
        
      
 