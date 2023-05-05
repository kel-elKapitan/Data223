# Game that utilises the pokemon API

# Import modules
import pandas as pd
import requests
import random
import json

# Functions needed to run the main driver code
def get_pokemon_id(name):
	response= requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}') 
    	pokemon_data=response.json() 
    	id=pokemon_data['id'] 
    	return id

def get_pokemon_details(id):
    	response= requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}') 
	pokemon_data=response.json() 
    	id=pokemon_data['id'] 
    	name=pokemon_data['name']

    # to retieve the base stat of HP, attack and defence
	for key in pokemon_data['stats']: 
        
        	for value in key.items():
            	if key['stat']['name'] == 'hp':
                	HP = key['base_stat']
                
            	elif key['stat']['name'] == 'attack':
                	attack = key['base_stat']
                
            	elif key['stat']['name'] == 'defense':
                	defense = key['base_stat']   
    
        	types=[t['type']['name']for t in pokemon_data['types']]  

	pokemon_details={'id':id, 'name':name, 'HP': HP, 'attack': attack, 'defence': defense, 'types':types}
	return pokemon_details


# Function to get attack modifiers


def attack_mod(p1, p2):
    
    	p1_name = p1.get('name')
    	p2_name = p2.get('name')
    
    	p1_id = p1.get('id')
    	p2_id = p2.get('id')
    
    	p1_types = p1.get('types')
    	p2_types = p2.get('types')

    	p1_attack = p1.get('attack')
    	p2_attack = p2.get('attack')

	p1_hp = p1.get('HP')
    	p2_hp = p2.get('HP')
	p1_defense = p1.get('defence')
	p2_defense = p2.get('defence')
  



    # Grass type Attack modifier
	if 'grass' in p1_types and 'normal' in  p2_types:
        	pass
        	# no attack modifier needed
    	elif 'grass' in p1_types and 'fire' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack * 2
	elif 'grass' in p1_types and 'water' in p2_types:
        	p1_attack = p1_attack * 2
        	p2_attack = p2_attack / 2
	elif 'grass' in p1_types and 'electric' in p2_types:
		p2_attack = p2_attack / 2 
        
	elif 'grass' in p1_types and 'grass' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack / 2
        
	elif 'grass' in p1_types and 'ice' in p2_types:
        	p2_attack =- p2_attack * 2
        
	elif 'grass' in p1_types and 'fightiing' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'grass' in  p1_types and 'poison' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack * 2
        
	elif 'grass' in p1_types and 'ground' in p2_types:
        	p1_attack = p1_attack * 2
        	p2_attack = p2_attack / 2
        
	elif 'grass' in p1_types and 'flying' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack * 2
        
	elif 'grass' in p1.get('types') and 'pychic' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'grass' in p1_types and 'bug' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack * 2
        
	elif 'grass' in p1_types and 'rock' in p2_types:
        	p1_attack = p1_attack * 2
        
	elif 'grass' in p1_types and 'ghost' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'grass' in p1_types and 'dragon' in p2_types:
        	p1_attack = p1_attack / 2
        
	elif 'grass' in p1_types and 'dark' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'grass' in p1_types and 'steel' in p2_types:
    		p1_attack = p1_attack / 2
       
	elif 'grass' in p1_types and 'fairy' in p2_types:
        	pass
        	# no attack modifier needed


	# Normal type Attack modifier
	if 'normal' in p1_types and 'normal' in  p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'fire' in p2_types:
        	pass
	elif 'normal' in p1_types and 'water' in p2_types:
        	pass
	elif 'normal' in p1_types and 'electric' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'ice' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'fightiing' in p2_types:
        	p2_attack = p2_attack * 2 
	elif 'normal' in  p1_types and 'poison' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'ground' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'flying' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1.get('types') and 'pychic' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'bug' in p2_types:
        	pass
	# no attack modifier needed
   	elif 'normal' in p1_types and 'rock' in p2_types:
        	p1_attack = p1_attack / 2
    	elif 'normal' in p1_types and 'ghost' in p2_types:
        	p1_attack = 0
        	p2_attack = 0
	elif 'normal' in p1_types and 'dragon' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'dark' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'normal' in p1_types and 'steel' in p2_types:
        	p1_attack = p1_attack / 2
	elif 'normal' in p1_types and 'fairy' in p2_types:
        	pass
        	# no attack modifier needed


	# Fire type Attack modifier
	if 'fire' in p1_types and 'fire' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack / 2
	elif 'fire' in p1_types and 'water' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack / 2
	elif 'fire' in p1_types and 'electric' in p2_types:
        	pass
	elif 'fire' in p1_types and 'ice' in p2_types:
        	p1_attack = p1_attack * 2
        	p2_attack = p2_attack / 2
	elif 'fire' in p1_types and 'fightiing' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'fire' in  p1_types and 'poison' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'fire' in p1_types and 'ground' in p2_types:
        	p2_attack = p2_attack * 2
        
	elif 'fire' in p1_types and 'flying' in p2_types:
        	pass 
        	# no attack modifier needed
	elif 'fire' in p1.get('types') and 'pychic' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'fire' in p1_types and 'bug' in p2_types:
        	p1_attack = p1_attack * 2
        	p2_attack = p2_attack / 2
	elif 'fire' in p1_types and 'rock' in p2_types:
        	p1_attack = p1_attack / 2
        	p2_attack = p2_attack * 2
	elif 'fire' in p1_types and 'ghost' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'fire' in p1_types and 'dragon' in p2_types:
        	p1_attack = p1_attack / 2
	elif 'fire' in p1_types and 'dark' in p2_types:
        	pass
        	# no attack modifier needed
	elif 'fire' in p1_types and 'steel' in p2_types:
        	p1_attack = p1_attack * 2
        	p2_attack = p2_attack / 2
	elif 'fire' in p1_types and 'fairy' in p2_types:
        	p2_attack = p2_attack / 2


    	# package p1 and p2 into dictionaries exactly like the input dictionaries
	p1 = {'id': p1_id, 'name': p1_name, 'attack': p1_attack, 'HP': p1_hp, 'defense': p1_defense, 'type': p1_types }
	p2 = {'id': p2_id, 'name': p2_name, 'attack': p2_attack, 'HP': p2_hp, 'defense': p2_defense, 'type': p2_types }
	

	return p1, p2

