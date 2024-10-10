import RPi.GPIO as GPIO
from time import sleep

# Define the GPIO pins for the motors
MotorA1 = 27  # Motor A forward
MotorA2 = 28  # Motor A backward
PWMA1 = 0    # PWM control for Motor A forward
PWMA2 = 2    # PWM control for Motor A backward

MotorB1 = 24  # Motor B forward
MotorB2 = 25  # Motor B backward
PWMB1 = 4     # PWM control for Motor B forward
PWMB2 = 5     # PWM control for Motor B backward

# Define the GPIO pins for the ultrasonic sensor
#TRIG = 16
#ECHO = 18

# Initialize GPIO
GPIO.setmode(GPIO.BCM)

# Initialize the PWM for motors
GPIO.setup(PWMA1, GPIO.OUT)
PWMA1_pwm = GPIO.PWM(PWMA1, 100)  # 100 Hz frequency
PWMA1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWMA2, GPIO.OUT)
PWMA2_pwm = GPIO.PWM(PWMA2, 100)  # 100 Hz frequency
PWMA2_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWMB1, GPIO.OUT)
PWMB1_pwm = GPIO.PWM(PWMB1, 100)  # 100 Hz frequency
PWMB1_pwm.start(0)  # Initial duty cycle 0%

GPIO.setup(PWMB2, GPIO.OUT)
PWMB2_pwm = GPIO.PWM(PWMB2, 100)  # 100 Hz frequency
PWMB2_pwm.start(0)  # Initial duty cycle 0%

# Initialize motors
GPIO.setup(MotorA1, GPIO.OUT)
GPIO.setup(MotorA2, GPIO.OUT)
motorA_forward = GPIO.PWM(MotorA1, 100)  # 100 Hz frequency
motorA_backward = GPIO.PWM(MotorA2, 100)  # 100 Hz frequency

GPIO.setup(MotorB1, GPIO.OUT)
GPIO.setup(MotorB2, GPIO.OUT)
motorB_forward = GPIO.PWM(MotorB1, 100)  # 100 Hz frequency
motorB_backward = GPIO.PWM(MotorB2, 100)  # 100 Hz frequency

# Initialize the ultrasonic sensor
#GPIO.setup(TRIG, GPIO.OUT)
#GPIO.setup(ECHO, GPIO.IN)

# Define motor control functions
def motor_A(forward, speed):
    """
    Control Motor A to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        PWMA1_pwm.ChangeDutyCycle(speed)
        motorA_forward.ChangeDutyCycle(speed / 100.0)
        motorA_forward.start()
    else:
        PWMA2_pwm.ChangeDutyCycle(speed)
        motorA_backward.ChangeDutyCycle(speed / 100.0)
        motorA_backward.start()

def motor_B(forward, speed):
    """
    Control Motor B to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        PWMB1_pwm.ChangeDutyCycle(speed)
        motorB_forward.ChangeDutyCycle(speed / 100.0)
        motorB_forward.start()
    else:
        PWMB2_pwm.ChangeDutyCycle(speed)
        motorB_backward.ChangeDutyCycle(speed / 100.0)
        motorB_backward.start()

def full_stop():
    """Stop both motors."""
    motorA_forward.stop()
    motorA_backward.stop()
    motorB_forward.stop()
    motorB_backward.stop()

#def avoid_obstacle():
#    """Move back and turn if an obstacle is detected."""
#    if sensor.distance < 0.2:  # If distance is less than 20 cm
#        print("Obstacle detected! Moving back.")
#        motor_A(False, 50)  # Move backward
#        motor_B(False, 50)  # Move backward
#        sleep(1)            # Move back for 1 second
#        sleep(0.5)          # Pause before turning
#        print("Turning...")
#        motor_A(True, 50)   # Turn one motor forward for a turn
#        motor_B(False, 50)  # Turn the other motor backward
#        sleep(1)            # Turn for 1 second
#        full_stop()         # Stop the motors

# Example usage
try:
    while True:
        motor_A(True, 50)  # Move forward at