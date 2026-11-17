students = [{"name": "riya", "marks": 88},
{"name": "aman", "marks": 95},
{"name": "rahul", "marks": 78}]

highest = students[0]
for student in students:
    if student["marks"] > highest["marks"]:
        highest = student
        print("highest marks:", highest["name"])
        print("marks:", highest["marks"])
