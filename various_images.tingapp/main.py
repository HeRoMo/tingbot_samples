# To add images, first drag an image into the sidebar,
# or use the 'Import...' button at the bottom of the 
# sidebar.

# Once imported, images can be displayed using the
# screen.image() method. Even animated GIFs work!

import tingbot
from tingbot import *

@every(seconds=1.0/30)
def loop():
    screen.fill(color='white')
    screen.image('images/fireworks.gif', xy=(0,10), align='topleft')
    screen.image('images/fireworks.png', xy=(110,10), align='topleft')
    screen.image('images/fireworks.jpg', xy=(220,10), align='topleft')
    screen.image('images/fireworks.bmp', xy=(0,80), align='topleft')
    # screen.image('images/fireworks.webp', xy=(0,150), align='topleft')
    
    screen.image('images/red.png', xy=(160,100), align='topleft')
    screen.image('images/blue.png', xy=(140,125), align='topleft')
    screen.image('images/green.png', xy=(190,135), align='topleft')

tingbot.run()
