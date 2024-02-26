# weapon class for making weapons
import random
import listsofitems as loi

base_values = [1, 10, 20, 50, 100, 150, 200, 300, 500, 550, 1000, 1000]

class Weapon:
    
    def __init__(self):
        self.name = ''
        self.rarity = 'none'
        self.max_value = '0'
        self.qty  = 1

    def __repr__(self):
        return self.name

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
            # print('Multiversal')
            self.rarity = 'Multiversal'
            self.name = random.choice(loi.multiversal_items)
            self.value = base_values[11]
        elif prcnt > 0.25 and prcnt <= 0.50:    # .25%
            # print('Cosmical')
            self.rarity = 'Cosmical'
            self.name = random.choice(loi.cosmical_items)
            self.value = base_values[10]
        elif prcnt > 0.50 and prcnt <= 1.25:    # .75%%
            # print('Devine')
            self.rarity = 'Devine'
            self.name = random.choice(loi.divine_items)
            self.value = base_values[9]
        elif prcnt > 1.25 and prcnt <= 2:        # .75%
            # print('Demonic')
            self.rarity = 'Demonic'
            self.name = random.choice(loi.demonic_items)
            self.value = base_values[8]
        elif prcnt > 2  and prcnt <= 6:          # 4%
            # print('Blessed')
            self.rarity = 'Blessed'
            self.name = random.choice(loi.blessed_items)
            self.value = base_values[7]
        elif prcnt > 6  and prcnt <= 10:          # 4%
            # print('Void Touched')
            self.rarity = 'Void Touched'
            self.name = random.choice(loi.void_touched_items)
            self.value = base_values[6]
        elif prcnt > 10 and prcnt <= 20:          # 10%
            # print('Legendary')
            self.rarity = 'Legendary' 
            self.name = random.choice(loi.legendary_items)
            self.value = base_values[5]
        elif prcnt > 20  and prcnt <= 35:          # 15%
            # print('Epic')
            self.rarity = 'Epic'
            self.name = random.choice(loi.epic_items) 
            self.value = base_values[4]
        elif prcnt > 35  and prcnt <= 50:          # 15%
            # print('Rare')
            self.rarity = 'Rare' 
            self.name = random.choice(loi.rare_items)
            self.value = base_values[3]
        elif prcnt > 50  and prcnt <= 70:          # 20%
            # print('Uncommon')
            self.rarity = 'Uncommon'
            self.name = random.choice(loi.uncommon_items)
            self.value = base_values[2]
        elif prcnt > 70 and prcnt <= 90:            # 20%
            # print('Common')
            self.rarity = 'Common'
            self.name = random.choice(loi.common_items)
            self.value = base_values[1]
        elif prcnt > 90  and prcnt <= 100:          # 10%
            # print('Trash')
            self.rarity = 'Trash'
            self.name = random.choice(loi.trash_items)
            self.value = base_values[0]
        else:
            # Just checking if anythin fell through the cracks
            print('##########################')
            print('Fell out of designed plans')
            print(prcnt)
            print('##########################')

# print(random.choice(loi.trash_items))
# for i in range(10):
#     w = Weapon()
#     w.build_weapon()
#     print(w.name)
#     print(w.rarity)
#     print(w.value)
#     print(w.qty)