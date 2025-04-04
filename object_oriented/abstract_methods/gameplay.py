from npc import titus, thomas
from items import healing_potion


titus.dealDamage(thomas)
titus.dealDamage(thomas)
titus.dealDamage(thomas)
thomas.dealDamage(titus)
thomas.storeItem(healing_potion)
thomas.consumeItem(healing_potion)
print(titus._Character__attack)
print(titus)
print(thomas)
