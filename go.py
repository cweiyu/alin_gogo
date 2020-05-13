# Channel Access Token
line_bot_api = "5TG59krKsc34A0BeWhNa3bgOTLuWNaM6rrw2aieVZp89Bo2dSQhB5A4MctqRQaN+tZUrrfge2OS8LSOKzqOYA7Ijo7FI4iyx/EacVaV4HcF4JsG94rBKPbYU8PAX86tD1Erq9M9fuJBotU4c97kX4gdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler("ca247252b9030967aec2ec711235281f")
#from _future_ import print_function
#from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import time
import re
import datetime
import random
import codecs
import sys
import json

from flask import Flask, request, abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)

################################

from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = "你的Channel access token"')
# Channel Secret
handler = WebhookHandler('"你的Channel secret"')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="Hi"):
        reply_text = "Hello"
        #Your user ID

    elif(text=="你好"):
        reply_text = "哈囉"
    elif(text=="機器人"):
        reply_text = "叫我嗎"
    else:
        reply_text = text
#如果非以上的選項，就會學你說話

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
