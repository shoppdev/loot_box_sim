# Welcome to the Player class
import pickle
import save
    
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        self.inventory = {} # name  rarity max_value num_in_inventory
        self.trade_status = False
        self.key_list = []

    # display inventory and alow you to sell, trade, delete
    def access_inventory(self):
        count = 1
        print('\n')
        for key, value in self.inventory.items():
            print(f'''
        {count}. {key}
                    RARITY: {value[0]}      VALUE: {value[1]}      QTY: {value[2]}               
                  ''')
            print('_______________________________________________________________________')
            count += 1

        print("\n")
        print("1: Sell")
        print("0: Exit")
        choice = int(input("\nWhat would you like to do with your inventory?"))
        if choice == 1:
            self.sell_inventory()

    def sell_inventory(self):

        sell_choice = int(input("What # do you want to sell? "))
        key_number = int(sell_choice) - 1

        dict_key = self.key_list[key_number]
        key_string = dict_key.name #string
        
        for key, value in self.inventory.items():
            if key_string == key.name:
                print(f'Selling {key.name} for {key.value}G!!')
                self.gold_total += key.value    # adds value to gold pool
                junk = self.inventory.pop(key)
                jumk = self.key_list.pop(key_number)
                # save the player file
                save.player_save(self)
                break        

   # pass in the weapon object list
    def add_to_inventory(self, won_inventory):
        for obj in won_inventory:
            self.inventory[obj] = [obj.rarity, obj.value, obj.qty]
            if obj in self.key_list:
                pass
            else:
                self.key_list.append(obj)