'''
Write a program that displays how many songs have a duration of more than 400000 milliseconds.
'''
fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()

i = 1
counter = 0
while i < len(contentCsv):
    line = contentCsv[i].strip().split(",")
    if int(line[2]) > 400000:
        print(f"Music: {line[1]}| Duration: {line[2]}")
        counter+=1
    i+=1

print(f"{counter} songs have a duration of more than 400000 milliseconds.\n")