'''
sentinel-controlled loop
word = ""

while word != "exit":
    word = input("Enter something or enter exit to stop: ")
    if word != "exit":
        print("word saved!")
'''

#using the break statement

while True:
    word = str(input("Enter a word or type exit to stop: "))
    if word == "exit":
        break
    else:
        print("word saved")
        last = word
print(f"The last word saved was {last}")
#an infinite loop that stops with a condition = break instruction
