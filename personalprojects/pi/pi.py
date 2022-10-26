from mpmath import mp

mp.dps = 1000000
pi = mp.pi

with open('personalprojects/pi/pi.txt', 'w') as file:
    file.write(str(pi))