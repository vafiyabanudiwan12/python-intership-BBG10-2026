# read imput.txt and copy its contents
with open("input.txt","r")as source:
 content = source.read()
# write contents into copy.txt
with open("copy.txt", "w")as destination:
 destination.write(content)
print("file copied successfully!")
