import RPi.GPIO as GPIO
from gpiozero import LineSensor
from time import sleep, time
from signal import pause #signal er indbygget i python idle3
from sshkeyboard import listen_keyboard

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


# Initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  

# Initialize the PWM for motors
GPIO.setup(PWM_A1, GPIO.OUT)
PWM_A1_pwm = GPIO.PWM(PWM_A1,1000)  # 1000 Hz frequency
PWM_A1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_A2, GPIO.OUT)
PWM_A2_pwm = GPIO.PWM(PWM_A2, 1000)  # 1000 Hz frequency
PWM_A2_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B1, GPIO.OUT)
PWM_B1_pwm = GPIO.PWM(PWM_B1, 1000)  # 1000 Hz frequency
PWM_B1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWM_B2, GPIO.OUT)
PWM_B2_pwm = GPIO.PWM(PWM_B2, 1000)  # 1000 Hz frequency
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
motor_B(True,False,100 )

def move(state, speedleft, speedright):
   #Control Motor A (Left Side)
    GPIO.output(DIR_A1, GPIO.HIGH if state else GPIO.LOW)  # Set direction for left motor
    GPIO.output(DIR_A2, GPIO.LOW if state else GPIO.HIGH)  # Adjust the opposite direction pin
    PWM_A1_pwm.ChangeDutyCycle(speedleft)  # Set speed for left motor
    PWM_A2_pwm.ChangeDutyCycle(speedleft)

    #Control Motor B (Right Side)
    GPIO.output(DIR_B1, GPIO.HIGH if state else GPIO.LOW)  # Set direction for right motor
    GPIO.output(DIR_B2, GPIO.LOW if state else GPIO.HIGH)  # Adjust the opposite direction pin
    PWM_B1_pwm.ChangeDutyCycle(speedright)  # Set speed for right motor
    PWM_B2_pwm.ChangeDutyCycle(speedright)



def GoForward():
 print('Going Forward')



def GoBackward():
    print('Going Backward')
    


def press(key):
    if key == "f":
    GoForward()

    elif key == "b":
    GoBackward()




try:
    while True:
    move(GPIO.LOW,50,50)  

    sleep(0.3)  # Adjust the sleep time to control the sensitivity of the line detection
       
except KeyboardInterrupt:
    print('Programmet er stoppet')
    pass

finally:
    GPIO.cleanup()
    PWM_A1_pwm.stop()
    PWM_A2_pwm.stop()
    PWM_B1_pwm.stop()
    PWM_B2_pwm.stop()
