from machine import Pin, ADC
from time import sleep

ldr = ADC(27)
led = Pin(0, Pin.OUT, value = 0)
relay = Pin(1, Pin.OUT, value = 1)
reading = 0
# led.low()

while True:
   reading = ldr.read_u16()
   print(reading)
   if reading < 32678 and reading <29000:
       
      
       led.toggle()
       print('light on')   
       relay.value(0)
       sleep(1)
        
   else:
       led.off()
       print('light OFF')
       relay.value(1)
       sleep(1)   
    
       
   
   