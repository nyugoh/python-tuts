import bs4 as bs
from urllib import request

url = 'https://pythonprogramming.net/parsememcparseface/'
response = request.urlopen(url).read()
soup = bs.BeautifulSoup(response, 'lxml')

# find by class
for div in soup.find_all('div', class_='body'):
    print(div.get_text())