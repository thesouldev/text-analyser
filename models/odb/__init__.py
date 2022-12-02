from . import ndb

try:
    _ = basestring
except:
    basestring = str

Key = ndb.Key

StringProperty = ndb.StringProperty
BooleanProperty = ndb.BooleanProperty


class Model(ndb.Model):
    @classmethod
    def kind(cls):
        return cls._get_kind()

    @classmethod
    def properties(cls):
        return cls()._properties

    @classmethod
    def _get_final_namespace(cls, namespace):
        return namespace

    @classmethod
    def generate_cache_key(cls, id_):
        return cls.__name__ + ":" + str(id_)

    @classmethod
    def get_by_id(cls, id_, namespace=None):

        value = super(Model, cls).get_by_id(
            id_, namespace=cls._get_final_namespace(namespace)
        )

        return value

    @classmethod
    def get_by_key_name(cls, id_, namespace=None):

        namespace = cls._get_final_namespace(namespace)
        if isinstance(id_, list):
            if isinstance(id_[0], basestring):
                return ndb.get_multi([Key(cls, k, namespace=namespace) for k in id_])
            if isinstance(id_[0], Key):
                return ndb.get_multi(id_)

        return cls.get_by_id(id_, namespace=namespace)

    @classmethod
    def get(cls, key):
        value = key.get()
        return value

    @classmethod
    def query(cls, *args, **kwargs):
        namespace = kwargs.get("namespace")
        kwargs["namespace"] = cls._get_final_namespace(namespace)
        return super(Model, cls).query(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        assert not args

        if "key_name" in kwargs:
            if "id" in kwargs:
                raise ValueError("Cannot use both `key_name` and `id`")
            kwargs["id"] = kwargs.pop("key_name")

        if "parent" in kwargs:
            parent = kwargs.get("parent")
            if isinstance(parent, self):

                kwargs["parent"] = parent.key

        namespace = kwargs.get("namespace")
        kwargs["namespace"] = self._get_final_namespace(namespace)

        return super(Model, self).__init__(*args, **kwargs)

    def put(self):
        result = super(Model, self).put()
        return result

    @classmethod
    def delete_by_key(cls, key, **kwargs):
        return key.delete(**kwargs)

    def delete(self, key_delete_kwargs=None):
        kwargs = {}
        if key_delete_kwargs:
            kwargs = key_delete_kwargs
        return self.delete_by_key(self.key.id(), **kwargs)


class Query(ndb.Query):
    def __init__(self, *args, **kwargs):
        super(Query, self).__init__(*args, **kwargs)
