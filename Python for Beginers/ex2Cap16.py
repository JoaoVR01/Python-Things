'''
Write a program that displays the names of songs by the artist "Eminem". 
'''

fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()

i = 0
while i < len(contentCsv):
    line = contentCsv[i].strip().split(",")
    if line[0] == "Eminem":
        print(line[1])
    i+=1