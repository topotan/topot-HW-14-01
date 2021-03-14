# 1

import random


class PlayableUnit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.hp = 98
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
        self.basic = "dexterity"

    def choose_ability(self):
        making_choice = input("Choose between bow and crossbow: ")
        if making_choice == "bow" or making_choice == "crossbow":
            return f"{self.name} is a master of {making_choice}!"
        else:
            return "Archer class can only use bow or crossbow."


class Mage(PlayableUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.basic = "intellect"

    def choose_ability(self):
        making_choice = input("Choose between air, fire and water: ")
        if making_choice == "air" or making_choice == "fire" or making_choice == "water":
            return f"{self.name} is a Mage of {making_choice}!"
        else:
            return "You can only choose between fire, air and water."


class Knight(PlayableUnit):
    def __init__(self, name, clan):
        super().__init__(name, clan)
        self.basic = "strength"

    def choose_ability(self):
        making_choice = input("Choose between axe, sword and lance: ")
        if making_choice == "axe" or making_choice == "sword" or making_choice == "lance":
            return f"{self.name} is a Knight of {making_choice}!"
        else:
            return "You can only choose between axe, sword and lance."
