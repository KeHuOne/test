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

def get_amd_am4():
    html = get_html("https://market.yandex.ru/catalog--protsessory-cpu/55330/list?hid=91019&glfilter=" \
                "5038955%3A14744384&onstock=1&local-offers-first=0")
    if html:
        soup = BeautifulSoup(html, 'lxml')
        all_amd_am4 = soup.find_all('div', class_='n-snippet-card2')
        result = []
        for div in all_amd_am4:
            beginning = div.find('div', class_='n-snippet-card2__title')
            
            product = beginning.find('a', class_='link').get('title')
            
            url = beginning.find('a', class_='link').get('href')
            url = 'https://market.yandex.ru' + url
            
            images = div.find('div', class_='n-snippet-card2__part').find('a', class_='n-snippet-card2__image').find('img', class_='image').get('src')
            image = 'https:' + images
            
            price = div.find('div', class_='n-snippet-card2__main-price-wrapper').find('div', class_='price').get_text()
            price = price.replace("\xa0₽", "")
            price = price.replace(" ", "")

            information = div.find('div', class_='n-snippet-card2__content').find('ul').find('li').text
            
            
            result.append({
                "name" : product,
                "url" : url,
                "image" : image,
                "price" : price,
                "information" : information
            })
        return result
    return False

print(get_amd_am4())
