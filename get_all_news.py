from webapp import create_app
from webapp.overua_news import get_overua_news

app = create_app()
with app.app_context():
    get_overua_news()