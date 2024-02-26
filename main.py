# IMPORTS
import pickle
import os
import random
from player import Player
from lootbox import LootBox
from weapon import Weapon

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

# give the plahyer some weapons
temp_wep_list = []
for i in range(4):
    w = Weapon()
    w.build_weapon()
    temp_wep_list.append(w)

print('############')
for obj in temp_wep_list:
    print(obj.name + " " + obj.rarity)

player.add_to_inventory(temp_wep_list)
# w = Weapon()
# w.build_weapon()
# print(w.name)


# player.add_to_inventory({"Basic Sword": ['Short Sword', "Common", 10, 1], "Old Hat": ['Hat', 'Trash', 1, 1]})


# player.add_to_inventory({'Sock (used)': ['Sock', 'Trash', 1, 1]})

print(player.access_inventory())



#saves changes to player
player_save(get_path(), player)



