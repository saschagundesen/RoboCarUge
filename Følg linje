import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Motor A
DIR_A1 = 4  # DIR 1 for Motor A
DIR_A2 = 11  # DIR 2 for Motor A
PWM_A1 = 24  # PWM 1 for Motor A
PWM_A2 = 10  # PWM 2 for Motor A

# Motor B
DIR_B1 = 17  # DIR 1 for Motor B
DIR_B2 = 9  # DIR 2 for Motor B
PWM_B1 = 27  # PWM 1 for Motor B
PWM_B2 = 7   # PWM 2 for Motor B

# Sensor A
SEN_1 = 11
# Sensor B
SEN_2 = 16

# Set up motor pins
GPIO.setup(DIR_A1, GPIO.OUT)
GPIO.setup(DIR_A2, GPIO.OUT)
GPIO.setup(PWM_A1, GPIO.OUT)
GPIO.setup(PWM_A2, GPIO.OUT)

GPIO.setup(DIR_B1, GPIO.OUT)
GPIO.setup(DIR_B2, GPIO.OUT)
GPIO.setup(PWM_B1, GPIO.OUT)
GPIO.setup(PWM_B2, GPIO.OUT)

# Set up sensor pins
GPIO.setup(SEN_1, GPIO.IN)
GPIO.setup(SEN_2, GPIO.IN)

# Create PWM objects for controlling the motors
pwm_a1 = GPIO.PWM(PWM_A1, 100)
pwm_a2 = GPIO.PWM(PWM_A2, 100)
pwm_b1 = GPIO.PWM(PWM_B1, 100)
pwm_b2 = GPIO.PWM(PWM_B2, 100)

# Start PWM with 0 duty cycle (motors off)
pwm_a1.start(0)
pwm_a2.start(0)
pwm_b1.start(0)
pwm_b2.start(0)

def move_forward(speed):
    # Move both motors forward
    GPIO.output(DIR_A1, GPIO.HIGH)
    GPIO.output(DIR_A2, GPIO.LOW)
    GPIO.output(DIR_B1, GPIO.HIGH)
    GPIO.output(DIR_B2, GPIO.LOW)
    pwm_a1.ChangeDutyCycle(speed)
    pwm_a2.ChangeDutyCycle(0)
    pwm_b1.ChangeDutyCycle(speed)
    pwm_b2.ChangeDutyCycle(0)

def turn_left(speed):
    # Stop motor B and move motor A forward
    GPIO.output(DIR_A1, GPIO.HIGH)
    GPIO.output(DIR_A2, GPIO.LOW)
    GPIO.output(DIR_B1, GPIO.LOW)
    GPIO.output(DIR_B2, GPIO.LOW)
    pwm_a1.ChangeDutyCycle(speed)
    pwm_a2.ChangeDutyCycle(0)
    pwm_b1.ChangeDutyCycle(0)
    pwm_b2.ChangeDutyCycle(0)

def turn_right(speed):
    # Stop motor A and move motor B forward
    GPIO.output(DIR_A1, GPIO.LOW)
    GPIO.output(DIR_A2, GPIO.LOW)
    GPIO.output(DIR_B1, GPIO.HIGH)
    GPIO.output(DIR_B2, GPIO.LOW)
    pwm_a1.ChangeDutyCycle(0)
    pwm_a2.ChangeDutyCycle(0)
    pwm_b1.ChangeDutyCycle(speed)
    pwm_b2.ChangeDutyCycle(0)

def stop():
    # Stop both motors
    pwm_a1.ChangeDutyCycle(0)
    pwm_a2.ChangeDutyCycle(0)
    pwm_b1.ChangeDutyCycle(0)
    pwm_b2.ChangeDutyCycle(0)

try:
    while True:
        sensor1 = GPIO.input(SEN_1)
        sensor2 = GPIO.input(SEN_2)
        
        if sensor1 == GPIO.LOW and sensor2 == GPIO.LOW:
            # Move forward if both sensors are off the line
            move_forward(50)
        elif sensor1 == GPIO.HIGH and sensor2 == GPIO.LOW:
            # Turn left if sensor 1 detects the line
            turn_left(50)
        elif sensor1 == GPIO.LOW and sensor2 == GPIO.HIGH:
            # Turn right if sensor 2 detects the line
            turn_right(50)
        else:
            # Stop if both sensors detect the line (end of the track)
            stop()
        
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    pwm_a1.stop()
    pwm_a2.stop()
    pwm_b1.stop()
    pwm_b2.stop()
    GPIO.cleanup()
