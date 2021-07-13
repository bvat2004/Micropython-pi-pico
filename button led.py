from machine import Pin
import time
import utime 
import ssd1306

button = Pin(1, Pin.IN, Pin.PULL_DOWN)
led = machine.Pin(28, machine.Pin.OUT)

last_state =FALSE
current_state = FALSE


while True:
	if button.value():
		print("press buttion",button.value())
		led.toggle()
		#time.sleep(0.5)