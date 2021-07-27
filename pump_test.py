import gpiozero
import sys
from time import sleep

button_pump = gpiozero.Button(25) # wired to GPIO and ground (20)
button_off = gpiozero.Button(23) # wired to GPIO and ground (14)
pump = gpiozero.OutputDevice(21) # wired to 5v, GPIO, and ground (6)
led = gpiozero.LED(17) # wied to GPIO and ground (30). btween GPIO and long leg should be resistor (330)

def pump_on():
    pump.on()
    led.blink()


def pump_off():
    pump.off()
    led.off()
    print("pump off")


def shutdown():
    print("exiting")
    sys.exit()


button_pump.when_pressed = pump_on
button_pump.when_released = pump_off
button_off.when_pressed = shutdown


while True:
    if button_off.is_pressed:
        break
    sleep(.1)