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
data_rate = adafruit_hts221.Rate.ONE_SHOT

#Stores Data temporarily
ReadList = []
today = date.today()

def loop():
    take_measurements()
    #Gets Sensor Data and converts it to the correct formating
    temperature = float(f'{(hts.temperature * 9/5) +32:.2f}')
    relative_humidity = float(f'{hts.relative_humidity:.2f}')
    hour = int(time.strftime('%H'))
    minute = int(time.strftime('%M'))
    current_time = f'{hour:02d}:{minute:02d}'
    
    #Adds Data to the list
    ReadList.append(f'{current_time},{hts.relative_humidity:.2f},{hts.temperature * 9/5: +32:.2f}')

#Opens a File and writes the Data
def write_file(file_name):
    #Opens file to add to it
    with open(file_name, 'a') as data_file:
        data_file.write('\n'.join(readingslist)+'\n')
    data_file.close()
    readingslist.clear() #Clears the List to prevent multi entries
     
def write_file_heading(file_date, file_name):
    data_file = open(file_name,'a')
    data_file.write(f'{file_date}\n')
    
def main():
    file_date = (today.strftime('%m-%d-%Y'))
    file_name = f'hts221_{file_date}.txt'
    write_file_heading(file_date,file_name)
    #Checks the time and stops if it reaches a specific hour (military time)
    while int(time.strftime('%H')) < 7: 
        loop()
        write_file(file_name)
        time.sleep(180) #Waits (blank) seconds before starting the loop again
  

if __name__ == "__main__":
	main()



