from gpiozero import Button, LED
import time

btn = Button(17)
led = LED(4)
# btn.when_pressed = led.on
# btn.when_released = led.off


# time.sleep(20)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
