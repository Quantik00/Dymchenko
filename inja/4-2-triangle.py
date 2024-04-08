import RPi.GPIO as gpio 
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]  

try:
    while (True):
        s = input()
        if not s.isdigit():
            print("Not a chislo, please try again")
        for i in range(255):
            gpio.output(dac, dec2bin(i))
            time.sleep(int(s)/256) 
        for i in range(255, -1, -1):
            time.gpio.output(dac, dec2bin(i))
            sleep(int(s)/256)      
finally:
    gpio.output(dac, 0)
    gpio.cleanup()               