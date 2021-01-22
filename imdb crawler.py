'''
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
'''


#Web CrawLing
#1.send request and wait for response - urllib.request
#2. get the response and fetch the data - bs4(BeautifulSOup4) , LXML - library XML
import urllib.request as url
import bs4,lxml
import webbrowser
movieName = input("Enter Movie Name =>").replace(" ","+")
path ="https://www.imdb.com/find?q="+movieName
response = url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')
result = data.find('td',class_="result_text")

link ='https://www.imdb.com'+result.find('a')['href'] 

response = url.urlopen(link)

data = bs4.BeautifulSoup(response,'lxml')
div = data.find('div',class_="title_wrapper")
h1 = div.find('h1')
print("Movie Name :",h1.text)
rating = data.find('span',itemprop="ratingValue")
print("Rating : ",rating.text,'/10')
a_group = data.find('div',class_='subtext')
a_list = a_group.findAll('a')
print("Genre : ",end="")
for i in a_list[0:len(a_list)-1]:
    i = i.text
    print(i,end="  |  ")
print('\nDate of Release : ',a_list[-1].text)
