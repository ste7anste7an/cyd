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


