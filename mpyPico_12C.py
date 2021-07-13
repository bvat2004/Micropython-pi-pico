import uos
import machine

print(uos.uname())
print("Freq: "  + str(machine.freq()) + " Hz")

i2c = machine.I2C(0)
print(i2c)

print("Available i2c devices: "+ str(i2c.scan()))