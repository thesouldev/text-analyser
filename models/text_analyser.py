from models import odb as ndb


class DocumentEntity(ndb.Model):
    document = ndb.StringProperty()

    @classmethod
    def create(cls, id, document, namespace='', to_put=True):
        entity = cls(id=str(id), document=document, namespace=namespace)
        if to_put:
            entity.put()
        return entity