def get_random_pokemon_id():
	return random.randint(1,1021)

def pokenames_id():
	response_2 = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")
	response_dict_2 = response_2.json()
	results = response_dict_2['results']
	names = []
	for items in results:
		names.append(items['name'])

	pokemon = pd.DataFrame(names)
	pokemon.index += 1
	pokemon.columns =['Names']
	return pokemon


# THE FIGHT FUNCTION

def fight(pokemon_1, pokemon_2):
	pokemon_2['health'] = pokemon_2['HP'] + pokemon_2['defense']
	pokemon_1['health'] = pokemon_1['HP'] + pokemon_1['defense']

	while pokemon_1['health'] > 0 and pokemon_2['health'] > 0:
		pokemon_2['health'] = pokemon_2['health'] - pokemon_1['attack']
		if pokemon_2['health'] > 0:
			print(f"{pokemon_2['name']} has {pokemon_2['health']}HP left")
		elif pokemon_2['health'] <= 0:
			print(pokemon_2['name'] + ' is on 0HP and unable to battle. Therefore, ' + pokemon_1['name'] + ' wins!')
			break

		pokemon_1['health'] = pokemon_1['health'] - pokemon_2['attack']
		if pokemon_1['health'] > 0:
			print(f"{pokemon_1['name']} has {pokemon_1['health']}HP left")
		elif pokemon_1['health'] <= 0:
			print(pokemon_1['name'] + ' is 0HP and unable to battle. Therefore, ' + pokemon_2['name'] + ' wins!')
			break


def choose_pokemon():
	df = pokenames_id()
	print("Please enter your pokemon name: ")
        print('-------------------------------------------------------')
        p1_name = input()
        p1_random = get_random_pokemon_id()
        cpu_random = get_random_pokemon_id()
        p2_random = get_random_pokemon_id()

	# get the id number from the pokemon name
        if p1_name in df['Names'].values:
		id = get_pokemon_id(p1_name)
		print(f"Your pokemon name is: {p1_name}. Your pokemon ID is: {id}")
		p1 = get_pokemon_details(id)
		print("Your pokemon stats are: ")
		print(p1)
		print('-------------------------------------------------------')

	else:
		print("Pokemon does not exist! Randomly selecting.")
		print('-------------------------------------------------------')
		print(f"Your pokemon ID is: {p1_random}")
		p1 = get_pokemon_details(p1_random)
		print("Your pokemon stats are: ")
		print(p1)
		print('-------------------------------------------------------')
	return p1


# Driver code
print("Welcome to Pokemon Text Battle!")
print('-------------------------------------------------------')

print("Would you like to enter the game? (y/n)")
answer = input()
if answer == 'y':
	# ask for input for single or two players
	print('-------------------------------------------------------')
	print("Please choose from the following options:")
	print('-------------------------------------------------------')
	print("1. Single player")
	print("2. Two players")
	players = input()
	if players == '1':
        # create a single player game

        # call function to create a pokemon for each player

        print('-------------------------------------------------------')
        print("Welcome to Single Player Mode!")
        print('-------------------------------------------------------')
        p1 = choose_pokemon()

        p2 = get_pokemon_details(get_random_pokemon_id())
        print('-------------------------------------------------------')
        print("Fighting against: " + p2['name'])
        print('-------------------------------------------------------')

elif players == '2':
        print('-------------------------------------------------------')
        print("Welcome to Two Player Mode!")
        print('-------------------------------------------------------')
        print("Player 1!")
        p1 = choose_pokemon()

        print('-------------------------------------------------------')
        print("Player 2!")
        p2 = choose_pokemon()

else:
        print("Nope. Start game again...")
        quit()

# adjust the stats of each pokemon if appropriate
    
p1, p2 = attack_mod(p1, p2)
    
# call the fight function
fight(p1, p2)

print('Thank you for playing!')



else:
	answer == 'n'
	print('-------------------------------------------------------')
	print("GAME OVER.....")
	quit()



