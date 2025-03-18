# Documentation: https://docs.circuitpython.org/projects/hts221/en/latest/api.html
# GitHub: jacks-somewhere

#imports
import time
from datetime import date
import board
import adafruit_hts221

#Sets up board and Sensor
i2c = board.I2C()  # uses board.SCL and board.SDA
hts = adafruit_hts221.HTS221(i2c)
data_rate = adafruit_hts221.Rate.label[hts.data_rate]

ReadList = []
today = date.today()

def loop():
    #Gets Sensor Data and converts it to the correct formating
    temperature = ((hts.temperature * 9/5) + 32)
    relative_humidity = hts.relative_humidity
    hour = int(time.strftime('%H'))
    minute = int(time.strftime('%M'))
    current_time = f'{hour:02d}:{minute:02d}'
    
    #Adds Data to the list
    ReadList.append(f'{current_time},{hts.relative_humidity:.2f},{hts.temperature:2f}')
    print(f'Current Time: {hour:02d}:{minute:02d}')
    print(f'Temperature: {temperature:.2f}')
    print(f'Relative_humidity: {relative_humidity:.2f}% rH')

#Opens a File and writes the Data
def write_file(file_name):
    with open(file_name, 'a') as data_file:
        data_file.write('\n'.join(ReadList)+'\n')
    data_file.close()
    ReadList.clear()
     
def write_file_heading(file_date, file_name):
    data_file = open(file_name,'a')
    data_file.write(f'{file_date}\n')
    
def main():
    file_date = (today.strftime('%m-%d-%Y'))
    file_name = f'hts221_{file_date}.txt'
    write_file_heading(file_date,file_name)
    #Checks the time and stops if it reaches a specific hour (military time)
    while int(time.strftime('%H.%M')) <= 13: 
        loop()
        write_file(file_name)
        time.sleep(3) #Waits (blank) seconds before starting the loop again
  
if __name__ == "__main__":
	main()




