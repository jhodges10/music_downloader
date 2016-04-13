# Scrape youtube and download mp3's

import csv #Imports CSV's duh
import vidscraper #This is kind of redundant
import urllib #This submits the html for youtube
import urllib2 #This downloads the HTML and parses it
from bs4 import BeautifulSoup #This does the hard work on the HTML
import pafy #This does Youtube API stuff
import time

## You have to pip install youtube-dl as well for pafy to work right

#make the array for videos that gets filled by csv file read
videos = [] 

#read the CSV
with open('sample.csv') as csvfile:
    videograbber=csv.reader(csvfile)
    for row in videograbber:
        videos.append(row)


#simply a counter for iterating, shouldn't be necessary but is cuz I suck
y= 0

for each in videos:
    tempstring = ','.join(videos[y]) #convert list to string
    searchterm = tempstring #make nice variable name
    print searchterm #print out which one we're searching
    y+=1 #increase the position in the list
    query = urllib.quote(searchterm) #define the query string
    url = "https://www.youtube.com/results?search_query=" +query #generate url query
    response = urllib2.urlopen(url) #download the response
    html = response.read() #read that HTML wassup
    soup = BeautifulSoup(html) #make some soup out of that HTML
    # LETS LOOP SOME SHIT
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}): #goes through every line that it pulls out which is a youtube video link (including friggen playlists)
        url = 'https://www.youtube.com' + vid['href'] #generate the nice URL
        video = pafy.new(url) #turn that into something that our youtube API tool can use
        vid_title = video.title #grab the title for it
        #attempt to only grab ones that don't contain the wrong title
        if "remix" not in vid_title:
            video_audio = video.getbestaudio()
        elif "cover" not in vid_title:
            video_audio = video.getbestaudio()
        #deal with weird bug in pafy where it has problems with files already existing since the temp name is bad
        try:
            filename = video_audio.download(quiet=True)
        except:
            pass
        #somewhat redundant?
        print 'https://www.youtube.com' + vid['href']
        #add in a sleep to deal with that same issue
        time.sleep(1)
        
    
