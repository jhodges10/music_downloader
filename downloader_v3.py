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

#Song class
class Song:
    
    def __init__(self, title, artist, album):
      self.title = title
      self.artist = artist
      self.album = album

    def displaySong(self):
      print "Title : ", self.title, ", Artist: ", self.artist, ", Album: ", self.album

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

#other functions
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
    try:
        best=video.getbestaudio(preftype="m4a")
        filename=best.download(filepath="../downloads/",quiet=True)
    except:
        best=video.getbest(preftype="mp4")
        filename=best.download(filepath="../downloads/",quiet=True)
        
#eventually add a document to add more exceptions which will import into this array
exceptionlist = []
songlist = []
y=0

with open('exceptions.csv') as exceptionfile:
    exceptions=csv.reader(exceptionfile)
    for row in exceptions:
        exceptionlist.append(row)
        
with open('songfile.csv') as csvfile: #import song lists
    fieldnames=['songname','songartist','songalbum']
    reader=csv.DictReader(csvfile, fieldnames=fieldnames)
    for row in reader:
        x=Song(row['songname'],row['songartist'],row['songalbum'])
        songlist.append(x)
        
for each in songlist: #for every song in the songlist, download the mp4
    songtitle = each.getTitle()
    songartist = each.getArtist()
    songsearch = songtitle+" "+songartist
    answer=find_url(songsearch)
    download_song(answer)
    print answer
    y=y+1
