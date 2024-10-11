import RPi.GPIO as GPIO
from gpiozero import LineSensor
from time import sleep, time
from signal import pause #signal er indbygget i python idle3
#from sshkeyboard import listen_keyboard

# Motor A
DIR_A1 = 4 # skal skiftes  # DIR 1 for Motor A
DIR_A2 = 23 # 11 # DIR 2 for Motor A
PWM_A1 = 18 # 24 # PWM 1 for Motor A
PWM_A2 = 19 # 10 # PWM 2 for Motor A

# Motor B
DIR_B1 = 17 # skiftes # DIR 1 for Motor B
DIR_B2 = 21 # 9 # DIR 2 for Motor B
PWM_B1 = 13 # 27 # PWM 1 for Motor B
PWM_B2 = 26 # 7 # PWM 2 for Motor B

# Sensor A
SEN_1 = 11
# Sensor B
SEN_2 = 16

#sensor = LineSensor(SEN_1, SEN_2)
sensor_A = LineSensor(SEN_1)
sensor_B = LineSensor(SEN_2)
#prøv


# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  

# Initialize the PWM for motors
GPIO.setup(PWM_A1, GPIO.OUT)
PWM_A1_pwm = GPIO.PWM(PWM_A1, 1000)  # 50 Hz frequency
PWM_A1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_A2, GPIO.OUT)
PWM_A2_pwm = GPIO.PWM(PWM_A2, 1000)  # 50 Hz frequency
PWM_A2_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B1, GPIO.OUT)
PWM_B1_pwm = GPIO.PWM(PWM_B1, 1000)  # 50 Hz frequency
PWM_B1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B2, GPIO.OUT)
PWM_B2_pwm = GPIO.PWM(PWM_B2, 1000)  # 50 Hz frequency
PWM_B2_pwm.start(0)  # Initial duty cycle 0%

# Initialize DIR pins
GPIO.setup(DIR_A1, GPIO.OUT)
GPIO.setup(DIR_A2, GPIO.OUT)
GPIO.setup(DIR_B1, GPIO.OUT)
GPIO.setup(DIR_B2, GPIO.OUT)

GPIO.setup(SEN_1,GPIO.IN)
GPIO.setup(SEN_2,GPIO.IN)

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



# Define direction control functions

# Use keyboard to trigger these movements
#def press(key):
   # if key == "f":
       # GoForward()
    #elif key == "b":
       # GoBackward()
    #elif key == "l":
       # TurnLeft()
   # elif key == "r":
       # TurnRight()



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
  
        print("Sensor A: Line detected! Adjusting motors.")
        # Motor A continues forward, Motor B slows down or adjusts
        motor_A(True, False, 60)  # Move Motor A forward at 50% speed
        motor_B(True, False, 30)  # Slow Motor B to turn towards the line

def off_line_A():
    
        print("Sensor A: Off the line! Adjusting motors.")
        # Adjust motors when the sensor loses the line
        motor_A(True, False, 30)  # Stop Motor A
        motor_B(True, False, 60)  # Speed up Motor B to adjust course

def on_line_B():
    
        print("Sensor B: Line detected! Adjusting motors.")
        # Motor B continues forward, Motor A slows down or adjusts
        motor_A(True, False, 30)  # Slow Motor A to turn towards the line
        motor_B(True, False, 60)  # Move Motor B forward at 50% speed

def off_line_B():
    
        print("Sensor B: Off the line! Adjusting motors.")
        motor_A(True, False, 60)  # Speed up Motor A to adjust course
        motor_B(True, False, 30)  # Stop Motor B


#Attach callbacks to the line sensors
sensor_A.when_line = on_line_A
sensor_A.when_no_line = off_line_A

sensor_B.when_line = on_line_B
sensor_B.when_no_line = off_line_B

def move(state, speedleft, speedright):
    """ Move the robot based on speed of left and right motors """
    # Motor A (left motor)
    GPIO.output(DIR_A1, GPIO.HIGH if state else GPIO.LOW)
    GPIO.output(DIR_A2, GPIO.LOW)
    PWM_A1_pwm.ChangeDutyCycle(speedleft)
    PWM_A2_pwm.ChangeDutyCycle(speedleft)

    # Motor B (right motor)
    GPIO.output(DIR_B1, GPIO.HIGH if state else GPIO.LOW)
    GPIO.output(DIR_B2, GPIO.LOW)
    PWM_B1_pwm.ChangeDutyCycle(speedright)
    PWM_B2_pwm.ChangeDutyCycle(speedright)



try:
    while True:
        move(GPIO.LOW,60,60)
        print("Motor speed:",PWM_A1_pwm.ChangeDutyCycle(60))
        print("Motor direction:",GPIO.output(DIR_A1,GPIO.HIGH))
        sleep(0.5)
       
except KeyboardInterrupt:
    print('Programmet er stoppet')
    pass

finally:
    GPIO.cleanup()
    PWM_A1_pwm.stop()
    PWM_A2_pwm.stop()
    PWM_B1_pwm.stop()
    PWM_B2_pwm.stop()