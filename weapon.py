# weapon class for making weapons
import random

rarities = ('trash', 'common', 'uncommon', 'rare', 'epic' 'legendary', 'Void Touched', 
           'Blessed','Demonic', 'Divine', 'Cosmical', 'Multiversal')

class Weapon:
    
    def __init__(self):
        self.name = ''
        self.wep_type = 'default'
        self.rarity = 'none'
        self.max_value = '0'
        self.qty  = 1

    def __repr__(self):
        print(self.name)

    def build_weapon(self):
        # first pick rarity -- this gives us o to 1, we turn into percentage.
        # rand_dec = round(random.uniform(-1, 1.0), 6)
        # prcnt = rand_dec * 100
        prcnt = -2

        # grab a random number and make sure its not negative
        while prcnt < 0:
            rand_dec = round(random.uniform(-1, 1.0), 5)
            prcnt = rand_dec * 100
 
        if prcnt > 0 and prcnt <= 0.25:         # .25%
            print('Multiversal')
            self.rarity = 'Multiversal'
        elif prcnt > 0.25 and prcnt <= 0.50:    # .25%
            print('Cosmical')
            self.rarity = 'Cosmical'
        elif prcnt > 0.50 and prcnt <= 1.25:    # .75%%
            print('Devine')
            self.rarity = 'Devine'
        elif prcnt > 1.25 and prcnt <= 2:        # .75%
            print('Demonic')
            self.rarity = 'Demonic'
        elif prcnt > 2  and prcnt <= 6:          # 4%
            print('Blessed')
            self.rarity = 'Blessed'
        elif prcnt > 6  and prcnt <= 10:          # 4%
            print('Void Touched')
            self.rarity = 'Void Touched'
        elif prcnt > 10 and prcnt <= 20:          # 10%
            print('Legondary')
            self.rarity = 'Legondary' 
        elif prcnt > 20  and prcnt <= 35:          # 15%
            print('Epic')
            self.rarity = 'Epic' 
        elif prcnt > 35  and prcnt <= 50:          # 15%
            print('Rare')
            self.rarity = 'Rare' 
        elif prcnt > 50  and prcnt <= 70:          # 20%
            print('Uncommon')
            self.rarity = 'Uncommon'
        elif prcnt > 70 and prcnt <= 90:            # 20%
            print('Common')
            self.rarity = 'Common'
        elif prcnt > 90  and prcnt <= 100:          # 10%
            print('Trash')
            self.rarity = 'Trash'
        else:
            print('##########################')
            print('Fell out of designed plans')
            print(prcnt)
            print('##########################')

            
        

        
    # build name based on rarity
    def name_weapon(self):
        pass

    # decide value based on rarity
    def value_weapon(self):
        pass


for i in range(100):
    w = Weapon()
    w.build_weapon()