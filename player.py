# Welcome to the Player class
    
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
        print("2: Trade")
        print("3: Destroy")
        print("0: Exit")
        choice = int(input("\nWhat would you like to do with your inventory?"))
        if choice == 1:
            self.sell_inventory()

    # this is not working. need to get it to delete dict entries
    def sell_inventory(self):
        sell_choice = int(input("What # do you want to sell? "))
        key_number = sell_choice - 1

        dict_key = self.key_list[key_number]
        key_string = dict_key.name
        key_value = dict_key.value

        
        if key_string in self.inventory.keys():
            print('found item you want to sell')
        else:
            print(f'cant find {key_string}')
            for item in self.inventory.keys:
                print(item)

        # print(type(sell_choice))
        # print(type(key_number))
        # print(type(dict_key))
        # print(dict_key)


   # pass in the weapon object list
    def add_to_inventory(self, won_inventory):
        # print('in add_to_inventory')
        for obj in won_inventory:
            self.inventory[obj] = [obj.rarity, obj.value, obj.qty]
            if obj in self.key_list:
                # print('in here')
                pass
            else:
                # print('not in here')
                self.key_list.append(obj)
                # print(type(obj.name))