#using files

savingFile = open("chapter16file.txt")
# this is how we open a file in python

# Reading information in files
filecontent = savingFile.read() #the read method return a string with the entire file content

# Separating information with delimiters
content_list = filecontent.split(',')

print(content_list)
print(content_list[0])
print(len(content_list))

file = open('chapter16costumers.txt')
content = file.readlines() #returns a list where each index represents a line of the file

for line in content:
    line = line.strip() #strip method is used to remove any whitespces
    costumer_data = line.split(',')#the split method divid the string into a list according to the delimiter
    print(f"FirstName: {costumer_data[0]}")
    print(f"LastName: {costumer_data[1]}")
    print(f"Age: {costumer_data[2]}")
    
#writing on files

fileW = open("doc_file.txt", "w")
#when you pass the w parameter, every time you write something in the file, the previous content is deleted
#if you want to add some content to the file you need to use the a parameter
fileContent = input("Enter your savings: \n")

fileW.write(fileContent)
fileW = open("doc_file.txt")
print(fileW.read())

fileW.close()