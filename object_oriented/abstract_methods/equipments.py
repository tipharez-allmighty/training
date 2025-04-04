from abstract_classes import *


class Equipemnt(Item):
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    def __repr__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description


class Weapon(Equipemnt, AttackItem):
    def __init__(self, name: str, description: str, attack: int):
        super().__init__(name, description)
        self.__attack = attack

    @property
    def attack(self):
        return self.__attack


class Armor(Equipemnt, DefenceItem):
    def __init__(self, name: str, description: str, defence: int):
        super().__init__(name, description)
        self.__defence = defence

    @property
    def defence(self):
        return self.__defence


class HealingPotion(Equipemnt, ConsumableItem):
    def __init__(self, name: str, description: str, healing_bonus):
        super().__init__(name, description)
        self.__healing_bonus = healing_bonus

    @property
    def healing_bonus(self):
        return self.__healing_bonus

    def consume(self, target: LivingCreature):
        if isinstance(target, LivingCreature):
            target.increaseHealth(self.__healing_bonus)
        else:
            raise Exception("Target is not and Living Creature, cant get healed")
