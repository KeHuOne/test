import os
import requests
import settings
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False

def get_all_item_info(html):
    if html:
        soup = BeautifulSoup(html, 'lxml')
        all_product = soup.find_all('div', class_='n-snippet-card2')
        result = []
        for div in all_product:
            beginning = div.find('div', class_='n-snippet-card2__title')
            
            product = beginning.find('a', class_='link').get('title')
            
            url = beginning.find('a', class_='link').get('href')
            url = 'https://market.yandex.ru' + url
            
            images = div.find('div', class_='n-snippet-card2__part').find('a', class_='n-snippet-card2__image').find('img', class_='image').get('src')
            image = 'https:' + images
            
            price = div.find('div', class_='n-snippet-card2__main-price-wrapper').find('div', class_='price').get_text()
            price = price.replace("\xa0₽", "")
            price = price.replace(" ", "")

            information = div.find('div', class_='n-snippet-card2__content').find('ul').find_all('li')
           
            result.append({
                "name" : product,
                "url" : url,
                "image" : image,
                "price" : price,
                "information" : information
            })
        
    
    

        with open (os.path.abspath('.\\allinfo.txt'), 'w', encoding='utf8') as file:
            for i in result:
                i = str(i)
                file.write(i + '\n')

if __name__ == "__main__":
    for url in settings.ALL_URL:
        html = get_html(url)
    if html:
        get_all_item_info(html)