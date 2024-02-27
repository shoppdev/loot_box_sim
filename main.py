# IMPORTS
import pickle
import os
import random
from player import Player
from lootbox import LootBox

# VARS
player = None
path_start = 'files/bin/'
box_cost = 10   # this is the cost of a lootbox

        
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

def make_lootbox():
    loot_box = LootBox()
    loot_box.populate_loot()
    return loot_box

def show_loot(choice, box_list):
    print(f'You chose box #{choice}')
    if choice == 1:
        # print(box_list[0].loot_list)
        print('\n\n You recieced: \n')
        for obj in box_list[0].loot_list:
            print(obj.name)
            print(obj.rarity)
            print(obj.value)
            print('\n')
            player.add_to_inventory(box_list[0].loot_list)
    elif choice == 2:
        # print(box_list[0].loot_list)
        print('\n\n You recieced: \n')
        for obj in box_list[1].loot_list:
            print(obj.name)
            print(obj.rarity)
            print(obj.value)
            print('\n')
            player.add_to_inventory(box_list[1].loot_list)
    elif choice == 3:
        # print(box_list[0].loot_list)
        print('\n\n You recieced: \n')
        for obj in box_list[2].loot_list:
            print(obj.name)
            print(obj.rarity)
            print(obj.value)
            print('\n')
            player.add_to_inventory(box_list[2].loot_list)
    else:
        print("IF YOU SEE ME SOMTHING IS TERRIBLY WRON IN MAIN/show_loot()")
    fake = input('\nPress Enter to contine\n')


def loot_box_time():
    choice = 99
    l1 = make_lootbox()
    l2 = make_lootbox()
    l3 = make_lootbox()
    box_list = [l1, l2, l3]
    while choice != 0:
        print('Please choose a loot box: 0 to exit')
        print('''
         _____     _____     _____
        |  ^  |   |  ^  |   |  ^  |
        |  1  |   |  2  |   |  3  |
        |     |   |     |   |     |  
         -----     -----     -----                  
    ''')
        choice = int(input("? "))
        if choice < 1 or choice > 3:
            print('Please choose a valid box')
        else:
            player.gold_total -= box_cost
            show_loot(choice, box_list)

## MAIN LOOP ##
# Starts the game asking for player
player = check_for_player()

print(f'\nWelcome {player.name} to Loot Box Simulator!')


choice = 49
while choice != 0:
    print(f'You have {player.gold_total}G and {len(player.inventory)} items')
    print('\n')
    print('''
    1. See inventory
    2. Buy Loot Box
    3. Sell
    4. Trade
    0. exit
          ''')
    choice = int(input("? "))
    if choice == 1:
        player.access_inventory()
    elif choice == 2:
        loot_box_time()
    elif choice == 3:
        print("sell here (shop closed)")
    elif choice == 4:
        print("Trading comming soon")
    else:
        print('Please choose another choice. Ya know, from the list?')

# # make a loot box and see what is inside
# loot1 = LootBox()
# loot1.populate_loot()
# loot2 = LootBox()
# loot2.populate_loot()
# loot3 = LootBox()
# loot3.populate_loot()

# print('What box you want 1, 2, 3')
# choice = input('? ')
# if int(choice) == 1:
#     print('\nBox 1')
#     print('Congrats! Here is your loot!!\n')
#     for item in loot1.loot_list:
#         print(item.name)
#         print(item.rarity)
#         print(item.value)
#         print("\n")
# else:
#     print('did you choose 1?')
# player.add_to_inventory(loot1.loot_list)
# print(player.access_inventory())



#saves changes to player
player_save(get_path(), player)



