from machine import Pin, PWM
import time
from utime import sleep
import ssd1306

oled = ssd1306.SSD1306_I2C(128, 32, machine.I2C(0))

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

buzzer = PWM(Pin(15))


def find():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(5)
    trig.low()
    
    while echo.value() == 0:
        signaloff = time.ticks_us()
    
    while echo.value() == 1:
        signalon = time.ticks_us()
        
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    
    print("dis : ", distance, "cm")
 
    #oled.text("Dis : ", 0, 0)
    oled.text(str(distance) + " cm", 0, 0)
    
    if distance > 4.14:
        oled.text("water flowing", 0, 10)   
        oled.show()
        oled.fill(0)
    
    else:
        buzzer.freq(500)
        buzzer.duty_u16(1000)
        sleep(1)
        buzzer.duty_u16(0)
        print("water full") 
        oled.text("water full", 0, 10)
        oled.text("water off", 0, 20)       
        oled.show()
        oled.fill(0)
    
while True:
    find()
    time.sleep(1)
    