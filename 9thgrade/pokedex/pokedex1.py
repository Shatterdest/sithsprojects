import json
import time
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedexData = json.load(pokedex)

count = 1
newline = '\n'
try:
    delay = float(input('How long do you want the delay between each pokemon be? (There are 809 Pokemon.) : '))
    for entry in range(len(pokedexData)):
        print(f'''Pokemon #{count}:
    English Name: {pokedexData[entry]["name"]["english"]}
    Japanese Name: {pokedexData[entry]["name"]["japanese"]}
    Chinese Name: {pokedexData[entry]["name"]["chinese"]}
    French Name: {pokedexData[entry]["name"]["french"]}''')
        print('')
        count = count + 1
        time.sleep(delay)
except:
    print("Try reentering the delay, and make sure it's a number. Thanks!")