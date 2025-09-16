import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 26
phototrans = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(phototrans, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(phototrans))
