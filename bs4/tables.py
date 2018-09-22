import bs4 as bs
from urllib import request
#import pandas as pd

url = 'https://pythonprogramming.net/parsememcparseface/'
response = request.urlopen(url).read()

soup = bs.BeautifulSoup(response, 'lxml')

table = soup.find('table') # Get the first table

for tr in table.find_all('tr'):
    data = [td.text for td in tr.find_all('td')]
    print(data)

# Will read the page and return all the tables
#df = pd.read_html(url)
