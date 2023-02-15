# importing modules
from bs4 import BeautifulSoup
import requests
import lxml

# Setting the url im scarping as a constant
URL = "https://www.timeout.com/film/best-movies-of-all-time"

# Scraping data from the url
response = requests.get(url=URL)
website_html = response.text

# Using soup to scrape the html
soup = BeautifulSoup(website_html, "lxml")

# Finding all the movie title information
title_links = soup.find_all(name="h3", class_="_h3_cuogz_1")

# Making a list of all the movie title information
all_movie_titles = [movie.getText() for movie in title_links]

# Removing the last item in the list as it's not relevant
all_movie_titles.pop()

# Removing   from each movie in the list and adding a space between each number and movie
all_movie_titles_formatted = []
for n in all_movie_titles:
    removed_beginning = n.replace(" ", "")
    all_movie_titles_formatted.append(removed_beginning.replace(".", ") "))

# Writing the movie titles to a .txt file
with open(file="movie_list.txt", mode="w") as file:
    for title in all_movie_titles_formatted:
        file.write(f"{title}\n")
