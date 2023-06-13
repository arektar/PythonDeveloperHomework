from ..models import db
from bson.objectid import ObjectId
from typing import Optional
from .user import User


class Chat():
    table = db.chat

    chat_id: Optional['str'] = None
    user: Optional['User'] = None

    @property
    def _insert_doc(self):
        doc = self.full_doc
        doc.pop('_id')
        doc["user_id"] = ObjectId(doc["user_id"])
        return doc

    @property
    def full_doc(self) -> dict:
        return {"_id": str(self.chat_id), "user_id": str(self.user.user_id)}

    def _insert(self) -> str:
        inserted_id = self.table.insert_one(self._insert_doc).inserted_id
        self.chat_id = inserted_id
        return inserted_id

    @classmethod
    def get_by_user_id(cls, user_id: str) -> Optional['Chat']:
        chat_dict = cls.table.find_one({"user_id": ObjectId(user_id)})
        if chat_dict:
            return cls.from_dict(chat_dict)
        else:
            return None

    @classmethod
    def get_by_id(cls, chat_id: str) -> Optional['Chat']:
        chat_dict = cls.table.find_one({"_id": ObjectId(chat_id)})
        if chat_dict:
            return cls.from_dict(chat_dict)
        else:
            return None

    @classmethod
    def from_dict(cls, chat_dict: dict) -> 'Chat':
        chat = Chat()
        chat.chat_id = ObjectId(chat_dict["_id"])
        chat.user = User.get_by_id(chat_dict["user_id"])
        return chat

    @classmethod
    def from_user_id(cls, user_id: str) -> 'Chat':
        chat = cls.get_by_user_id(user_id)
        if not chat:
            chat = Chat()
            chat.user = User.get_by_id(user_id)
            chat._insert()
        return chat
