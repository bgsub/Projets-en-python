import requests 
from datetime import datetime
from bs4 import BeautifulSoup


url = "https://ici.radio-canada.ca/"
page = requests.get("https://ici.radio-canada.ca/")
soup = BeautifulSoup(page.content, 'html.parser')
articles = soup.find_all("article", class_ = "sc-ya1rc9-0 crbnVK card info")
recent_news_radio_canada = {}
today = datetime.now().strftime("%d_%m_%Y_%Hh_%Mmins")
file_name = "Articles_du_" + today + ".txt"
#adding articles name and link in a dictionary
for article in articles:
    link = article.div.a.get("href")
    title = article.div.a.text.strip()
    recent_news_radio_canada[title] = link

#create a file and write title and link of each article
#param : the file name 
#return:  nothing
def write_titles(name_of_the_file):
    file = open(name_of_the_file,"w",encoding='utf-8')
    for title,link in recent_news_radio_canada.items(): 
        file.write("\n" "nom de l'article: " + title + "      " + "lien : " + url+link + "\n")
    file.close()
    if file: 
        print("\n"+ name_of_the_file+ " a été créé")
    return None


write_titles(file_name)