# open the flie in append mode 
with open("my_story.txt", "a") as flie:
 flie.write ("2026-07-22\n")
 print("Date appended successfully!")
 #verify the flie contents 
 with open("my_story.txt","r")as flie:
     print(flie.read())