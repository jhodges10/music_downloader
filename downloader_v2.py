# Bulk MP4 Downloader
# Written by Jerfrey and Huff
# In progress
## You have to pip install youtube-dl, pafy, and beautifulsoup

import csv #Imports CSV's duh
import urllib #This submits the html for youtube
import urllib2 #This downloads the HTML and parses it
from bs4 import BeautifulSoup #This does the hard work on the HTML
import pafy #This does Youtube API stuff
#import eyeD3 #This does ID3 tags for mp3s
import time

def get_urls(soup):
    for link in soup.find_all('a'):
        templink=link.get('href')
        if templink.startswith('/watch'):
            return templink
            break
    
def exceptions_in_string(exceptions, song_string, searchterm):
    tempvar=0
    for s in exceptions:
        if s in vid_title:
            if s in searchterm:
                print "2 ifs ",s
                continue
            tempvar=1
            break
    return tempvar

def find_url(songtitle):
    pagevar=1
    temp=None
    print "We are searching for: " +songtitle #print out which one we're searching
    while temp==None:
        pagecontrol="&page="+str(pagevar)
        query = urllib.quote(songtitle) #define the query string
        url = "https://www.youtube.com/results?search_query=" +query+pagecontrol #generate url query
        response = urllib2.urlopen(url) #open the URL
        html_page = response.read() #read that HTML wassup
        soup = BeautifulSoup(html_page,"lxml") #make some soup out of that HTML
        temp=get_urls(soup)
        pagevar=pagevar+1
    return temp

def download_song(answer):
    url="https://www.youtube.com"+answer
    video=pafy.new(url)
    best=video.getbest(preftype="mp4")
    filename=best.download(quiet=True)

#eventually add a document to add more exceptions which will import into this array
exceptions= ["cover","live","remix","version", "edit", "Cover", "Live", "Remix", "Version", "Edit", "COVER", "LIVE", "REMIX", "VERSION", "EDIT"]

songlist = []
y=0

with open('sample.csv') as csvfile: #import song lists
    songs=csv.reader(csvfile)
    for row in songs:
        songlist.append(row)
        print row

for each in songlist: #for every song in the songlist, download the mp4
    songtitle = ",".join(songlist[y])
    answer=find_url(songtitle)
    download_song(answer)
    print answer
    y=y+1
    
