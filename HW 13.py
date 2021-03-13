# 1

import random


class PlayableUnit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.hp = 100
        self.strength = 1
        self.dexterity = 1
        self.intellect = 1
        self.basic = ""

    def heal_unit(self):
        if self.hp < 100:
            hp_amount_added = random.randint(0, 10)
            self.hp += hp_amount_added
            if self.hp > 100:
                self.hp = 100
            if hp_amount_added == 0:
                return f"Attempt to heal was unsuccessful. The medication is wasted."
            else:
                return f"{self.name} was healed! The medication gave {self.name} {hp_amount_added} HP and his health is {self.hp} HP now."
        else:
            return "Don't waste that medicine, you are in full health!"

    def increase_strength(self):
        if self.strength < 10:
            self.strength += 1
            return f"{self.name} became stronger! His strength is {self.strength} now!"
        else:
            return "You are the strongest!"

    def increase_dexterity(self):
        if self.dexterity < 10:
            self.dexterity += 1
            return f"{self.name} is becoming dangerous! His dexterity is {self.dexterity} now!"
        else:
            return "You are the most dexterous!"

    def increase_intellect(self):
        if self.intellect < 10:
            self.intellect += 1
            return f"{self.name} became smarter! His intellect is {self.intellect} now!"
        else:
            return "You are the smartest!"

    def augment_basic_quality(self):
        if self.basic == "intellect":
            return self.increase_intellect()
        elif self.basic == "dexterity":
            return self.increase_dexterity()
        elif self.basic == "strength":
            return self.increase_strength()


class Archer(PlayableUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        bow_type = random.choice(["crossbow", "bow"])
        self.bonus_quality = f"{name} is a master of {bow_type}!"
        self.basic = "dexterity"


class Mage(PlayableUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        magic_type = random.choice(["Air", "Fire", "Water"])
        self.bonus_quality = f"{name} is a Mage of {magic_type}!"
        self.basic = "intellect"


class Knight(PlayableUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        weapon_type = random.choice(["axe", "sword", "lance"])
        self.bonus_quality = f"{name} will defeat his enemies with the power of {weapon_type}!"
        self.basic = "strength"
