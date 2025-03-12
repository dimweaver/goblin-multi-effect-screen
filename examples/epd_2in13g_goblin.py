#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13g
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("epd2in13g Goblin MFX Demo")

    epd = epd2in13g.EPD()   
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
 
    # Drawing on the image
    logging.info("1.Drawing on the image...")
    Himage = Image.new('RGB', (epd.height, epd.width), epd.WHITE)  
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 60), 'OCCASIONALLY FUNCTIONING', font = font15, fill = epd.BLACK)
    draw.text((20, 90), 'AUDIO UTILITIES', font = font15, fill = epd.BLACK)
    

    epd.display(epd.getbuffer(Himage))
    time.sleep(5)
    
    # read bmp file 
    logging.info("2.read bmp file")
    Himage = Image.open(os.path.join(picdir, '2in13g.bmp'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(20)
    
    logging.info("Clear...")
    epd.Clear()
    
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13g.epdconfig.module_exit(cleanup=True)
    exit()
