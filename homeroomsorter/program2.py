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

# sorts into 3 homerooms based on the first initial of last name
if first_initial_of_last_name.lower() in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
    homeroom = 101
elif first_initial_of_last_name.lower() in ('h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'):
    homeroom = 102
else:
    homeroom = 103

# prints the result
print (f'You are in homeroom: {homeroom}. Thanks for using the homeroom sorter!')
