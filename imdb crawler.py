#Web CrawLing
#1.send request and wait for response - urllib.request
#2. get the response and fetch the data - bs4(BeautifulSOup4) , LXML - library XML
import urllib.request as url
import bs4,lxml
path ="https://www.imdb.com/title/tt4154796/?ref_=nv_sr_srsg_0"
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
div = data.find('div',class_="title_wrapper")
h1 = div.find('h1')
print("Movie Name :",h1.text)
