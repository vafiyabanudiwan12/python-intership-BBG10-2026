#remove duplicates no from a list

no=[12,70,45,90,30,60,90,83,90,45]
print("original list:",no)
res=[]
for i in no:
    if i not in res:
        res.append(i)
        print("list after removing duplicates:",res)
        