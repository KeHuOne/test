import requests
from bs4 import BeautifulSoup

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
            result_news.append({
                "title": title,
                "url": url
            })
        return result_news
    return False
