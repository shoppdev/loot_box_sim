
from weapon import Weapon
import random

class LootBox:

    def __init__(self):
        self.name = "LootBox"
        self.loot_list = []

    def populate_loot(self):
        how_many = random.randint(3,4)
        for i in range(0, how_many):
           w = Weapon()
           w.build_weapon()
           self.loot_list.append(w)


