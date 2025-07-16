product = "Laser-100-20"

index = product.find("-")
#first we find the first - to use its index to find the another -
index2 = product.find("-", index + 1)
#with the second - index we can print the quantity
quantity = product[index2 + 1 : len(product)]
#the quantity will always start in the index2 + 1 (int this case)
print(quantity)

print("-----------------------------------")
#loops with strings
word = input("Enter any word: ")
i = 0
while i < len(word):
    print(word[i])
    i += 1
print("-----------------------------------")

text = 'Ginza'
print(text[0])
print(text[0:3]) #the character in the index 3 doesn't count 
indexZ = text.find("z")
print(indexZ)