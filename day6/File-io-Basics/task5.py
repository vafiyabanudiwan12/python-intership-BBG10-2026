# open the text flie
with open("input.txt", "r")as flie:
 content = flie.read()

 #count the  total number of words 
words =coutent.split()
total_words = len(words)
print("Total number of words:",total_words)
