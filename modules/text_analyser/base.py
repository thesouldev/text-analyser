from flask.views import MethodView
from models.odb import ndb

from models.users import UserAccount

class UserLogin(MethodView):
    def get(self):
        breakpoint()
        client = ndb.Client()
        with client.context():
            UserAccount.create('sasidharanofficial@gmail.com')
            UserAccount.query().fetch()
        return 'sdfs'
