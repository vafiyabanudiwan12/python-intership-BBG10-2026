employees ={ "amit":25000, "rahul":35000, "neha":30000, "priya":45000, "raj": 40000}
sorted_emp = sorted(employees.items(), key=lambda x: x[1], 
reverse=True)
for name, salary in sorted_emp[:3]:
    print(name, salary)