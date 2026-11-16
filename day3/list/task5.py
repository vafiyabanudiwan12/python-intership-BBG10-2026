student=[("john",85), ("alice",92),("bob",78)]
print("student records:")
res=sorted(student,key=lambda x: x[1], reverse=True)
print(res)