import requests  #to pull data from a site
import schedule  #to schedule things to run at certain intervals within the program


from bs4 import BeautifulSoup       #

import smtplib   #for emails

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()           #to have each email on different days have different title

content = ''

#get the news stories from a website
def extract_news(url):
    print ('Getting website url')
    #print('Extracting hacker new stories...')
    cnt = ''
    #cnt += ('<b>HN Top Stories:</b>\n'+'<br>' + '-' *50+'<br>')
    cnt += ('<b> God Loves You! </b>\n' + '<br' + '-' *50 + '<br><br><br>')

    #get the page
    response = requests.get(url)
    content = response.content

    #get the html content
    soup = BeautifulSoup(content, 'html.parser')
    #look for the correct attributes in the inspect html code that you want to extract
    for i, tag in enumerate(soup.find_all('div', attrs={'class':'layout_layout layout_inner layout_normal'})):
        cnt += (tag.text + "<br><br>")
    return cnt
    #for i, tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        #cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    #return cnt



#cnt = extract_news('https://news.ycombinator.com/')
cnt = extract_news('https://www.churchofjesuschrist.org/comeuntochrist/believe/god/gods-love')
content += cnt
content += ('<br>------<br>')
content +=('<br><br>End of Message')

#print(content)

#lets send the email
print('Composing Email...')
emailList = 'callsluvcredit@gmail.com'
#update email address
SERVER = 'smtp.gmail.com'  #your smtp server
PORT = 587 # your port number
FROM = 'callmejoshcall@gmail.com' #your email id
TO = emailList  #your email ids can be a list as a string? or single email
PASS = '********' #your email id's password



msg = MIMEMultipart()


#create email structure
#dynamic changing subject title based on datetime
#msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['Subject'] = 'Always Remember God\'s Love' + ' ' + str(now.day) + '-'+ str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

#add the content we scraped in the format we want
msg.attach(MIMEText(content, 'html'))


#Authentication
server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO.split(","), msg.as_string())

print('Email Sent...')

server.quit()