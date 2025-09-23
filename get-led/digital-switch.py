import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
button = 13
GPIO.setup(button, GPIO.IN)
state = 0

while True:
    if GPIO.input(button):
        state = not state
        time.sleep(0.2)
    GPIO.output(led, state)