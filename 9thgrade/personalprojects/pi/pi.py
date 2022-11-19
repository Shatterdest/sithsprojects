import time
from mpmath import mp


input = input('How many digits of pi do you want? ')
mp.dps = int(input)
st = time.time()# set number of digits
balls = mp.pi

with open('C:/Users/Shatterdest/Documents/GitHub/sithsprojects/9thgrade/personalprojects/pi/pi.txt', 'w') as file:
    file.write(str(balls))# print pi to a thousand places

et = time.time()

tt = et-st

print(f'Time took: {tt}')
