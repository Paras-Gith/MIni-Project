import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
content = ""


def extract_news(url):
    print('Extracting Hacker news stories...')
    cnt = ''
    cnt +=('<br>HN Top Stories: </b>\n'+'<b>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('span', class_='titleline')):
        cnt += str(i+1) + ' :: ' + tag.text + "<br>\n"

    return cnt


    return(cnt)

cnt = extract_news('https://news.ycombinator.com/news')
content += cnt
content += ('<br>-------<br>')
content += ('<br><br>End of Message') 

#email sent
print('composing Email...')

SEVER = 'smtp.gmail.com'
PORT = 587
FROM = 'parasdummy3@gmail.com'
TO = ['nainwalparas5@gmail.com', 'chuphalravi8@gmail.com', 'rtcgunshot@gmail.com']
PASS = ''    #use google 'app password' main one will not work because of google policy
 
msg = MIMEMultipart()

msg['Subject'] = 'Top News HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = ", ".join(TO)

msg.attach(MIMEText(content, 'html'))

print('initiating server...')

server = smtplib.SMTP(SEVER, PORT)

server.set_debuglevel(1)
server.ehlo()
server.starttls()

server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent..')

server.quit()
