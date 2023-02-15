# Importing modules
from bs4 import BeautifulSoup
import lxml

# Opening content in website.html
with open(file="website.html") as file:
    result = file.read()

# Using soup to read the html file, "lxml" helps soup know what file it is reading
soup = BeautifulSoup(result, "lxml")

# Prints the lines with the title tags
print(soup.title)
# Prints the name of the title tag
print(soup.title.name)
# Prints the string that's between the title tags
print(soup.title.string)
# Printing the whole object
print(soup)
# Prints the object in a more readable format
print(soup.prettify())
# prints the first "p" tag
print(soup.p)
# Prints all the selected tags in a list
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# Prints all the strings in the "a" tags
for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))  # prints variables in the selected tag

# Finding a tag by looking for the id
heading = soup.find_all(name="h1", id="name")
print(heading)
# Finding a tag by looking for the class, by having find instead of find_all is, so it only looks for the first thing
heading_section = soup.find(name="h3", class_="heading")
print(heading_section.getText())
# Finding a specific "a" tag. We know this one is in a "p" tag (it can also be .classes or #ids
company_url = soup.select_one(selector="p a")
print(company_url)
