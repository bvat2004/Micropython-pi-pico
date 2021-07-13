from machine import Pin
from time import sleep

relay = Pin(16, Pin.OUT)     #ต่อขา GP16 เป็น output

while True:
    relay.value(1)          #รีเลย์ทำงาน = digitalWrite(16,LOW)
    sleep(1)                # delay 1 วินาที
    relay.value(0)          #รีเลย์ off
    sleep(0)
    
    
