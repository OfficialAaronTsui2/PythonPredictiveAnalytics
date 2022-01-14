filename = "pizza.txt"

infile = open("C:\Users\aaron\Downloads\pizza.txt", "r") 
text = infile.read()
split = text.split("\n")
result = ""
for line in infile:
    result = result + line + "\n\n"
result = result[0:len(result)-3]
print(result)

infile.close()