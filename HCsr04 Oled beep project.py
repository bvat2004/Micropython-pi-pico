from machine import Pin
import time
import utime 
import ssd1306

oled = ssd1306.SSD1306_I2C(128, 64, machine.I2C(0))

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

led = machine.Pin(28, machine.Pin.OUT)
buzzer = machine.Pin(0, machine.Pin.OUT)

def water_full():
    print("ALARM! water full")
    led.toggle()
    
    for i in range(5):
		buzzer.toggle()
		utime.sleep_ms(200)
		

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
    
    if distance > 2.4545:
        oled.text("water flowing", 0, 10)   
        oled.show()
        oled.fill(0)
    
    else:
        water_full()
        print("water full") 
        oled.text("ALARM! water full", 0, 10)
        oled.text("water off", 0, 20)       
        oled.show()
        oled.fill(0)
    
while True:
    find()
    led.off()
    buzzer.off()
    time.sleep(1)
    