import RPi.GPIO as gpio
import time as t 
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial = gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)
def dec2bin(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]  
def adc2():
    schet = 0
    for i in range(7, -1, -1):
        schet += 2**i
        gpio.output(dac, dec2bin(schet))
        t.sleep(0.0007)
        if gpio.input(comp) == 1:
            schet -= 2**i
    return schet 
def adc1():
    for i in range(256):
        dac2 = dec2bin(i)
        gpio.output(dac,dac2)
        compVal = gpio.input(comp)
        t.sleep (0.007) 
        if compVal == 1:
            return i    
def vol(n):
    n = round(n/256*8)
    d = [0 for i in range(8)]
    for i in range(n):
        d[i] += 1
    return d                
try:
    while True:
        gpio.output(leds, vol(adc1()))
        print(int(adc1())/256*3.3)
finally: 
    gpio.output(dac, 0)
    gpio.cleanup()     