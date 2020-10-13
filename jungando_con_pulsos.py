import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(20,GPIO.IN)
while True:
	GPIO.output(2,GPIO.input(20))

print(“Fin del programa”)
