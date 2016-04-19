#LOL ITS A MESS BUT IT KIND OF WORKS I GUESS i need to sleep on it lol. sigh python.
# Scrape youtube and download mp3's

import csv #Imports CSV's duh
import vidscraper #This is kind of redundant
import urllib #This submits the html for youtube
import urllib2 #This downloads the HTML and parses it
from bs4 import BeautifulSoup #This does the hard work on the HTML
import pafy #This does Youtube API stuff
#import eyeD3 #This does ID3 tags for mp3s
import time


## You have to pip install youtube-dl as well for pafy to work right

#make the array for videos that gets filled by csv file read
videos = [] 

#read the CSV
with open('sample.csv') as csvfile:
    videograbber=csv.reader(csvfile)
    for row in videograbber:
        videos.append(row)

def exceptions_in_string(exceptions, song_string, searchterm):
    tempvar=0
    for s in exceptions:
        if s in vid_title:
            if s in searchterm:
                continue
            tempvar=1
            break
    return tempvar

#simply a counter for iterating, shouldn't be necessary but is cuz I suck
y= 0
print "y= ",y
for each in videos:
    soup=" "
    html=" "
    response=" "
    url=" "
    searchterm = ','.join(videos[y]) #convert list to string
    print "Searchterm= ", searchterm
    print "This is what we're looking for: " +searchterm #print out which one we're searching
    query = urllib.quote(searchterm) #define the query string
    url = "https://www.youtube.com/results?search_query=" +query #generate url query
    response = urllib2.urlopen(url) #download the response
    html = response.read() #read that HTML wassup
    soup = BeautifulSoup(html,"lxml") #make some soup out of that HTML
    # LETS LOOP SOME SHIT
    #count=0
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}): #goes through every line that it pulls out which is a youtube video link (including friggen playlists)
    #while count==0:
        vid_title=" "
        url=" "
        video=" "
        video_audio=" "
        filename=" "
        url = 'https://www.youtube.com' + vid['href'] #generate the nice URL
        video = pafy.new(url) #turn that into something that our youtube API tool can use
        vid_title = video.title #grab the title for it
        print "vid_title= ",vid_title
        video_audio=video.getbestaudio()
        #attempt to only grab ones that don't contain the wrong title
        evar=exceptions_in_string(exceptions,vid_title, searchterm)
        if evar==1:
            continue
        print vid_title
        filename=video_audio.download(quiet=True)
        filename = video_audio.download(filepath="../downloads/", quiet=True)
        time.sleep(10)
        print 'https://www.youtube.com' + vid['href']  #somewhat redundant?
        #time.sleep(5) #add in a sleep to deal with that same issue
        #count=1
        #print "count", count
        y+=1 #increase the position in the list
        break
