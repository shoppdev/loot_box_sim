# Welcome to the Player class
    
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