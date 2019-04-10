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

def get_asus_1151v2():
    html = get_html("https://market.yandex.ru/catalog--materinskie-platy/55323/list?hid=91020&glfilter=4923171%3A15177871&glfilter=4923184%3A12108231&glfilter=7893318%3A152863&onstock=1&local-offers-first=0")
    if html:
        soup = BeautifulSoup(html, 'lxml')
        all_asus_1151v2 = soup.find_all('div', class_='n-snippet-card2')
        result = []
        for div in all_asus_1151v2:
            
            product = div.find('div', class_='n-snippet-card2__title').find('a', class_='link').get('title')
            
            url = div.find('div', class_='n-snippet-card2__title').find('a', class_='link').get('href')
            url = 'https://market.yandex.ru' + url
            
            images = div.find('div', class_='n-snippet-card2__part').find('a', class_='n-snippet-card2__image').find('img', class_='image').get('src')
            image = 'https:' + images
            
            price = div.find('div', class_='n-snippet-card2__main-price-wrapper').find('div', class_='price').get_text()
            price = price.replace("\xa0₽", "")
            price = price.replace(" ", "")

            socket = div.find('div', class_='n-snippet-card2__content').find('ul').find_all('li')[1].text

            chipset = div.find('div', class_='n-snippet-card2__content').find('ul').find_all('li')[2].text
            
            
            result.append({
                "name" : product,
                "url" : url,
                "image" : image,
                "price" : price,
                "socket" : socket,
                "chipset" : chipset
            })
        return result
    return False

print(get_asus_1151v2())