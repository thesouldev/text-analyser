from flask.views import MethodView
from models.odb import ndb
from models.text_analyser import DocumentEntity
from flask import render_template
import os
import json
from flask import request
from modules.text_analyser import base
import uuid


class DashboardView(MethodView):
    def get(self):
        return render_template('text_analyser/display.html')

    def post(self):
        request_data = json.loads(request.data)
        raw_data = request_data.get('data')
        id = uuid.uuid4().hex
        client = ndb.Client()
        with client.context():
            DocumentEntity.create(id, raw_data, namespace=base.MODULE)
            DocumentEntity.query().fetch()

        request_data['id'] = id

        return json.dumps(request_data), 201


class TextAnalyseView(MethodView):
    def get(self, id):
        client = ndb.Client()
        with client.context():
            query = DocumentEntity.get_by_id(id, namespace=base.MODULE)
            template_values = {}
            template_values['text'] = query.document

        return render_template('text_analyser/document_render.html', template_values=template_values)

    def post(self, id):
        return
