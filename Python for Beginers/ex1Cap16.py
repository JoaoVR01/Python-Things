'''
Write a program that displays the names of songs released in 2000. 
Hint: you could use the following statement inside the loop body: if(int(songData[4]) == 2000):
'''

fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()
i = 1
while(i < len(contentCsv)):
    line = contentCsv[i].strip().split(",")
    if int(line[4]) == 2000:
        print(line[1])
    i += 1