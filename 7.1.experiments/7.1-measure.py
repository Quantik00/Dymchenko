import RPi.GPIO as gpio
from matplotlib import pyplot
import time
# настраиваем нашу работу с GPIO
gpio.setmode(gpio.BCM)

leds =[2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(leds,gpio.OUT)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
gpio.setup(dac, gpio.OUT, initial = gpio.HIGH)

comp = 14
troyka = 13
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

#измерение напряжение на выходе тройка-модуля
def adc():
    k = 0  
    for i in range(7, -1, -1):
        k += 2**i
        gpio.output(dac, dec2bin(k))
        time.sleep(0.007)
        if gpio.input(comp) == 1:
            k -= 2**i
    return k 

#выводим двоичное представление числа в область светодиодов   
def dec2bin(a):
    return[int(element) for element in bin(a)[2:].zfill(8)]
# размещаем исполняемую часть скрипта в try
try:
    volts = 0
    result_measure = [] #список для добавления новых измерений 
    time_start =time.time() #момент начала измерений
    count = 0
    #измерения в момент зарядки конденсатора
    print("-/ Зарядка конденсатора\- ")
    while volts < 207:
        volts = adc()
        result_measure.append(volts)
        time.sleep(0.01)
        count += 1
        gpio.output(leds, dec2bin(volts))
        print(volts)

    time_expereiment = time.time() - time_start    
    # #измерения в момент разрядки конденсатора
    # print("-/ Разрядка конденсатора\- ")
    # while volts > 256*0.02:
    #     volts = adc()
    #     result_measure.append(volts)
    #     time.sleep(0.007)
    #     count +=1
    #     gpio.output(leds, dec2bin(volts))
    #     print(volts)
 
    # time_expereiment = time.time() - time_start 
    # #запись данных под графики
    print("Запись данных")
    with open ('data.txt','w') as f:
        for i in result_measure:
            f.write(str(i) + '\n') 
    with open ('settings.txt', 'w') as f:
        f.write(str(count/time_expereiment) + '\n') 
        f.write(str(3.3/256)) 
    print('продолжительность {}', format(time_expereiment))

    #Графики
    print('Графики')
    x = [i*time_expereiment/count for i in range(len(result_measure))] 
    y = [i/256*3.3 for i in result_measure]
    pyplot.plot(x, y, color = 'purple', marker = 'o', markersize = 4 )
    pyplot.xlabel('Время')
    pyplot.ylabel('Напряжение')
    pyplot.title('График зависимости показаний АЦП от времени')
    pyplot.show()

#подаем 0 на все GPIO выходы и сбрасываем настройки GPIO в блоке finally
finally:
    gpio.output(leds, 0)
    gpio.output(dac, 0)
    gpio.cleanup()    
