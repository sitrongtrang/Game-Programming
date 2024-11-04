# Quick import for all items

from .BaseItem import BaseItem
from .HealItem import HealItem
from .SpeedItem import SpeedItem
from .DmgItem import DmgItem
from .JumpItem import JumpItem
from .SpeedItem import SpeedItem
from .BulletItem import BulletItem 
from random import choice as _random
ItemMap = {
    'heal': HealItem,
    'speed': SpeedItem,
    'dmg': DmgItem,
    'jump': JumpItem,
    'bullet': BulletItem
}

def random_item(flag: bool = False):
    if not flag: return ItemMap.get(_random(ItemMap.keys()))
    else: return ItemMap.get(_random(['heal', 'speed', 'dmg', 'jump']))