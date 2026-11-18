from functools import reduce

numbers = [10, 25, 5, 80, 45, 60]
largest= reduce(lambda a, b: a if a >b else b, numbers)
print("largest number :", largest)
