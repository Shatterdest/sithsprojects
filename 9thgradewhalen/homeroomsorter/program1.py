import time

print('Welcome to the homeroom sorter!')
time.sleep(1.7)
print('We just need your last name, and we will sort you into a homeroom!')
time.sleep(2.5)


# recieve user input of last name, sets it as variable
last_name = input('What is your last name? ')
print('Thanks! We are sorting you into a homeroom now. Please wait...')
time.sleep(4)

# extracts first letter of last name, and sets it as the first initial
first_initial_of_last_name = last_name[0]

# Checks the first initial of last name, and sorts it into 
# a homeroom based on what it is.
if first_initial_of_last_name.lower() == 'a':
    homeroom = '101'
elif first_initial_of_last_name.lower() == 'b': 
    homeroom = '102'
else:
    homeroom = '103'

# prints the result based on the last name input
print (f'You are in homeroom: {homeroom}. Thanks for using the homeroom sorter!')
