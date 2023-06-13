from ..models import db
from bson.objectid import ObjectId
from typing import Optional


class User():
    table = db.user

    name = ''
    user_id = None

    @property
    def _insert_doc(self):
        doc = self.full_doc
        doc.pop('_id')
        return doc

    @property
    def full_doc(self):
        return {"_id": str(self.user_id), "name": self.name}

    def _insert(self) -> str:
        inserted_id = self.table.insert_one(self._insert_doc).inserted_id
        self.user_id = inserted_id
        return inserted_id

    @classmethod
    def get_by_name(cls, name: str) -> Optional['User']:
        user_dict = cls.table.find_one({"name": name})
        if user_dict:
            return cls.from_dict(user_dict)
        else:
            return None

    @classmethod
    def get_by_id(cls, user_id: str) -> Optional['User']:
        user_dict = cls.table.find_one({"_id": ObjectId(user_id)})
        if user_dict:
            return cls.from_dict(user_dict)
        else:
            return None

    @classmethod
    def from_dict(cls, user_dict: dict) -> 'User':
        user = User()
        user.user_id = ObjectId(user_dict["_id"])
        user.name = user_dict["name"]
        return user

    @classmethod
    def from_name(cls, name) -> 'User':
        user = cls.get_by_name(name)
        if not user:
            user = User()
            user.name = name
            user._insert()
        return user
