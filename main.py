from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

from handlers import setup_dispatcher, start, echo
from settings import TELEGRAM_TOKEN, HEROKU_APP_NAME, PORT

# Setup bot handlers
updater = Updater(TELEGRAM_TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# on different commands - answer in Telegram
dispatcher.add_handler(CommandHandler("start", start))

# on non command i.e message - echo the message on Telegram
dispatcher.add_handler(MessageHandler(~Filters.command, echo))

# Run bot
if HEROKU_APP_NAME is None:  # pooling mode
    print("Can't detect 'HEROKU_APP_NAME' env. Running bot in pooling mode.")
    print("Note: this is not a great way to deploy the bot in Heroku.")

    updater.start_polling()
    updater.idle()

else:  # webhook mode
    print(f"Running bot in webhook mode. Make sure that this url is correct: https://{HEROKU_APP_NAME}.herokuapp.com/")
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TELEGRAM_TOKEN,
        webhook_url=f"https://{HEROKU_APP_NAME}.herokuapp.com/{TELEGRAM_TOKEN}"
    )

    updater.idle()
