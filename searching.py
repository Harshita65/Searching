import urllib.request,urllib.parse,urllib.error
import requests
from bs4 import BeautifulSoup
import re
keyword = input('Enter a keyword:')
req = urllib.request.Request('https://google.com/search?q='+keyword,data = None,headers = {'User-Agent':'Mozilla/5.0;Chrome/35.0.1916.47'})
f = urllib.request.urlopen(req)
f=f.read().decode('utf-8')
soup = BeautifulSoup(f, 'html.parser')
urls = []
for link in soup.find_all('a'):
    if(link.get('href').startswith("/url?q=")):
        url = re.findall("[/url?q=]*(.+)",link.get('href'))[0]
        urls.append(urllib.parse.unquote(re.findall("(.*?)&",url)[0]))
    #urls.append(link.get('href'))
headings = []
for title in soup.find_all(['h3']) :
    headings.append(title.get_text())
    #print(title.get_text())
urls=urls[:-2]
dict ={"title":headings,"url":urls}
print(dict.keys())
for link in soup :
    print(dict['title'] ,':', dict['url'])
