from flask import Blueprint, render_template, current_app
from webapp.news.models import News
from webapp.weather import weather_by_city
from webapp.exchangerates import exchange_rates

blueprint = Blueprint('news',__name__)

@blueprint.route('/')
def index():
    title = "Домашняя страница"
    
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    exchangerates = exchange_rates("currency")

    news_list = News.query.order_by(News.published.desc()).all()

    return render_template('news/index.html', page_title=title, weather=weather, exchangerates=exchangerates, news_list=news_list)
