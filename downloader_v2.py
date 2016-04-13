# Scrape youtube and download mp3's

import csv
import vidscraper
import urllib
import urllib2
from bs4 import BeautifulSoup
import pafy
import time

videos = []

with open('stamp.csv') as csvfile:
    videograbber=csv.reader(csvfile)
    for row in videograbber:
        videos.append(row)



y= 0

for each in videos:
    tempstring = ','.join(videos[y])    
    searchterm = tempstring
    print searchterm
    y+=1
    query = urllib.quote(searchterm)
    url = "https://www.youtube.com/results?search_query=" +query
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        url = 'https://www.youtube.com' + vid['href']
        video = pafy.new(url)
        vid_title = video.title
        if "remix" not in vid_title:
            video_audio = video.getbestaudio()
        elif "cover" not in vid_title:
            video_audio = video.getbestaudio()
        try:
            filename = video_audio.download(quiet=True)
        except:
            pass
        print 'https://www.youtube.com' + vid['href']
        time.sleep(1)
        
    
