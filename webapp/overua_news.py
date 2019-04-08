from datetime import datetime

import requests
from bs4 import BeautifulSoup

from webapp.db import db, News
from webapp.news.models import News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_overua_news():
    html = get_html("https://www.overclockers.ua/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='mainpage_block_left').find('ul').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            url = "https://www.overclockers.ua" + url
            published = datetime.now()
            save_news(title, url, published)

def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()