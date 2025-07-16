'''
Write a program that displays the names of songs that start with the letter "D". 
'''

fileCsv = open("songs.csv", encoding="utf-8")
contentCsv = fileCsv.readlines()

for line in contentCsv:
    line = line.strip().split(",")
    music_name = line[1].lower()
    if music_name.find("d") == 0:
        print(line[1])