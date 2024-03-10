#!/bin/python

# 0. install:
# sudo apt install lm-sensors
# sudo sensors-detect --auto

import re
import os
import numpy as np

bash_comand = r'sensors | grep "^Core\s[[:digit:]]\+:"'
command = os.popen(bash_comand)
temperature_sring = command.read()
command.close()

temperature_predicat = re.compile(r'\+\d{1,3}\.\d{1}°C\s')
temperature_sring_list = temperature_predicat.findall(temperature_sring)

temperature_list = []
for i in temperature_sring_list:
    temp = re.sub(r'\+|°C', '', i)
    temperature_list.append(float(temp))

current_temperature = '+' + str(np.array(temperature_list).mean()) + '°C'
print(current_temperature)
