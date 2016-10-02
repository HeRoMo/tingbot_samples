# -*- coding: utf-8 -*-

import tingbot
from tingbot import *

# setup code here

@every(seconds=1.0/30)
def loop():
    # drawing code here
    screen.fill(color='black')
    message = u'日本語もOK'
    screen.text(message, xy=(0,0), color="white", align='topleft',
                font='fonts/NotoSansCJKjpRegular.otf')
    screen.text(message, xy=(0,45), color="blue", align='topleft',
                font='fonts/ipagp.ttf')
    screen.text(message, xy=(0,80), color="aqua", align='topleft' , 
                font='fonts/ipamp.ttf')
    screen.text(message, xy=(0,120), color="lime", align='topleft' ,
                font='fonts/cinecaption226.ttf')
    screen.text(message, xy=(0,160), color="yellow", align='topleft', 
                font='fonts/TanukiMagic.ttf')
    screen.text(message, xy=(0,200), color="fuchsia", align='topleft', 
                font='fonts/kiloji_p.ttf')

tingbot.run()
