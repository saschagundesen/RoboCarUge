from time import sleep
import gpiozero as GPIO
from gpiozero import Motor, PWMOutputDevice, DistanceSensor,LineSensor
from signal import pause #signal er indbygget i python idle3
from sshkeyboard import listen_keyboard

# Establish an SSH connection to the Raspberry Pi
#ssh = sshkeyboard.SSH('pi@raspberrypi.local')

# Define the GPIO pins for the motors
MotorA1 = 26  # Motor A forward
MotorA2 = 24  # Motor A backward
PWMA = 12     # PWM control for Motor A

MotorB1 = 19  # Motor B forward
MotorB2 = 21  # Motor B backward
PWMB = 13     # PWM control for Motor B

# Define the GPIO pins for the ultrasonic sensor
TRIG = 16
ECHO = 18

#Line sensor - KY 033 JOY IT- 15 pin
SENSOR_PIN = 3 
SENSOR_PIN2 = 4

# Initialize the PWM for motors
PWMA_pwm = PWMOutputDevice(PWMA)
PWMB_pwm = PWMOutputDevice(PWMB)

# Initialize motors
motorA = Motor(forward=MotorA1, backward=MotorA2)
motorB = Motor(forward=MotorB1, backward=MotorB2)

# Initialize the ultrasonic sensor
sensor = DistanceSensor(trigger=TRIG, echo=ECHO)

#Kalder KY sensor
sensor = LineSensor(SENSOR_PIN,SENSOR_PIN2)

# Define motor control functions
def motor_A(forward, speed):
    """
    Control Motor A to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        motorA.forward(speed / 100.0)  # Convert speed to fraction
        motorA.forward() # Move forward
    else:
        PWMA_pwm.value = speed /100.0
        motorA.backward(speed / 100.0)

def motor_B(forward, speed):
    """
    Control Motor B to move forward or backward at a given speed.
    :param forward: Boolean value indicating direction.
    :param speed: Speed percentage (0-100).
    """
    if forward:
        motorB.forward(speed / 100.0)
        motorB.forward()  # Move forward
    else:
        PWMB_pwm.value = speed / 100.0  # Set PWM value
        motorB.backward(speed / 100.0)

def full_stop():
    """Stop both motors."""
    motorA.stop()
    motorB.stop()

def avoid_obstacle():
    """Move back and turn if an obstacle is detected."""
    if sensor.distance < 0.2:  # Hvis afstanden er mindre end 20 cm
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



def on_line():
    """Function to call when the sensor detects the line."""
    print("Line detected! Moving forward.")
    motor_A(True, 50)  # Move forward
    motor_B(True, 50)  # Move forward

def off_line():
    """Function to call when the sensor does not detect the line."""
    print("Off the line! Stopping or adjusting.")
    full_stop()  # Stop the motors

# Attach callbacks to the line sensor
LineSensor.when_line = on_line
LineSensor.when_no_line = off_line


# Example usage
try:
   while True:
        motor_A(True, 50)  # Kører fremad 50% speed
        motor_B(True, 50)
        sleep(0.1)        
        
except Exception as c:
    print('Program stopped by user.')
finally:
    full_stop()  
    #Sikre os at motoren også stopper