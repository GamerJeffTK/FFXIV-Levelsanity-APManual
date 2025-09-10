from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for job in world.item_name_groups["ARR Job"]:
        if (state.count(job, player) + 10) >= int(level):
            return True
    for job in world.item_name_groups["HW Job"]:
        if (state.count(job, player) + 20) >= int(level):
            return True
    for job in world.item_name_groups["STB Job"]:
        if (state.count(job, player) + 40) >= int(level):
            return True
    for job in world.item_name_groups["SHB Job"]:
        if (state.count(job, player) + 50) >= int(level):
            return True
    for job in world.item_name_groups["EW Job"]:
        if (state.count(job, player) + 60) >= int(level):
            return True
    for job in world.item_name_groups["DT Job"]:
        if (state.count(job, player) + 70) >= int(level):
            return True
    for job in world.item_name_groups["BLU"]:
        if (state.count(job, player)) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
