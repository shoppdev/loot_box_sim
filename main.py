# IMPORTS
import pickle
import os
import random
from player import Player
from lootbox import LootBox

# VARS
player = None
path_start = 'files/bin/'

        
# ////// FUNCTIONS ///////

# this gets player name input and checks to see if save exists
def check_for_player():
    player_name = input("What is your player name? (Use same name to continue game) ")
    file_path = path_start + player_name

    # check for file
    if os.path.isfile(file_path):
        return player_load(player_name, file_path)
    else:
        return player_create(player_name, file_path)

# loads in the player object. should contain all info needed to play. ie inventory and trade status
def player_load(player_name, path):
    print('Loading your save')
    with open(path, 'rb') as player_save:
        player = pickle.load(player_save)
    return player

# creates a new player if save not found
def player_create(player_name, path):
    print("Creating new player. Prepare for the fun")
    player = Player(player_name)
    player_save(path, player)
    return player

# saves player file, nothing returned
def player_save(path, player):
    with open(path, 'wb') as file:
        pickle.dump(player, file)

# just to make one thing easier
def get_path():
    return path_start + player.name


## MAIN LOOP ##
# Starts the game asking for player
player = check_for_player()

# make a loot box and see what is inside
loot1 = LootBox()
loot1.populate_loot()
loot2 = LootBox()
loot2.populate_loot()
loot3 = LootBox()
loot3.populate_loot()

print('What box you want 1, 2, 3')
choice = input('? ')
if int(choice) == 1:
    print('\nBox 1')
    print('Congrats! Here is your loot!!\n')
    for item in loot1.loot_list:
        print(item.name)
        print(item.rarity)
        print(item.value)
        print("\n")
else:
    print('did you choose 1?')
player.add_to_inventory(loot1.loot_list)
print(player.access_inventory())



#saves changes to player
player_save(get_path(), player)



