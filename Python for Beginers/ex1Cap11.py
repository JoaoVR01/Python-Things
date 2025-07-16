'''
Write a program in which you ask the user to input four names of their favorite movies through the keyboard. 
Then, add each of those names to a list, and finally, print the list.
'''
movies = []
i = 0
while i < 4:
    movie = input("Enter your top 4 movies: ")
    movies.append(movie)
    i+=1
i = 0
while i < 4:
    print(movies[i])
    i+=1