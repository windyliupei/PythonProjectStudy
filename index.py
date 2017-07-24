#coding=utf-8

import urllib
import urllib.request
from bs4 import BeautifulSoup

x=0;
url = 'http://www.dbmeinv.com/?pager_offset=1'

def crawl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    req = urllib.request.Request(url,headers=headers)
    page = urllib.request.urlopen(req,timeout=20)
    contents = page.read()
    #print(contents)
    soup = BeautifulSoup(contents,'html.parser')
    my_girl = soup.find_all('img')
    for girl in my_girl:
        link = girl.get('src')
        print(link)
        global x
        urllib.request.urlretrieve(link,'image\\%s.jpg'%x)
        x+=1
        print("Downloading %s"%x)

#crawl(url)

for page in range(1,11):
    url = 'http://www.dbmeinv.com/?pager_offset=%s'%page
    crawl(url)