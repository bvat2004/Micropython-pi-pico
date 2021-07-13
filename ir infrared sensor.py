from machine import Pin
import utime

led = Pin(28, Pin.OUT)
sensor = Pin(2, Pin.IN)


while True:
	
	print('sensor : ', sensor.value())
	utime.sleep(0.5)
	
	if sensor.value() == 1:
		led.value(0)
	else:
		led.value(1)
		
	
	
