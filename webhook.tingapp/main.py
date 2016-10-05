# -*- coding: utf-8 -*-
import tingbot
from tingbot import *

font = 'NotoSansCJKjpRegular.otf'
font_color = 'white'
wh_name = str(tingbot.app.settings['webhook_name'])

screen.fill(color='black')
screen.text('Waiting...')

@webhook(wh_name)
def on_webhook(data):
    data = data.decode('utf-8')
    screen.fill(color='black')
    screen.text(data, color=font_color, font=font)
tingbot.run()
