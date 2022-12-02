from models import odb as ndb


class DocumentEntity(ndb.Model):
    document = ndb.StringProperty()
    is_sentiment_analysis = ndb.BooleanProperty(default=False)
    is_context_analysis = ndb.BooleanProperty(default=False)
    is_toxic_analysis = ndb.BooleanProperty(default=False)

    @classmethod
    def create(
        cls,
        id,
        document,
        is_sentiment_analysis=False,
        is_toxic_analysis=False,
        is_context_analysis=False,
        namespace="",
        to_put=True,
    ):
        entity = cls(
            id=str(id),
            document=document,
            is_sentiment_analysis=is_sentiment_analysis,
            is_context_analysis=is_context_analysis,
            is_toxic_analysis=is_toxic_analysis,
            namespace=namespace,
        )
        if to_put:
            entity.put()
        return entity
