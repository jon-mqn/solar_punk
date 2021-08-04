import gpiozero
import sys
from time import sleep
from signal import pause

button_pump = gpiozero.Button(15) # wired to GPIO and ground (20)
button_off = gpiozero.Button(23) # wired to GPIO and ground (14)
hygrometer = gpiozero.DigitalputDevice(14) # wired to 5v, GPIO, and ground (6)


def shutdown():
    print("exiting")
    sys.exit()


button_off.when_pressed = shutdown
# Test the hygrometer
levels = []
print("Begin hygrometer test...")
whle True:
    moisture = hygrometer.value
    levels.append(moisture)
    print(f'Moisture evels: {moisture}')
print("End hygrometer test")
print(levels)
