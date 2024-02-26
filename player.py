# Welcome to the Player class
    
class Player:

    def __init__(self, name):
        self.name = name
        self.gold_total = 1000  # just a guess, will update for balance
        self.inventory = {} # name item rarity max_value num_in_inventory
        self.trade_status = False

    def __repr__(self):
        pass

    # display inventory and alow you to sell, trade, delete
    def access_inventory(self):
        print('\n')
        print(" NAME                    |      RARITY     |            VALUE     |               QTY")
        print('____________________________________________________________________________________________________')
        for key, value in self.inventory.items():
            
            print('"{key}"          |      {rarity}     |     Value: {value}     |     {in_inventory}'.format(key=key, rarity = value[0], value = value[1], in_inventory = value[2]))
            print('_______________________________________________________________________________________________')

        print("\n")
        print("1: Sell")
        print("2: Trade")
        print("3: Destroy")
        print("0: Exit")
        choice = input("\nWhat would you like to do with your inventory?")


    #REWRITE FOR TAKING IN AN OBJECT NOT A DICT
    def add_to_inventory(self, won_inventory):
        # pass in a dict of all the objects recieved if object in inventory increases qty
        # for key, value in won_inventory.items():
        #     if key in self.inventory.keys():
        #         self.inventory[key][-1] += 1
        #     else:
        #         self.inventory[key] = value

        for obj in won_inventory:
            self.inventory[obj] = [obj.rarity, obj.value, obj.qty]