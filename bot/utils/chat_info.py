from aiogram.types import Message, CallbackQuery


class ChatInfo:
    """
    Метод для получения информации о чате:
    `user_id`, `username`, `chat_id`, `msg_id`
    """
    def __init__(self, msg: CallbackQuery | Message) -> None:
        user = msg.from_user
        self.user_id = str(user.id)
        self.username = str(user.username)
        self.full_name = (str(user.first_name) 
                     + (' ' if user.last_name else '')
                     + str(user.last_name if user.last_name else ''))
        if isinstance(msg, CallbackQuery):
            msg = msg.message
        self.chat_id = str(msg.chat.id)
        self.msg_id = str(msg.message_id)
    
    def __call__(self) -> dict:
        data = {
            "tg_user_id": self.user_id,
            "tg_chat_id": self.chat_id,
            "tg_username": self.username,
            "full_name": self.full_name,
        }
        return data
    
    def __repr__(self) -> str:
        return f"{self.user_id} - {self.username} - {self.full_name}"