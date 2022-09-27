import random 
import csv 
#Sarah Vasquez 

#creating the dictionary 
def makeDictionary():
    movieDict={} 
    with open('movies.csv', mode = 'r') as infile:
        reader=csv.reader(infile) 
        movieDict = { col[0]:[ col[1], col[2],col[3], col[4] ] for col in reader}
 #returning dictionary of all movies        
    return (movieDict)

def genreList (makeDictionary, g): 

 #get input of which genre user wants to see   
 genre = str(input("What genre would you like to watch?\nEnter Here: ")) 
 
 #creating a new dictionary of only the movies with genres from input
 genreDict = {}

#getting the list of name of the movies (NOT INFO OF MOVIE aka. Description, Year, Ranking)
 list_of_keys = [key for key, list_of_movies in makeDictionary.items() if genre in list_of_movies] 

#creaiting dictionary based on the list of movies and retrieving info of the movie
 genreDict = {x:makeDictionary[x] for x in list_of_keys}

#number of how many movies are in the genre category 
 numOfList = len(list_of_keys)

 print("We found", numOfList, "movie(s) in this category, would you like to display the list or send it to the random generator to pick a movie for you?")
 ds = input("Enter either: Display or Random: ") 

 if ds == "Display": 
    print(genreDict.keys()) 
 else:
    randomList(genreDict) 

 
def randomList(dictionary): 

    moviePick = random.choice(list(dictionary.keys()))
    print("Your selected movie is", moviePick) 
    descriptions = input("Would you like to see more info about the movie? Y/N: ") 
    if descriptions == "Y": 
        print(dictionary[moviePick])
    if descriptions == "N": 
        exit()


    return 0

def rankList(dictionary, IMBDrank): 

    num = int(input("Enter a number from 1-250: ")) 

    my_list = [] 
    for i in dictionary.values():
        my_list.append(i)
    
    key_list= list(dictionary.keys())
    val_list = list(dictionary.values()) 

    position = val_list.index(my_list[num]) 
    print(key_list[position], my_list[num])
        

    return 0

 


def main():
    #heading
    print("Random Movie Genorator\n") 
    makeDictionary()

 
    usrInput = str(input("Would you like a random movie? Specific ranking? or Specific Genre? \n Enter Here: "))

    if usrInput.lower() == "genre" :
        print("true")
        genreList(makeDictionary(), usrInput)
    if usrInput.lower() == "ranking" : 
        rankList(makeDictionary(), usrInput)
    if usrInput.lower() == "random": 
        randomList(makeDictionary())  
        
    


#numOfListMovies = int(input("\nHow many movies would you like listed.\nChoose between 1 - 10\nEnter Here: ")) 
main()