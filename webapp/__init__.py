from flask import Flask, render_template


from webapp.weather import weather_by_city
from webapp.exchangerates import exchange_rates
from webapp.model import db, News

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Домашняя страница"
        
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        exchangerates = exchange_rates("currency")

        news_list = News.query.order_by(News.published.desc()).all()

        return render_template('index.html', page_title=title, weather=weather, exchangerates=exchangerates, news_list=news_list)
    
    return app