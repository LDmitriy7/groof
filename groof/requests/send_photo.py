from .base import ReplyMarkupT
from ..api import request
from ..context import ctx
from ..objects import MessageEntity, Message, InputFile
from ..objects.tg_methods import SendPhoto


def send_photo(
        photo: InputFile | str,
        reply_markup: ReplyMarkupT = None,
        caption: str = None,

        chat_id: int | str = None,
        parse_mode: str = None,
        disable_notification: bool = None,
        protect_content: bool = None,

        caption_entities: list[MessageEntity] = None,
        reply_to_message_id: int = None,
        allow_sending_without_reply: bool = None,
) -> Message:
    return request(
        SendPhoto,
        locals(),
        chat_id=ctx.chat_id,
        parse_mode=ctx.parse_mode,
        disable_notification=ctx.disable_notification,
        protect_content=ctx.protect_content,
    )
