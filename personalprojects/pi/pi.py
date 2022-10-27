try:
     # import version included with old SymPy
     from sympy.mpmath import mp
except ImportError:
     # import newer version
     from mpmath import mp

mp.dps = 1000  # set number of digits
balls = mp.pi

with open('C:/Users/Shatterdest/Desktop/pi', 'w') as file:
    file.write(balls)# print pi to a thousand places