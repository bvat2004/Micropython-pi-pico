import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN)
led = machine.Pin(14, machine.Pin.OUT)
buzzer = machine.Pin(15, machine.Pin.OUT)     #for Active buzzer

def water_full(pin):
    print("ALARM! water full")
    for i in range(50):
        led.toggle()
        buzzer.toggle()
        utime.sleep_ms(100)
        
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler= water_full)

while True:
    led.toggle()
    utime.sleep(5)
