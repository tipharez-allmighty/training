from equipments import Weapon, Armor, HealingPotion

# Weapon
fist = Weapon(name="Fist", description="Bare knuckle", attack=10)

basic_sword = Weapon(
    name="Basic sword", description="The msot basic sword imaginable", attack=50
)

skin = Armor(name="Bare skin", description="No armor", defence=10)

# Armor
cloth_armor = Armor(
    name="Basic cloth armor",
    description="The most basic cloth armor imaginable",
    defence=50,
)

# Consumables
healing_potion = HealingPotion(
    name="Healing potion",
    description="Potion that heals for 10 health",
    healing_bonus=10,
)
