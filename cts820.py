# cts820 touch driver for lvgl
# Created by Ste7an

import lvgl as lv
from machine import Pin, SoftI2C
import struct

class cts820:
    
    def __init__(self,scl=32,sda=33,freq=400000):
        self.touch = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=freq)
        self.touch.writeto_mem(21, 0xfe, b'\xff') # tell it not to sleep
        if not lv.is_initialized():
            lv.init()
        drv = lv.indev_create()
        drv.set_type(lv.INDEV_TYPE.POINTER)
        drv.set_read_cb(self.touch_cb)
    
    def read_touch(self):
        points, x1, y1 = struct.unpack('>BHH',self.touch.readfrom_mem(0x15, 0x02, 5))
        #print(x1,y1)
        return points, x1, y1

    def touch_cb(self,drv,data):
        points,x,y=self.read_touch()
        if points:
            data.point.x = y
            data.point.y = 240-x # mirror y
            data.state = lv.INDEV_STATE.PRESSED
        else:
            data.state = lv.INDEV_STATE.RELEASED
        return False


