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
    schet = 0
    for i in range(7, -1, -1):
        schet += 2**i
        gpio.output(dac, dec2bin(schet))
        t.sleep(0.0007)
        if gpio.input(comp) == 1:
            schet -= 2**i
    return schet    
try:
    while True:
        print(adc(), '{:.2f}v'.format(3.3*adc()/256) )
finally:
    gpio.output(dac, 0)
    gpio.cleanup()                   