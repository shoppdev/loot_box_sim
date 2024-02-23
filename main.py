

# VARS



# CLASSES
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        self.invantory = []
        self.trade_status = False

    def __repr__(self):
        pass


# check if player exists, if not make a new one -- working
def check_for_player():
    new_player_list = []
    check_name = input("Who might you be? ")
    with open('files/player_list.txt') as player_list:
        known_players = player_list.readlines()
        new_player_list = file_stipper(known_players)
        
        if check_name in new_player_list:
            player_load(check_name)
        else:
            make_new_player_save(check_name)

# Strip off \n and return a list  -- working
def file_stipper(file):
    new_list = []
    for line in file:
        new_list.append(line.strip())

    return new_list

# Make a new instance of player
def make_new_player_save(name):
    # p_name = Player(name)
    f_path = 'files/saves/' + name
    name_to_add = name + '\n'

    # add player name to player_list.txt
    with open('files/player_list.txt', 'a') as add_player:
        add_player.write(name_to_add)

    # make new save here    
    with open(f_path, 'w') as new_player:
        print('file created need to build file structure')
        new_player.write(name + "'s file existis")
        # we will create the file structure here soon

# load the player file
def player_load(player):
    print("We will load player here")
    f = 'files/saves/' + player
    with open(f, 'r') as curr_player:
        print(curr_player.readlines())
        print("Load Complete")

# save the player file
def player_save(player):
    print("We save the player here")
    pass





## MAIN LOOP ##
check_for_player()