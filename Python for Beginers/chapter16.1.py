#writing in files
while True:
    print("Action menu: \n1-Input Word\n2-Remove Word\n3-Clear\n4-View All\n0-Exit")
    option = int(input())
    match option:
        case 0:
            break
        case 1:#Input word
            with open("Ch16.1Base.txt") as dataBase:
                word_list = dataBase.read().split(',')
            while True:
                newContent = input("Enter a word: ")
                if newContent.lower() == 'exit':
                    break
                elif newContent in word_list:
                    print(f"{newContent} is already in data base, try other word.")
                    continue
                else:
                    with open("Ch16.1Base.txt","a") as dataBase: #with opens end close the file 
                        dataBase.write(newContent + ',')
        case 2: #Remove word
            with open("Ch16.1Base.txt") as dataBase:
                fileContent = dataBase.read().split(',')
                word_remove = input("Enter the word you want to remove: ")
                if word_remove in fileContent:
                    fileContent.remove(word_remove)
                    with open("Ch16.1Base.txt", "w") as dataBase:
                        dataBase.write(",".join(fileContent)) #join turns a list in a string with a separator
                        print(f"{word_remove} has been removed")
                else:
                    print(f"{word_remove} not found")
        case 3: #Clear
            with open("Ch16.1Base.txt", "w") as dataBase:
                confirmation = input("Are you sure you want to clear the data base? Y/N: ")
                if confirmation == "Y":
                    dataBase.write('')
                elif confirmation == "N":
                    print("Process denied")
                    continue
                else:
                    print("Not a option")
                    continue
        case 4: #View
            with open("Ch16.1Base.txt") as dataBase:
                word_list = dataBase.read().split(',')
                print(word_list)