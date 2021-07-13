from machine import Pin
import utime

ldr = machine.ADC(27)
led = Pin(0, Pin.OUT, value = 0)
relay = Pin(1, Pin.OUT, value = 1)
# led.low()

while True:
   reading = ldr.read_u16()
   print("ADC : ", reading)
   utime.sleep(0.2)
   
   if reading < 60000:
       print("??")
       relay.value(0)
       led.toggle()      
       utime.sleep(1)
      
  
   elif reading > 30000:
       print("no ok")
       relay.value(1)
       led.low()
   #utime.sleep(0.2)
   
  
 