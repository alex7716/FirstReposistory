import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 17

GPIO.setup(led,GPIO.OUT)
GPIO.cleanup()
