import os
import time
import gpiozero
from time import sleep
from datetime import datetime
from gpiozero import CPUTemperature

file = open("/media/usb/data_log_04252020.csv", "a")
i = 0
if os.stat("/media/usb/data_log_04252020.csv").st_size == 0:
    file.write("Date, Time, Reading\n")
while True:
    i = i+1
    date_now = datetime.today().date()
    current_time = time.strftime('%H:%M:%S', time.localtime())
    temperature = CPUTemperature()
    file.write(str(date_now)+","+str(current_time) +
               ","+str(temperature.temperature)+"\n")
    file.flush()
    time.sleep(5)
file.close()
