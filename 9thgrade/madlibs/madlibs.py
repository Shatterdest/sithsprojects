new_line = '\n'
# creating variables representing verbs, nouns, adjectives, etc. 
# user input is also recieved and assigned to the variables

verb1 = input('Enter Verb 1 here: ')
verb2 = input('Enter Verb 2 here: ')
noun1 = input('Enter Noun 1 here: ')
number1 = input('Enter Number here: ')
number2 = input('Enter Another Number here: ')
celebrity_guest = input('Enter Celebrity Guest here: ')
name1 = input('Enter Name here: ')
sport1 = input('Enter Sport here: ')
adjective = input('Enter Adjective 1 here: ')

# created variable "madlib" with f-string that tells a story 
# using variables from step 1

madlib = (f'One day, I {verb1.lower()} to school. My first class was with my friend {name1.capitalize()}. We had {noun1.lower()} class. {new_line}It was very {adjective.lower()}. However, our next class, Gym, was also very interesting. {new_line}We got to play volleyball with {celebrity_guest.capitalize()}. The score was {number1} to {number2}. At the end of the {new_line}day, I played {sport1.capitalize()} with my friend. After, I went home and did my favorite {new_line}activity, which is to {verb2.lower()}')

# prints the f string after recieving user input data

print(madlib)
