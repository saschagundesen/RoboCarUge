#import asyncio # Nyttig til samtidige opgaver som at styre motorer og aflæse sensorer samtidigt.
from time import sleep #God til når vi skal bruge pauser og delays

import gpiozero as gz

#Set up the pin factory
gz.PinFactory(pi=gz.pi_gpio, pin_class=gz.RPiGPIODevice)

#Define the pins
MotorA1 = 11
MotorA2 = 10
PWMA = 23

Motor2B1 = 12
Motor2B2 = 13
PWMB = 26

TRIG = 4
ECHO = 5

#Set up the pins as outputs or inputs
gz.setup(MotorA1, gz.OUT)
gz.setup(MotorA2, gz.OUT)
PWMA_pwm = gz.PWMOutputDevice(PWMA)


gz.setup(Motor2B1, gz.OUT)
gz.setup(Motor2B2, gz.OUT)
PWMB_pwm = gz.PWMOutputDevice(PWMB)

gz.setup(TRIG, gz.OUT)
gz.setup(ECHO, gz.IN)

#Define the motor functions
def motor_A(forward, speed):
    if forward:
        gz.output(MotorA1, gz.HIGH)
        gz.output(MotorA2, gz.LOW)
    else:
        gz.output(MotorA1, gz.LOW)
        gz.output(MotorA2, gz.HIGH)
    PWMA_pwm.value = speed / 100.0  # Set the duty cycle

def motor_B(forward, speed):
    if forward:
        gz.output(Motor2B1, gz.HIGH)
        gz.output(Motor2B2, gz.LOW)
    else:
        gz.output(Motor2B1, gz.LOW)
        gz.output(Motor2B2, gz.HIGH)
    PWMB_pwm.value = speed / 100.0  # Set the duty cycle

def full_stop():
    PWMA_pwm.value = 0
    PWMB_pwm.value = 0