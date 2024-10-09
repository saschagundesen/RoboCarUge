




import RPi.GPIO as GPIO # Vigtigt modul for at interagere med Raspberry Pi's hardware (motorer, sensorer)
import asyncio # Nyttig til samtidige opgaver som at styre motorer og aflæse sensorer samtidigt.
from time import sleep #God til når vi skal bruge pauser og delays


#import gamepad - hvis vi vil have en remote control på
#ussensor: Vigtigt til forhindringsdetektion og autonom kørsel. -  ikke nødvendig med RPi.GPI0
#motor_control: Ansvarlig for at styre motorerne i RoboCar - ikke nødvendig med RPi.GPI0


#Pins for vores motor kontrol (H-bro TB6612FNG)
MotorA1 = 17 #motor a input 1
MotorA2 = 17  #motor a input 2
PWMA = 17 #motor a pwm
Motor2B1= 17  #motor b input 1
Motor2B2= 17  #motor b input 2
PWMB = 17 #motor b pwm

#Pins for HC SR04 (ultrasonic sensor)
TRIG = 5
ECHO = 6

#GPIO setup
GPIO.setmode (GPIO.BCM)
GPIO.setup (MotorA1, GPIO.OUT)
GPIO.setup (MotorA2, GPIO.OUT)
GPIO.setup (PWMA, GPIO.OUT)
GPIO.setup (Motor2B1, GPIO.OUT)
GPIO.setup (Motor2B2, GPIO.OUT)
GPIO.setup (PWMB, GPIO.OUT)
GPIO.setup (TRIG, GPIO.OUT)
GPIO.setup (ECHO, GPIO.IN) #Hvorfor skal den være in

def motor_A(forward, speed): #Til bagdæk
    if forward:
        GPIO.output(MotorA1, GPIO.HIGH)
        GPIO.output(MotorA2, GPIO.LOW)

    else:
        GPIO.output(MotorA1, GPIO.LOW)
        GPIO.output(MotorA2, GPIO.HIGH)
    PWMA.ChangeDutyCycle(speed)


def motor_B(forward, speed): #Til fordæk
    if forward:
        GPIO.output(Motor2B1, GPIO.HIGH)
        GPIO.output(Motor2B2, GPIO.LOW)

    else:
        GPIO.output(Motor2B1, GPIO.LOW)
        GPIO.output(Motor2B2, GPIO.HIGH)
    PWMB.ChangeDutyCycle(speed)

def full_stop ():
    PWMA.ChangeDutyCycle(0)
    PWMB.ChangeDutyCycle(0)
    










#async def kørfrem ():
