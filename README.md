# telegram-support-bot
Easy way to use Telegram bot to hide your identity. Useful for support, anonymous channel management. Free clone of Livegram Bot. 

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## How bot works:



## .env variables

You need to specify these env variables to run this bot. If you run it locally, you can also write them in `.env` text file.

``` bash
TELEGRAM_TOKEN=  # your bot's token

# optional params
HEROKU_APP_NAME=  # name of your Heroku app for webhook setup

```

## Run bot locally

First, you need to install all dependencies:

```bash
pip install -r requirements.txt
```

Then you can run the bot. Don't forget to create `.env` file in the root folder with all required params (read above).

``` bash
python main.py
```
