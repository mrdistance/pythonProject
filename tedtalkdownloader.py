import requests  # to get the content of ted talk page

from bs4 import BeautifulSoup  #web scraping

import re #regular expression pattern matching

import sys  #for argument parsing

#Exception handling      Allows terminal to take url argument  python3 filename.py urlargument
#if len(sys.argv) > 1:
   # url  = sys.argv[1]
#else:
    #sys.exit("Error: Please enter the TED Talk URL")


url = "https://www.ted.com/talks/sir_ken_robinson_do_schools_kill_creativity"

r = requests.get(url)  #pull the site content

print ("Download about to start")

soup = BeautifulSoup(r.content,"html.parser")  #just the content from site

for val in soup.findAll("script"):
    if(re.search("videoData", str(val))) is not None:  #The tag has changed since tutorial dont know how to find video mp4
        result = str(val)

result_mp4 = re.search("(?P<url>https?://[^\s]+)(mp4)", result).group("url")  #get just the mp4s from the content

mp4_url = result_mp4.split('"')[0]  #get the first mp4 link (lowest quality)

print("Downloading video from ....." + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]   #create dynamic filename based on video name

print("Storing video in ...."+ file_name)

r = requests.get(mp4_url)   #pull url for mp4 from site

with open(file_name, 'wb') as f:    #write the mp4 to the file
    f.write(r.content)