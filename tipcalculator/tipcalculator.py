import sys
import time

try:
    # create user inputs for the bill and tip
    bill = float(input('Input bill here: '))
    tippercent = int(input('Input tip percent here: '))

    # create variables total, bill & tip
    # bill is a float variable whilst the tip percent is an int variable

    # calculates the total
    total = bill + float(tippercent/100 * bill)

    print('Please wait...')
    time.sleep(1.5)

    # prints the f string of total after user has input data
    print(f'This will cost a total of ${total}.')

except Exception:
    e = sys.exc_info()[1]
    print('Oops, an error occured! Please try again! Error: ' + e.args[0])
