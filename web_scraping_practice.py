import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#Get the HTML content
r = requests.get(url)
htmlContent = r.content

##Parse the HTML content
soup = BeautifulSoup(htmlContent, "html.parser")
#print(soup.prettify())

### HTML tree Traversal

'''
types of commonly used objects used in web scraping:
1. tag
2.NavigableString
3. BeautifulSoup
4. Comment
'''
title = soup.title
#print(title)

#getting all the paras
paras = soup.find_all("p")
#print(paras)


# to get first paragraph
#print(soup.find('p'))
#get class element in the HTML page
#print(soup.find('p')['class'])


#get text from tags
print(soup.find('p').get_text())


#to get anchor tags from the page
anchors = soup.find_all("a")
all_links = set()
#get all the links on the page
for link in anchors:
    if link.get('href') != '#':
       linkText = "https://codewithharry.com"+link.get('href')
       all_links.add(link)
       print(linkText)

nav_content = soup.find(id ='nav-content')
'''print(nav_content.contents)
print(nav_content.children)
'''
for ele in nav_content.contents:
    print(ele)

for item in nav_content.strings:
    print(item)

print(nav_content.parent.name)
for par in nav_content.parents:
    print(par.name)
