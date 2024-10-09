from time import sleep
from gpiozero import Motor, PWMOutputDevice, DistanceSensor

# Define the GPIO pins for the motors
MotorA1 = 11  # Motor A forward
MotorA2 = 10  # Motor A backward
PWMA = 23     # PWM control for Motor A

MotorB1 = 12  # Motor B forward
MotorB2 = 13  # Motor B backward
PWMB = 26     # PWM control for Motor B

# Define the GPIO pins for the ultrasonic sensor
TRIG = 4
ECHO = 5

# Initialize the PWM for motors
PWMA_pwm = PWMOutputDevice(PWMA)
PWMB_pwm = PWMOutputDevice(PWMB)

# Initialize motors
motorA = Motor(forward=MotorA1, backward=MotorA2)
motorB = Motor(forward=MotorB1, backward=MotorB2)

# Initialize the ultrasonic sensor
sensor = DistanceSensor(trigger=TRIG, echo=ECHO)

# Define motor control functions
def motor_A(forward, speed):
    """
    Control Motor A to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        motorA.forward(speed / 100.0)  # Convert speed to fraction
    else:
        motorA.backward(speed / 100.0)

def motor_B(forward, speed):
    """
    Control Motor B to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        motorB.forward(speed / 100.0)
    else:
        motorB.backward(speed / 100.0)

def full_stop():
    """Stop both motors."""
    motorA.stop()
    motorB.stop()

def avoid_obstacle():
    """Move back and turn if an obstacle is detected."""
    if sensor.distance < 0.2:  # If distance is less than 20 cm
        print("Obstacle detected! Moving back.")
        motor_A(False, 50)  # Move backward
        motor_B(False, 50)  # Move backward
        sleep(1)            # Move back for 1 second
        full_stop()         # Stop the motors
        sleep(0.5)          # Pause before turning
        print("Turning...")
        motor_A(True, 50)   # Turn one motor forward for a turn
        motor_B(False, 50)  # Turn the other motor backward
        sleep(1)            # Turn for 1 second
        full_stop()         # Stop the motors

# Example usage
try:
    while True:
        motor_A(True, 50)  # Move forward at 50% speed
        motor_B(True, 50)
        
        avoid_obstacle()    # Check for obstacles while moving forward

except KeyboardInterrupt:
    print("Program stopped by user.")
finally:
    full_stop()  # Ensure motors stop on exit