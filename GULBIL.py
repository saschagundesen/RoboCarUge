
import gpiozero as GPIO
from gpiozero import Motor,LineSensor
from time import sleep, time
from signal import pause #signal er indbygget i python idle3
#from sshkeyboard import listen_keyboard

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

#sensor = LineSensor(SEN_1, SEN_2)
sensor_A = LineSensor(SEN_1)
sensor_B = LineSensor(SEN_2)


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

    PWM_A1_pwm.ChangeDutyCycle(speedright)
    PWM_A2_pwm.ChangeDutyCycle(speedleft)
    PWM_B1_pwm.ChangeDutyCycle(speedright)
    PWM_B2_pwm.ChangeDutyCycle(speedleft)



#def GoForward():
#    print('Going Forward')
#    move(GPIO.HIGH, 50,50)  # Kører fremad 50% speed


#def GoBackward():
#    print('Going Backward')
#    move(GPIO.LOW, 50, 50)  # Kører baglæns 50% speed


#def press(key):
#    if key == "f":
#        GoForward()
#    elif key == "b":
#        GoBackward()


# Initialize the line sensor

#Define callback functions for each sensor
def on_line_A():
    """Function to call when sensor A detects the line."""
    print("Sensor A: Line detected! Moving forward.")
    motor_A(True, False, 50)  # Motor A moves forward with 50% speed

def off_line_A():
    """Function to call when sensor A does not detect the line."""
    print("Sensor A: Off the line! Stopping.")
    motor_A(False, False, 0)  # Stop Motor A

def on_line_B():
    """Function to call when sensor B detects the line."""
    print("Sensor B: Line detected! Moving forward.")
    motor_B(True, False, 50)  # Motor B moves forward with 50% speed

def off_line_B():
    """Function to call when sensor B does not detect the line."""
    print("Sensor B: Off the line! Stopping.")
    motor_B(False, False, 0)  # Stop Motor B

#Attach callbacks to the line sensors
sensor_A.when_line = on_line_A
sensor_A.when_no_line = off_line_A

sensor_B.when_line = on_line_B
sensor_B.when_no_line = off_line_B


try:
    while True:
        motor_A(True, False, 50)  # Move forward at 50% speed
        motor_B(True, False, 50)
        sleep(0)
       
except KeyboardInterrupt:
    print('Program stopped by user.')
finally:
    GPIO.cleanup()
    PWM_A1_pwm.stop()
    PWM_A2_pwm.stop()
    PWM_B1_pwm.stop()
    PWM_B2_pwm.stop()
