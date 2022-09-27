from bs4 import BeautifulSoup 
import requests 
from csv import writer



#the different categories 
# Movie Title, Year, Genre Type, Main Actors, Director 

    
def getGenre(link): 
        htmls = requests.get(link) 
        htmls.raise_for_status() 
        soups = BeautifulSoup(htmls.text,'html.parser')

        section = soups.find('div', {'class': 'ipc-chip-list__scroller'})
        for texts in section:
            genre = texts.find('span', {'class': 'ipc-chip__text'}).text
        return genre

def getDescription(link):
        htmls = requests.get(link) 
        htmls.raise_for_status() 
        soups = BeautifulSoup(htmls.text,'html.parser')

        description = soups.find('span', {'class': 'sc-16ede01-0 fMPjMP'}).text
        return description
        


page = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    #requesting access to the page from URL

page.raise_for_status()
    #for good practice this will let us know whether or not URL was accessed successfully

soup = BeautifulSoup(page.text,'html.parser')
    #this is what allows us to parse and extract info from page
    #the variable soup is the file handler that gives us access to parse
    
ListofMovies = soup.find('tbody', class_= "lister-list").find_all('tr') #should return 250 'tr' tags
    #the variable 'ListofMovies' is what will give us access to the 'tr' tags 
    #finding the parent tag 'tbody' that has an attribute of lister-list

with open('movies.csv', 'w', encoding = 'utf8', newline = '') as f:
    thewriter = writer(f)
    header = ['Movie Title', 'Year','Description', 'Genre', 'Rank'] 
    thewriter.writerow(header) 


    for film in ListofMovies:         
        movieTitle = film.find('td', class_= "titleColumn").a.text 
            
        for link in film.find_all('a') :
            infoLink = 'https://www.imdb.com'+link.get('href')

        genre = getGenre(infoLink) 
        description = getDescription(infoLink)
        year= film.find('td', class_="titleColumn").span.text.strip('()')
        rating = film.find('td', class_="ratingColumn imdbRating").strong.text
        rank = film.find('td', class_ = "titleColumn").text
        
        data = [movieTitle, year, description, genre, rank]
        thewriter.writerow(data)

    
