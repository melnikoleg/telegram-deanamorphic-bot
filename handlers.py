from io import BytesIO

import PIL
from PIL import Image
import requests

from telegram import Update, ForceReply
from telegram.ext import CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def echo(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id

    try:
        ratio = float(update.message.caption)
        file_name = update.message.document.file_name
        file = context.bot.getFile(update.message.document.file_id)
        response = requests.get(file.file_path, allow_redirects=True)
        image = Image.open(BytesIO(response.content))

        image = image.resize((image.size[0], int(image.size[1] / ratio)), PIL.Image.LANCZOS)
        image_file = BytesIO()
        image_file.name = file_name
        image.save(image_file, 'JPEG')
        image_file.seek(0)
        context.bot.send_document(chat_id, image_file)

    except:
        context.bot.send_message(chat_id, "Hey, send the photo with aspect ratio ex: 1.33, 1.5")


def setup_dispatcher(dp):
    dp.add_handler(CommandHandler('start', start))

    return dp
