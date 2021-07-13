from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(0))

for i in range(1):

		buzzer.freq(500)
		buzzer.duty_u16(2000) #lound 
		sleep(0.5)
		buzzer.duty_u16(0) # sound stop


