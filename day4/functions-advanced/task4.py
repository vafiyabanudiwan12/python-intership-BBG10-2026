usernames = ["raj", "rahul123", "amit", "priyanka", "sonu", "ankit123"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print(result)
