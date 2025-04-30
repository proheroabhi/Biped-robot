# Bluetooth-Controlled Biped Robot with Obstacle Avoidance

This project is a **Python-based robotic system** that emulates a biped robot capable of walking, detecting obstacles, and receiving movement commands via Bluetooth. The robot uses **ultrasonic sensors, IR sensors, servo motors**, and a **DHT11 sensor** to navigate and monitor its environment. The entire system runs on a **Raspberry Pi**, making it a compact and programmable IoT solution.
-----
## 🔧 Features

- **Bluetooth control** for movement commands (e.g., forward, backward, left, right)
- **Obstacle detection** using an ultrasonic sensor
- **IR-based edge detection** to avoid falls
- **Temperature & humidity monitoring** via DHT11 sensor
- **Servo-controlled biped walking mechanism**
- **Failsafe behavior** to stop on command loss or obstacle detection
-----
## 🧠 Technologies & Libraries

- **Python 3**
- **RPi.GPIO** – GPIO pin control
- **adafruit-circuitpython-dht** – DHT11 temperature/humidity sensor
- **bluedot** – Bluetooth communication
- **gpiozero** – High-level GPIO device support
- **pyserial** – Serial communication (optional)
---
## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/biped-robot-python.git
   cd biped-robot-python
   ```
2. Set up a Python virtual environment (optional but recommended):
  ```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
----
## 📁 Project Structure
biped-robot-python/   
├── biped_robot.py           # Main Python script for robot control   
├── requirements.txt         # Project dependencies    
└── README.md                # Project documentation  
-----
## 🛠️ Hardware Requirements
* Raspberry Pi (tested on Pi 4)
* 7 Servo Motors (for leg control)
* Ultrasonic Sensor (e.g., HC-SR04)
* IR Sensors (x2)
* DHT11 Sensor
* Bluetooth Module (e.g., HC-05 or internal Pi Bluetooth)
* Breadboard, jumper wires, external power for motors
----
## 📲 Bluetooth Command Mapping
Command	Action   
F	      Move Forward   
B	      Move Backward   
L	      Turn Left    
R	      Turn Right   
S	      Stop   
You can send commands using a Bluetooth terminal app from your smartphone or a serial monitor.
----
## ⚠️ Safety Notes
* Ensure servos are powered externally to prevent Pi reboots.
* Use voltage dividers or level shifters for sensors if needed.
* Run on a flat surface to avoid tipping over.
-----
## 📸 Demo & Results
[! demo1](Gallery/Robo-1.jpg)
[! demo2](Gallery/Robo-2.jpg)

----
## 🤝 Contributing

Contributions are welcome and appreciated! If you have suggestions for improvements, bug fixes, or new features, feel free to fork the repository and submit a pull request.
-----
### Steps to Contribute:
1. Fork the project repository.
2. Create your feature branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes: `git commit -m 'Add your message here'`
4. Push to the branch: `git push origin feature/YourFeatureName`
5. Open a pull request.

Please ensure your code adheres to the existing style and includes relevant documentation or comments. Let's make robotics development more accessible together!

----
## 🧑‍💻 Authors
-> Abhinav Jain – Technical Lead & Developer
----
## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
-----
## 🚀 Final Words

This project demonstrates how powerful and accessible robotics can be when paired with Python and Raspberry Pi. Whether you're a student, hobbyist, or enthusiast, we hope this serves as a solid foundation for your own bipedal or autonomous robot adventures. Feel free to expand on it, innovate, and make it your own — the possibilities are endless!

Happy Building! 🤖✨
----
