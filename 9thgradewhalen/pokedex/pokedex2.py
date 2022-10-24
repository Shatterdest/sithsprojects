import sys
import json
import time
## Open the JSON file of pokemon data
pokedex = open("9thgradewhalen/pokedex/pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedexData = json.load(pokedex)

try: 
    print('What pokemon type do you want to filter by?')
    print('''Choose from Normal, Fire, Water, Grass, Flying, Fighting, Poison, Electric,
Ground, Rock, Psychic, Ice, Bug, Ghost, Steel, Dragon, Dark, and Fairy.''')
    userinput = input('Enter Type Here: ')
    language = input('What language do you want the Pokemon name to be? (English, Japanese, Chinese, French): ')
    delay = float(input('How long do you want the delay between each Pokemon be? (There are 809 Pokemon in this Pokedex): '))
    sortedPokemon = 0


    def sortpokemon(pokemonType):
        count = 1
        for entry in range(len(pokedexData)):
            pokemonTypes = pokedexData[entry]["type"]
            pokemonName = pokedexData[entry]["name"][language.lower()]
            if pokemonType.capitalize() in pokemonTypes:
                print(f'''{pokemonType} Pokemon #{count}: {pokemonName}!''')
                global sortedPokemon
                sortedPokemon = sortedPokemon + 1
                time.sleep(delay)
                count = count + 1
        if sortedPokemon == False:
            print('We could not find a Pokemon of the type you mentioned. Sorry!')

    sortpokemon(userinput)

except:
    e = sys.exc_info()[1]
    print('The Type you entered did not match any Pokemon! Sorry! If you did enter a valid type, an error probably occured: ' + e.args[0])
