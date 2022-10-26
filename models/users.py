from models import odb as ndb
import uuid

class UserAccount(ndb.Model):
    user_id = ndb.StringProperty()
    
    @classmethod
    def create(cls, email, to_put=True):
        entity = cls(id=email, user_id=uuid.uuid4().hex, namespace='')
        if to_put: 
            entity.put()
        return entity