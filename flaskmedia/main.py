import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'
import sys

led_pins = [7, 11]
control = sys.argv[1].strip().lower()=='on' 
no = int(sys.argv[2])

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(led_pins[no], GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(led_pins[no],control)

