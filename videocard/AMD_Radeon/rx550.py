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

def get_rx_550():
    html = get_html("https://market.yandex.ru/catalog--videokarty/55314/list?hid=91031&glfilter=4878792%3A14905759&onstock=1&local-offers-first=0&how=aprice")
    if html:
        soup = BeautifulSoup(html, 'lxml')
        all_rx_550 = soup.find_all('div', class_='n-snippet-card2')
        result = []
        for div in all_rx_550:
            
            product = div.find('div', class_='n-snippet-card2__title').find('a', class_='link').get('title')
            
            url = div.find('div', class_='n-snippet-card2__title').find('a', class_='link').get('href')
            url = 'https://market.yandex.ru' + url
            
            images = div.find('div', class_='n-snippet-card2__part').find('a', class_='n-snippet-card2__image').find('img', class_='image').get('src')
            image = 'https:' + images
            
            price = div.find('div', class_='n-snippet-card2__main-price-wrapper').find('div', class_='price').get_text()
            price = price.replace("\xa0₽", "")
            price = price.replace(" ", "")
            
            result.append({
                "name" : product,
                "url" : url,
                "image" : image,
                "price" : price
            })
        return result
    return False

print(get_rx_550())