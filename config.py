import os

from modules.text_analyser.base import UserLogin
from modules.text_analyser.views import DashboardView, TextAnalyseView

ROOT = os.path.dirname(__file__)

app = None

ROUTE_MAPPING = [
    ('/user', UserLogin, 'user_login'),
    ('/', DashboardView, 'dashboard'),
    ('/analyse/<id>', TextAnalyseView, 'text_analyse')
]


def register_urls():
    for url in ROUTE_MAPPING:
        app.add_url_rule(url[0], view_func=url[1].as_view(url[2]))
