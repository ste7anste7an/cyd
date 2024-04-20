import lvgl as lv
import espidf as esp
from ili9XXX import ili9341,LANDSCAPE
from cts820 import cts820

#init display
disp = ili9341(miso=12, mosi=13, clk=14, cs=15, dc=2, rst=-1, backlight=27,backlight_on=1, power=-1, width=320, height=240, rot=LANDSCAPE)
#from machine import I2S, Pin
#p=Pin(27,Pin.OUT)
#p.on()
tch=cts820()
#btn=lv.button(lv.screen_active())


arc=lv.arc(lv.screen_active())
arc.set_range(0,360)
arc.set_bg_angles(0,360)
arc.set_size(150,150)
arc.align(lv.ALIGN.CENTER,0,0)
arc.set_value(100)

slider = lv.slider(lv.screen_active())
slider.set_width(200)
slider.align(lv.ALIGN.CENTER,0,-100)
slider.set_range(0,360)


group = lv.group_create()
group.add_obj(arc)
group.add_obj(slider)

