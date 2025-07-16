#lists

#ages = [1,13,45,66,34,56]
#this is how we create lists
#print(len(ages))
#the len() function can be also used with lists
#split() function break input data at any blankspace in a list
'''
split exemple:
product1 = input()
product_data = product1.split()
print(product_data)
'''
#range(start, stop, step) function generates a int list in a specific gap
#the stop number will be not included in the list
'''
range exemple:
numbers = list(range(1,101)) #the list function create a list with a string, sequence of numbers
'''
words = []
while True:      
    option = str(input("What you want to do: REMOVE, SEE ,STOP, ADD, CLEAR: "))

    if option.lower() == "see":         
        while True:
            see_num = int(input("Enter the number of the word you want to see or enter exit to exit: "))
            if see_num == 0:
                break
            elif see_num > len(words):
                print("Not enough words! ")
                continue #return to the begining of the loop 
            print(words[see_num-1])
    elif option.lower() == "remove":
        while True:
            remove_num = int(input("Enter the number of the word you want to remove: "))
            if remove_num == 0:
                break
            elif remove_num > len(words):
                print("Not enough words!")
                continue
            else:
                print(f"{words[remove_num - 1]} was removed!")
                words.pop(remove_num - 1) #pop is used to remove a specifc item of the list
    elif option.lower() == "add":
        while True:
            word = input("Enter a word: ")
            if word.lower() == "exit":
                break
            else:
                words.append(word)
    elif option.lower() == "stop":
        break
    elif option.lower() == "clear":
        print("Words cleared!")
        words.clear() #remove all the items