import os

from modules.text_analyser.base import UserLogin

ROOT = os.path.dirname(__file__)

app = None

ROUTE_MAPPING = [
    ('/user', UserLogin, 'user_login')
]

def register_urls():
    for url in ROUTE_MAPPING:
        app.add_url_rule(url[0], view_func=url[1].as_view(url[2]))