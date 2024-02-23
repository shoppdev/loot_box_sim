# IMPORTS
import pickle
import os

# VARS
player = None


# CLASSES
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        # self.invantory = ['basic sword', 'hat']
        self.trade_status = False

    def __repr__(self):
        print(self.name, self.gold_total, self.trade_status)




# this gets player name input and checks to see if save exists
def check_for_player():
    player_name = input("What is your player name? (Use same name to continue game) ")
    file_path = 'files/bin/' + player_name

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
def player_save(player_name, path, player):
    with open(path, 'wb') as file:
        pickle.dump(player, file)


## MAIN LOOP ##
player = check_for_player()
print(player.name, player.gold_total)