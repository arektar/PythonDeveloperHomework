from flask import session
from flask_socketio import emit, join_room, leave_room
from app import socketio
from typing import Optional
from app.backend_requests.chat.models.message import Message
from app.backend_requests.chat.models.chat import Chat
from app import lang_model
from time import sleep


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room"""
    user = session.get('user')

    if user is not None:
        chat_dict = Chat.from_user_id(user["_id"]).full_doc
        session["chat"] = chat_dict

        room = chat_dict["_id"]
        join_room(room)

        restore_messages(chat_dict["_id"], room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message."""
    room = session.get('chat')["_id"]
    user = session.get('user')
    if room:
        mess = Message.new(user['_id'], user["name"], message['msg'])
        send_to_chat(mess, room)

        answer = send_to_model(mess)
        mess = Message.new(user['_id'], "robot", answer)
        send_to_chat(mess, room)


def send_to_model(mess: Message) -> str:
    messages = Message.get_by_chat_id(mess.chat.chat_id)
    messages = [msg.get_to_model_format() for msg in messages]
    answer = lang_model.chat(messages)
    return answer


def send_to_chat(mess: Message, room:str):
    emit('message', {'msg': mess.author + ':' + mess.text}, room=room)


def restore_messages(chat_id: str, room_id: str):
    messages = Message.get_by_chat_id(chat_id)
    for mess in messages:
        send_to_chat(mess, room_id)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room."""
    room = session.get('chat')["_id"]
    leave_room(room)
    session["chat"] = None
