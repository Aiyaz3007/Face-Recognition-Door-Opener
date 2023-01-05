from pyfirmata import SERVO
from pyfirmata.util import Iterator
import pyfirmata
import time


board = pyfirmata.ArduinoMega("")
servo = board.get_pin('d:12:o')
board.digital[12].mode = SERVO

def Servo_Controller(act):
    if act:
        value = 180
        servo.write(value)
        time.sleep(2)
    else:
        value = 0
        servo.write(value)
        