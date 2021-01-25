import urllib.request as url
import bs4

print('''
Press 1 for Entertainment
Press 2 for politics
Press 3 for sports''')
news_choice = int(input("Enter Choice : "))
path = 'https://www.foxnews.com/'
if news_choice==1:
    path =path+'entertainment'
    response = url.urlopen(path)
    data = bs4.BeautifulSoup(response,'lxml')
    h4List = data.findAll('h4',class_="title")    
    h4List = h4List[0:10]
    for i  in range(len(h4List)):
        print(f"{i+1}-->{h4List[i].text}\n")
        
