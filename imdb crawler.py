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
a_sequence=data.find('div',class_='inline')
span = a_sequence.find('span')
print("story : ",span.text)
divList = data.findAll('div',class_='credit_summary_item')
a_List=[]
for i in divList:
    a = i.findAll("a")
    a_List.append(a)

director = a_List[0]
writer = a_List[1]
stars = a_List[2]

print("director : ",end='')
for i in director:
    print(i.text,end='  |  ')
print()
print("writer : ",end='')
for i in writer[0:len(writer)-1]:
    print(i.text,end='  |  ')
print()

print("stars : ",end='')
for i in stars[0:len(stars)-1]:
    print(i.text,end='  |  ')

print()
