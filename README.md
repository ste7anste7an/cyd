# Cheap Yellow Display

## LVGL micropython
Build the lv_micropython version for ESP_GENERIC

```
cd ~/projects/esp32/micropython_lvgl_esp32_generic/lv_micropython
./start_esp32_docker.sh
make -C mpy-cross
make -C ports/esp32 LV_CFLAGS="-DLV_COLOR_DEPTH=16" BOARD=GENERIC
cp ports/esp32/build-GENERIC/firmware.bin micropython_lvgl_firmware.bin
```

## Display and touch
The CYD has an ili9431 display controller and a CTS820 touch controller. The ili9341 is already part of the default modules in lvgl. For the touch controller we need to construct our own class.


## connect PUPremote
P3, IO35 = rx, IO22=tx

bovenaanzicht, dus over o de connector met de connector naar beneden
```
  _____
 | . . |
|  G . |
 | T R |
  -----


R -  IO22
T -  IO35
```

code op CYD ESP32
```
import lvgl as lv
import espidf as esp
from ili9XXX import ili9341,LANDSCAPE
from cts820 import cts820
import time

#init display
disp = ili9341(miso=12, mosi=13, clk=14, cs=15, dc=2, rst=-1, backlight=27,backlight_on=1, power=-1, width=320, height=240, rot=LANDSCAPE)
#from machine import I2S, Pin
#p=Pin(27,Pin.OUT)
#p.on()
tch=cts820()

from pup import  PUPRemoteSensor, SPIKE_ULTRASONIC

def msg(*argv):
    if argv!=():
        print(argv)
        a=int(argv[0])
        arc.set_value(a)
    return str(value)


arc=lv.arc(lv.screen_active())
arc.set_range(0,360)
arc.set_bg_angles(0,360)
arc.set_size(150,150)
arc.align(lv.ALIGN.CENTER,0,0)
arc.set_value(100)

value=1
p=PUPRemoteSensor(sensor_id=SPIKE_ULTRASONIC,rx=35,tx=22)
p.add_command('msg',"repr","repr")
while(True):
    connected=p.process()
    value+=1
    value%=255
    time.sleep_ms(20)

```

code op pybricks
```
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pupremote import PUPRemoteHub

hub = PrimeHub()

p=PUPRemoteHub(Port.A)
p.add_command('msg',"repr","repr")

i=0
while True:
    q=p.call('msg')
    #print(q)
    i+=1
    if i==20:
        p.call('msg',q)
        i=0
    wait(20)
```
