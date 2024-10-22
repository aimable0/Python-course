from urllib import request
from bs4 import BeautifulSoup
import re



def get_data(url):
    data  = request.urlopen(url)
    html = data.read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a') 
    nexturl = tags[17].get('href', None)
    return nexturl


url = "http://py4e-data.dr-chuck.net/known_by_Raja.html"
n = 0
while (n < 7):
    url = get_data(url)
    print("Retrieving: ", url)
    n += 1

print(f'last url: {url}')

print("The name in the last url: {name}".format(name = re.findall("(B.+).html$", url)[0]))


