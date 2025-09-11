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
    target_level = int(level)
    
    # Check ARR Jobs (base level 10, plus level increases)
    for job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]:
        if state.has(f"{job} unlocked (default cap 10)", player):
            current_level = 10 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check HW Jobs (start at 30, plus level increases)
    for job in ["DRK","MCH","AST"]:
        if state.has(f"{job} unlocked", player):
            current_level = 30 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check STB Jobs (start at 50, plus level increases)
    for job in ["SAM","RDM"]:
        if state.has(f"{job} unlocked", player):
            current_level = 50 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check SHB Jobs (start at 60, plus level increases)
    for job in ["GNB","DNC"]:
        if state.has(f"{job} unlocked", player):
            current_level = 60 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check EW Jobs (start at 70, plus level increases)
    for job in ["RPR","SGE"]:
        if state.has(f"{job} unlocked", player):
            current_level = 70 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check DT Jobs (start at 80, plus level increases)
    for job in ["VPR","PCT"]:
        if state.has(f"{job} unlocked", player):
            current_level = 80 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check BLU (start at 1, plus level increases)
    if state.has("BLU unlocked", player):
        current_level = 1 + state.count("1 BLU Level", player)
        if current_level >= target_level:
            return True
    
    # Check DOH Jobs (start at 1, plus level increases)
    for job in ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]:
        if state.has(f"{job} unlocked", player):
            current_level = 1 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    # Check DOL Jobs (start at 1, plus level increases)
    for job in ["MIN","BTN","FSH"]:
        if state.has(f"{job} unlocked", player):
            current_level = 1 + state.count(f"1 {job} Level", player)
            if current_level >= target_level:
                return True
    
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"
