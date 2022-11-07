from flask.views import MethodView
from models.odb import ndb
from flask import render_template
import os

class DashboardView(MethodView):
    def get(self):
        return render_template('text_analyser/display.html')
