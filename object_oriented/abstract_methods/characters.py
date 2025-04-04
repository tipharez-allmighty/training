from abstract_classes import LivingCreature
from equipments import Weapon, Armor, Equipemnt, ConsumableItem
from items import fist, skin


class Character(LivingCreature):
    def __init__(
        self, name: str, weapon: Weapon | None = None, armor: Armor | None = None
    ):
        self.__name = name
        self.__max_health = 100
        self.__health = self.__max_health
        self.__attack = weapon.attack if weapon else fist.attack
        self.__defence = armor.defence if armor else skin.defence
        self.__items = []

    def __repr__(self):
        return (
            f"{self.__name}, "
            f"health={self.__health}/{self.__max_health}, "
            f"Attack={self.__attack}, "
            f"Defence={self.__defence}"
        )

    @property
    def name(self):
        return self.__name

    @property
    def max_health(self):
        return self.__max_health

    @property
    def health(self):
        return self.__health

    @property
    def attack(self):
        return self.__attack

    @property
    def defence(self):
        return self.__defence

    @property
    def items(self):
        return self.__items

    def decreaseHealth(self, damage: int):
        self.__health = max(0, self.__health - damage)

    def increaseHealth(self, amount: int):
        self.__health = min(self.__max_health, self.__health + amount)

    def dealDamage(self, target: LivingCreature):
        if isinstance(target, LivingCreature):
            damage = int(self.__attack * (1 - (target.defence / 100)))
            target.decreaseHealth(damage)
        else:
            raise Exception("This is not character")

    def storeItem(self, item: Equipemnt):
        if isinstance(item, Equipemnt):
            self.__items.append(item)
        else:
            raise Exception("You cant put this object into your inventory.")

    def consumeItem(self, item: ConsumableItem):
        if isinstance(item, ConsumableItem):
            if item in self.items:
                item.consume(self)
            else:
                return None
        else:
            raise Exception("You cant use item that is not consumable")
