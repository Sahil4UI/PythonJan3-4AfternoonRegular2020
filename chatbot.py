import os,glob,random,webbrowser
from datetime import datetime as dt
helloIntent = ["hi","hello","hey","wassup","hey buddy"]
dateIntent = ["date","show me date","date please","whats the date"]
timeIntent = ["time","show me time","time please","whats the time"]
msg = input("Enter Message : ")
msg = msg.lower()
musicIntent = ["music","play music"]

if msg in helloIntent:
    print("hello Sir....")
elif msg in dateIntent:
    datetime = dt.now()
    date = datetime.strftime("%d-%m-%y,%a")
    print(date)
elif msg in timeIntent:
    datetime = dt.now()
    time = datetime.strftime("%I:%M:%S,%p")
    print(time)
elif msg in musicIntent:
    os.chdir(r"C:\Users\sahil\Downloads")#raw string
    #list=os.listdir()
    song = glob.glob("*.mp3")
    os.startfile(random.choice(song))
elif msg.startswith("open"):
    name=msg.split()[-1]+".com"
    webbrowser.open(name)
