import RPi.GPIO as gpio
import time as t 
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial = gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)
def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]  
def adc():
    for i in range(256):
        dac2 = dec2bin(i)
        gpio.output(dac,dac2)
        compVal = gpio.input(comp)
        t.sleep (0.007) 
        if compVal == 1:
            return i
try:
    while True:
        print(adc(), '{:.2f}v'.format(3.3*adc()/256) )
finally:
    gpio.output(dac, 0)
    gpio.cleanup()                   