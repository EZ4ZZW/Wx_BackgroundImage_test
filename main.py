from urllib.request import Request, urlopen
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import urllib


def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=25) as f:
        data = f.read()
    return data.decode("utf-8")


def getImage(url, filename):
    image = urllib.request.urlopen(url)
    writer = image.read()
    File = open(filename + '.png', 'wb')
    File.write(writer)
    File.close

print("请输入微信公众号文章链接:")
url = input()
HtmlData = getHtml(url)
soup = BeautifulSoup(HtmlData, 'html.parser')
flag = False
metas = soup.find_all("meta")
ImageUrl = ""
ImageTitle = ""
for meta in metas:
    try:    
        pro = meta["property"]
        if pro == 'og:image':
            ImageUrl = meta['content']
        elif pro == 'og:title':
            ImageTitle = meta['content']
    except:
        continue

if ImageUrl == "":
    print("获取图片背景url失败，请重试")
    exit(0)    
try:
    getImage(ImageUrl, ImageTitle)
    print("背景图获取成功,文件名为: "+ImageTitle+'.png')
except:
    print("获取背景图失败QAQ")
