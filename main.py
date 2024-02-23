# IMPORTS
import pickle
import os
import random

# VARS
player = None
path_start = 'files/bin/'


# CLASSES - move to new file soon
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        self.inventory = {"Basic Sword" : ['Short Sword', 'Common', 10, 1]} # name item rarity max_value num_in_inventory
        self.trade_status = False

    def __repr__(self):
        pass

    # display inventory and alow you to sell, trade, delete
    def access_inventory(self):
        print('\n')
        print(" NAME            |      TYPE     |      RARITY     |            VALUE     |               QTY")
        print('_______________________________________________________________________________________________')
        for key, value in self.inventory.items():
            
            print('"{key}"     |     {type}     |     {rarity}     |     Value: {value}     |     {in_inventory}'.format(key=key, type = value[0], rarity = value[1], value = value[2], in_inventory = value[3]))
            print('_______________________________________________________________________________________________')

        print("\n")
        print("1: Sell")
        print("2: Trade")
        print("3: Destroy")
        print("0: Exit")
        choice = input("\nWhat would you like to do with your inventory?")

    def add_to_inventory(self, won_inventory):
        # pass in a dict of all the objects recieved if object in inventory increases qty
        for key, value in won_inventory.items():
            if key in self.inventory.keys():
                self.inventory[key][-1] += 1
            else:
                self.inventory[key] = value
        
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

# player.add_to_inventory({"Basic Sword": ['Short Sword', "Common", 10, 1], "Old Hat": ['Hat', 'Trash', 1, 1]})


player.add_to_inventory({'Sock (used)': ['Sock', 'Trash', 1, 1]})

print(player.access_inventory())



#saves changes to player
player_save(get_path(), player)
