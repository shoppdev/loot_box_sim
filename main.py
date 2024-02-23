# IMPORTS
import pickle
import os
import random

# VARS
player = None
path_start = 'files/bin/'


# CLASSES
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        self.inventory = {"Sword" : ['Rare', 10, 0, 4, 9]}
        self.trade_status = False

    def __repr__(self):
        pass

    def display_inventory(self):
        pass

    def display_stats(self):
        pass



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

def player_create(player_name, path):
    print("Creating new player. Prepare for the fun")
    player = Player(player_name)
    player_save(player, path, player)
    return player

# need to build new path nothing returned
def player_save(path, player):
    with open(path, 'wb') as file:
        pickle.dump(player, file)

# just to make one thing easier
def get_path():
    return path_start + player.name


## MAIN LOOP ##
# Starts the game asking for player
player = check_for_player()


#saves changes to player
player_save(get_path(), player)