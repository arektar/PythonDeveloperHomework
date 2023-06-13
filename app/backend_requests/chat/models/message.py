from typing import Optional
from ..models import db
from bson.objectid import ObjectId
from datetime import datetime
from .user import User
from .chat import Chat


class Message():
    mess_id: Optional['str'] = None
    chat: Optional['Chat'] = None
    author: Optional['str'] = None
    text: str = ''
    datetime: Optional['datetime'] = None
    table = db.message

    """def __init__(self, username, author, text):
        user = User(username)
        self.chat = Chat.get_by_user_id(user.user_id)
        self.author = author
        self.text = text
        self.datetime = datetime.utcnow()

        self.insert()"""

    @property
    def _insert_doc(self):
        doc = self.full_doc
        doc.pop('_id')
        doc["chat_id"] = ObjectId(doc["chat_id"])
        return doc

    @property
    def full_doc(self) -> dict:
        return {
            "chat_id": str(self.chat.chat_id),
            "_id": str(self.mess_id),
            "author": self.author,
            "text": self.text,
            "datetime": self.datetime,
        }

    def _insert(self) -> str:
        inserted_id = self.table.insert_one(self._insert_doc).inserted_id
        self.mess_id = inserted_id
        return inserted_id

    @classmethod
    def get_by_chat_id(cls, chat_id: str) -> Optional[list['Message']]:
        messages = cls.table.find({"chat_id": ObjectId(chat_id)})
        if messages:
            return [cls.from_dict(mess) for mess in messages]
        else:
            return None

    @classmethod
    def get_by_id(cls, mess_id: str) -> Optional['Message']:
        mess_dict = cls.table.find_one({"_id": ObjectId(mess_id)})
        if mess_dict:
            return cls.from_dict(mess_dict)
        else:
            return None

    @classmethod
    def from_dict(cls, mess_dict: dict) -> 'Message':
        mess = Message()
        mess.mess_id = ObjectId(mess_dict["_id"])
        mess.chat = Chat.get_by_id(mess_dict["chat_id"])
        mess.author = mess_dict["author"]
        mess.text = mess_dict["text"]
        mess.datetime = mess_dict["datetime"]
        return mess

    @classmethod
    def new(cls, user_id, author, text) -> 'Message':
        mess = Message()
        user = User.get_by_id(user_id)
        mess.chat = Chat.get_by_user_id(user.user_id)
        mess.author = author
        mess.text = text
        mess.datetime = datetime.now()

        mess._insert()
        return mess

    def get_to_model_format(self):
        return {"agent": self.author, "message": self.text}
