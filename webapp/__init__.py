from flask import Flask, render_template

from webapp.overua_news import get_overua_news
from webapp.weather import weather_by_city
from webapp.exchangerates import exchange_rates

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = "Домашняя страница"
        
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        exchangerates = exchange_rates("currency")

        news_list = get_overua_news()

        return render_template('index.html', page_title=title, weather=weather, exchangerates=exchangerates, news_list=news_list)
    
    return app