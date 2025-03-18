# HTS221-Sensor-Recordings
Adafruit HTS221 - Temperature &amp; Humidity Sensor Breakout Board .txt recording 

This program record temperature and humidity with the Adafruit HTS221 Breakout Board and Raspberry Pi 4b. 
It will create a .txt file with a record of the sample time, temperature, and humidity. The resulting file is excel (and similar programs) compatable for analysis.

Required Hardware:
  - Adafruit HTS221 Board: https://www.adafruit.com/product/4535
  - Raspberry Pi (or similar pi)
  - QT Cable OR Wire (28 AWG, Breadboard wires)


# If Adafruit Blinka and/or CircuitPython are NOT installed:
*Please note this commands may download packages that may break you Raspberry Pi and it is not considered best practice. I chose to install the packages this way so I could use Thonny and not the Termal. Continue with caution!

Step 0.5:
In the termal write:
- pip install --break-system-packages adafruit-blinka
Next write:
- pip install --break-system-packages adafruit-circuitpython-hts221

# If Adafruit Blinka AND CircuitPython ARE installed:

Step 1: 
Download the HTS221_sensor.py file. Create a new file and move the file into it. The sensor output files will be located in this folder.

Step 2: 
Connect the sensor to the Pi. Follow the Adafruit wiring guild at:
  https://learn.adafruit.com/adafruit-hts221-temperature-humidity-sensor/python-circuitpython
If the green light is on, then the board is getting power.

Step 3: 
Open the HTS221_sensor.py in your prefered editer, I like Thonny (native to the pi). 

Step 4:
Click Run! The sensor will print data on the screen and record the data in a .txt file located in the same folder as the program.
The program will end ether by CTRL+C or the specified time found in the while loop.

# To Change the End Time of the Sensor
Step 1:
Locate the while loop on line 46.
Step 2:
Change the number at the end to one of your choising. Format your number in military time and use the format "Hour.Minute".





