import time
import RPi.GPIO as GPIO
from gpiozero import Servo
import serial
from Adafruit_DHT import DHT11

# Bluetooth setup (using pySerial for simplicity, PyBluez can be used for advanced Bluetooth communication)
bluetooth = serial.Serial("/dev/ttyAMA0", 9600)  # Set your correct Bluetooth port

# Pin assignments for servos
RhipPin = 12
LhipPin = 15
RkneePin = 14
LkneePin = 13
RtoePin = 2
LtoePin = 4
UltraPin = 33

# Ultrasonic sensor pins
trigPin = 32
echoPin = 35
obstaclePin = 22

# Initialize servo objects (gpiozero Servo objects or PWM control)
Rhip = Servo(RhipPin)
Lhip = Servo(LhipPin)
Rknee = Servo(RkneePin)
Lknee = Servo(LkneePin)
Rtoe = Servo(RtoePin)
Ltoe = Servo(LtoePin)

# Initialize ultrasonic sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(obstaclePin, GPIO.IN)

# Initialize temperature sensor (DHT11)
sensor = DHT11(pin=23)

# Servo positions and flags
RhipPPos = 1350
LhipPPos = 1400
RkneePPos = 1500
LkneePPos = 1200
RtoePPos = 1250
LtoePPos = 1300
delayno = 0.02  # Delay time

# Utility functions
def calculate_distance():
    GPIO.output(trigPin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)
    duration = GPIO.input(echoPin)
    distance = (duration * 0.0343) / 2
    return distance

def temperature():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, 23)
    if humidity is not None and temperature is not None:
        bluetooth.write(f"Temperature: {temperature}C Humidity: {humidity}%".encode())
    else:
        bluetooth.write("Failed to retrieve data from sensor".encode())

def irsense():
    if GPIO.input(obstaclePin) == GPIO.HIGH:
        bluetooth.write("Stop! No ground detected.".encode())
    else:
        bluetooth.write("Path is clear.".encode())

def forward():
    # Simulate servo movement for walking forward
    Rhip.value = 1  # Right hip forward
    Lhip.value = -1  # Left hip forward
    time.sleep(delayno)

def backward():
    # Simulate servo movement for walking backward
    Rhip.value = -1  # Right hip backward
    Lhip.value = 1  # Left hip backward
    time.sleep(delayno)

def turn_left():
    # Simulate turning left (use specific movement pattern)
    Rhip.value = -1
    Lhip.value = 1
    time.sleep(delayno)

def turn_right():
    # Simulate turning right (use specific movement pattern)
    Rhip.value = 1
    Lhip.value = -1
    time.sleep(delayno)

def sonar():
    distance = calculate_distance()
    if distance <= 10:
        backward()
        backward()

def getup():
    # Simulate getting up (servo positions should change according to real logic)
    pass

# Main loop to handle incoming Bluetooth commands
def main():
    while True:
        if bluetooth.in_waiting:
            data_in = bluetooth.read()
            if data_in == b'F':
                forward()
            elif data_in == b'B':
                backward()
            elif data_in == b'L':
                turn_left()
            elif data_in == b'R':
                turn_right()
            elif data_in == b'U':
                sonar()
            elif data_in == b'T':
                temperature()
            elif data_in == b'I':
                irsense()

if __name__ == "__main__":
    main()
