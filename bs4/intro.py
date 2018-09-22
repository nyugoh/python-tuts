import bs4 as bs
from urllib import request

# Get the page
sause = request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

# Convert to BS object
soup = bs.BeautifulSoup(sause,  'lxml')

# Get some element like title
print(soup.title)
print(soup.title.name) # Tag name i.e title
print(soup.title.text) # Get all the text
print(soup.title.string) # Get string, if not child component


# Get all P tags
for p in soup.find_all('p'):
    print(p.text)

# Get all urls tags
for url in soup.find_all('a'):
    print(url.get('href'))

# Get all the text in a page
print(soup.get_text())