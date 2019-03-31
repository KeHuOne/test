import requests

def exchange_rates(currency):
    ex_url = "https://www.cbr-xml-daily.ru/daily_json.js"

    try:
        result = requests.get(ex_url)
        result.raise_for_status()
        exrates = result.json()
        if 'Valute' in exrates:
            if 'USD' in exrates ['Valute']:
                try:
                    return exrates['Valute']['USD']
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    return False

if __name__ == "__main__":
    print(exchange_rates("currency"))