import json
import sys
import time
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedexData = json.load(pokedex)

try: 
    userinput = input('Enter Pokemon Name Here: ')
    language = input('What language are you entering it as? (English, Japanese, Chinese, French) ')

    def findPokemon(pokemonName):
        for entry in range(len(pokedexData)):
            if pokemonName.capitalize() in pokedexData[entry]["name"][language.lower()]:
                print(f'The Pokemon Name you entered was: {pokemonName}.')
                time.sleep(1)
                print(f'''The Pokemon's names in other languages are:
    English Name: {pokedexData[entry]["name"]["english"]}
    Japanese Name: {pokedexData[entry]["name"]["japanese"]}
    Chinese Name: {pokedexData[entry]["name"]["chinese"]}
    French Name: {pokedexData[entry]["name"]["french"]}''')
                time.sleep(2.5)
                print(f'''The Pokemon's type(s) are: 
    {', '.join(pokedexData[entry]["type"])}''')
                print(f'''The Pokemon's stats are: 
    {pokedexData[entry]["base"]["HP"]} HP,
    {pokedexData[entry]["base"]["Attack"]} Attack,
    {pokedexData[entry]["base"]["Defense"]} Defense,
    {pokedexData[entry]["base"]["Sp. Attack"]} Special Attack,
    {pokedexData[entry]["base"]["Sp. Defense"]} Special Defense, and
    {pokedexData[entry]["base"]["Speed"]} Speed.''')

    findPokemon(userinput)

except:
    e = sys.exc_info()[1]
    print('Oops, an error probably occured, try entering another Pokemon name!: ' + e.args[0])
