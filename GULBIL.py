from turtle import backward
import gpiozero as GPIO
from gpiozero import Motor,LineSensor
from time import sleep, time
from signal import pause #signal er indbygget i python idle3
from sshkeyboard import listen_keyboard

# Motor A
DIR_A1 = 4 # skal skiftes  # DIR 1 for Motor A
DIR_A2 = 11 # 11 # DIR 2 for Motor A
PWM_A1 = 24 # 24 # PWM 1 for Motor A
PWM_A2 = 10 # 10 # PWM 2 for Motor A

# Motor B
DIR_B1 = 17 # skiftes # DIR 1 for Motor B
DIR_B2 = 9 # 9 # DIR 2 for Motor B
PWM_B1 = 27 # 27 # PWM 1 for Motor B
PWM_B2 = 7 # 7 # PWM 2 for Motor B

# Sensor A
SEN_1 = 11
# Sensor B
SEN_2 = 16

sensor = LineSensor(SEN_1, SEN_2)


# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  

# Initialize the PWM for motors
GPIO.setup(PWM_A1, GPIO.OUT)
PWM_A1_pwm = GPIO.PWM(PWM_A1, 50)  # 50 Hz frequency
PWM_A1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_A2, GPIO.OUT)
PWM_A2_pwm = GPIO.PWM(PWM_A2, 50)  # 50 Hz frequency
PWM_A2_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B1, GPIO.OUT)
PWM_B1_pwm = GPIO.PWM(PWM_B1, 50)  # 50 Hz frequency
PWM_B1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B2, GPIO.OUT)
PWM_B2_pwm = GPIO.PWM(PWM_B2, 50)  # 50 Hz frequency
PWM_B2_pwm.start(0)  # Initial duty cycle 0%

# Initialize DIR pins
GPIO.setup(DIR_A1, GPIO.OUT)
GPIO.setup(DIR_A2, GPIO.OUT)
GPIO.setup(DIR_B1, GPIO.OUT)
GPIO.setup(DIR_B2, GPIO.OUT)

# Define motor control functions
def motor_A(dir1, dir2, speed):
    """
    Control Motor A to move in a specific direction at a given speed.
    :param dir1: Boolean value indicating direction 1.
    :param dir2: Boolean value indicating direction 2.
    :param speed: Speed percentage (0-100).
    """
    GPIO.output(DIR_A1, GPIO.HIGH if dir1 else GPIO.LOW)
    GPIO.output(DIR_A2, GPIO.HIGH if dir2 else GPIO.LOW)
    PWM_A1_pwm.ChangeDutyCycle(speed)
    PWM_A2_pwm.ChangeDutyCycle(speed)

def motor_B(dir1, dir2, speed):
    """
    Control Motor B to move in a specific direction at a given speed.
    :param dir1: Boolean value indicating direction 1.
    :param dir2: Boolean value indicating direction 2.
    :param speed: Speed percentage (0-100).
    """
    GPIO.output(DIR_B1, GPIO.HIGH if dir1 else GPIO.LOW)
    GPIO.output(DIR_B2, GPIO.HIGH if dir2 else GPIO.LOW)
    PWM_B1_pwm.ChangeDutyCycle(speed)
    PWM_B2_pwm.ChangeDutyCycle(speed)

motor_A(True, False, 100)

def move(state,speedleft,speedright):
    GPIO.output(DIR_A1,state)
    GPIO.output(DIR_A2,state)
    GPIO.output(DIR_B1,state)
    GPIO.output(DIR_B2,state)
    PWM_A1_pwm.ChangeDutyCycle(speedleft)
    PWM_A2_pwm.ChangeDutyCycle(speedleft)
    PWM_B1_pwm.ChangeDutyCycle(speedleft)
    PWM_B2_pwm.ChangeDutyCycle(speedleft)



def GoForward():
    print('Going Forward')
    motor_A(True, 50)  # Kører fremad 50% speed
    motor_B(True, 50)


def GoBackward():
    print('Going Backward')
    motor_A(False, 50)  # Kører baglæns 50% speed
    motor_B(False, 50)


def press(key):
    if key == "f":
        GoForward()
    elif key == "b":
        GoBackward()


#change th texthahahah




# Initialize the line sensor

def on_line():
    """Function to call when the sensor detects the line."""
    print("Line detected! Moving forward.")
    motor_A(True, 50)  # Move forward
    motor_B(True, 50)  # Move forward

def off_line():
    """Function to call when the sensor does not detect the line."""
    print("Off the line! Stopping or adjusting.")
    time.sleep(0.5)  # Stop the motors

# Attach callbacks to the line sensor
LineSensor.when_line = on_line
LineSensor.when_no_line = off_line

try:
    while True:
        motor_A(True, 50)  # Move forward at 50% speed
        motor_B(True, 50)
        sleep(0)
       
except KeyboardInterrupt:
    print('Program stopped by user.')
finally:
    GPIO.cleanup()
    PWM_A1_pwm.stop()
    PWM_A2_pwm.stop()
    PWM_B1_pwm.stop()
    PWM_B2_pwm.stop()
