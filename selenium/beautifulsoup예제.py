# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))

# 20210209
