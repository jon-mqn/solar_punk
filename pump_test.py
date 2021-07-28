import gpiozero
import sys
from time import sleep
from signal import pause

button_pump = gpiozero.Button(15) # wired to GPIO and ground (20)
button_off = gpiozero.Button(23) # wired to GPIO and ground (14)
pump = gpiozero.OutputDevice(14) # wired to 5v, GPIO, and ground (6)
led = gpiozero.LED(18) # wied to GPIO and ground (30). btween GPIO and long leg should be resistor (330)

def pump_on():
    pump.on()
    led.blink()
    print("pump on")


def pump_off():
    pump.off()
    led.off()
    print("pump off")
    led.on()


def shutdown():
    print("exiting")
    sys.exit()


button_pump.when_pressed = pump_on
button_pump.when_released = pump_off
button_off.when_pressed = shutdown
led.on()
# Test the pump
print("Begin pump test...")
pump.on()
sleep(3)
pump.off()
print("End pump test")

while True:
    pause()
