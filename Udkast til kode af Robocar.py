




import gpiozero as gz # Vigtigt modul for at interagere med Raspberry Pi's hardware (motorer, sensorer)
import asyncio # Nyttig til samtidige opgaver som at styre motorer og aflæse sensorer samtidigt.
from time import sleep #God til når vi skal bruge pauser og delays


#import gamepad - hvis vi vil have en remote control på
#ussensor: Vigtigt til forhindringsdetektion og autonom kørsel. -  ikke nødvendig med RPi.GPI0
#motor_control: Ansvarlig for at styre motorerne i RoboCar - ikke nødvendig med RPi.GPI0


#Pins for vores motor kontrol (H-bro TB6612FNG)
MotorA1 = 11 #motor a input 1
MotorA2 = 10  #motor a input 2
PWMA = 23 #motor a pwm
Motor2B1= 12  #motor b input 1
Motor2B2= 13  #motor b input 2
PWMB = 26 #motor b pwm

#Pins for HC SR04 (ultrasonic sensor)
TRIG = 4
ECHO = 5

#GPIO setup
gz.setmode (gz.BCM)
gz.setup (MotorA1,gz.OUT)
gz.setup (MotorA2, gz.OUT)
gz.setup (PWMA, gz.OUT)
gz.setup (Motor2B1, gz.OUT)
gz.setup (Motor2B2, gz.OUT)
gz.setup (PWMB, gz.OUT)
gz.setup (TRIG, gz.OUT)
gz.setup (ECHO, gz.IN) #Hvorfor skal den være in

def motor_A(forward, speed): #Til bagdæk
    if forward:
        gz.output(MotorA1, gz.HIGH)
        gz.output(MotorA2, gz.LOW)

    else:
        gz.output(MotorA1, gz.LOW)
        gz.output(MotorA2, gz.HIGH)
    PWMA.ChangeDutyCycle(speed)


def motor_B(forward, speed): #Til fordæk
    if forward:
        gz.output(Motor2B1, gz.HIGH)
        gz.output(Motor2B2, gz.LOW)

    else:
        gz.output(Motor2B1, gz.LOW)
        gz.output(Motor2B2, gz.HIGH)
    PWMB.ChangeDutyCycle(speed)

def full_stop ():
    PWMA.ChangeDutyCycle(0)
    PWMB.ChangeDutyCycle(0)
    










#async def kørfrem ():
