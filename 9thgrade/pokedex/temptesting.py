#File Two: You will be receiving user input and filtering the list based on
#Pokemon type. Your program must have error handling if the type is not
#found. All pokemon matching the given type must be printed on separate
#lines. Your program should contain the following
#-Accept user input for a type
#-develop a function that accepts a type parameter
#-iterate through the pokemon data and find pokemon matching the type
#-if no pokemon is found let the user know
import sys
import json
import time
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedexData = json.load(pokedex)


print('What pokemon type do you want to filter by?')
print('''Choose from Normal, Fire, Water, Grass, Flying, Fighting, Poison, Electric,
Ground, Rock, Psychic, Ice, Bug, Ghost, Steel, Dragon, Dark, and Fairy.''')
userinput = input('Enter Type Here: ')

# function to return key for any value
def get_key(val):
	for key, value in my_dict.items():
		if val == value:
			return key

	return "key doesn't exist"


# Driver Code
my_dict = {"Java": 100, "Python": 112, "C": 11}

print(get_key(100))
print(get_key(11))
