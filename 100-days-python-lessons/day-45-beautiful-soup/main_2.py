# importing modules
from bs4 import BeautifulSoup
import requests
import lxml

# Getting the html in text form from the hacker news website
response = requests.get(url="https://news.ycombinator.com/news")
yc_website = response.text

# Using soup to read the file from the api response
soup = BeautifulSoup(yc_website, "lxml")
# Printing the title
print(soup.title)

# Printing the first headline on the site
all_headlines = soup.find_all(name="span", class_="titleline")
first_heading = soup.select_one(selector=".titleline span a")
article_text = first_heading.getText()
print(article_text)

# Getting the article link and upvote score
article_link = first_heading.get("href")
upvote = soup.find(name="span", class_="score")
all_upvote = soup.find_all(name="span", class_="score")
article_upvote = upvote.getText()
print(article_link)
print(article_upvote)

# Making 3 list
all_article_upvote_list = []
all_article_headlines_list = []
all_article_links_list = []

# Appending all the headlines into the list
for tag in all_headlines:
    all_article_headlines = tag.getText()
    all_article_headlines_list.append(all_article_headlines)

# Appending all the links into the list
all_a_elements = soup.select(selector=".titleline span a")
for tag in all_a_elements:
    all_article_links_list.append(tag.get("href"))

# Appending all the upvote scores into the list
for upvote_tag in all_upvote:
    all_article_upvote = upvote_tag.getText().split()
    all_article_upvote_list.append(int(all_article_upvote[0]))

# Getting highest upvote number
highest_upvote = max(all_article_upvote_list)
highest_upvote_index = all_article_upvote_list.index(highest_upvote)


# Function to print an item from each list
def print_headlines(index):
    print(all_article_headlines_list[index])
    print(all_article_upvote_list[index])
    print(all_article_links_list[index])
    print("\n")


# Calling the print_headlines() function over and over until it reaches 11 reps or runs out of list items
for index in range(10):
    try:
        print_headlines(index)
    except IndexError:
        print("No more headlines.")

# Finding the highest upvote headline
print(f"\nThe hottest story right now is \"{all_article_headlines_list[highest_upvote_index]}\" with an upvote score of"
      f" {all_article_upvote_list[highest_upvote_index]}!. Here is the link: "
      f"{all_article_links_list[highest_upvote_index]}")
