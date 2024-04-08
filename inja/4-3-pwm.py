import RPi.GPIO as gpio
import time as t 
gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.OUT)
led = [2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(led, gpio.OUT)
pwm = gpio.PWM(21, 1000)
pwm.start(0)

try: 
    while True: 
        DutyCicle = int(input())
        gpio.output(21,1)
        pwm.start(DutyCicle)
        t.sleep(5)
        print("{:.2f}".format(DutyCicle*3.3/100))
        pwm.stop()

finally:
    gpio.output(led, 0)
    gpio.cleanup()

