from bs4 import BeautifulSoup
import requests

url = 'https://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content,"html.parser")

tweet = content.find('p',attrs={"class":"content"}).text
for tweet in content.findAll('p',attrs={"class":"content"}):
    print (tweet.text.encode('utf-8'))
