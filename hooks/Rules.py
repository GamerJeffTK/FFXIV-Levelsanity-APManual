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
def anyClassLevel(state: CollectionState, player: int, level: str):
    """Has the player reached the given level on any class?"""
    target_level = int(level)
    
    # Check ARR Jobs (start at level 1, get 10 levels free with crystal)
    for job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]:
        if state.has(f"{job} Job Crystal", player):
            # Job starts at level 1, gets 10 free levels, then +5 per item
            base_level = 10
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check HW Jobs (start at level 30 with crystal)
    for job in ["DRK","MCH","AST"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 30
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check STB Jobs (start at level 50 with crystal)
    for job in ["SAM","RDM"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 50
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check SHB Jobs (start at level 60 with crystal)
    for job in ["GNB","DNC"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 60
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check EW Jobs (start at level 70 with crystal)
    for job in ["RPR","SGE"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 70
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check DT Jobs (start at level 80 with crystal)
    for job in ["VPR","PCT"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 80
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check BLU (start at level 1 with crystal)
    if state.has("BLU Job Crystal", player):
        base_level = 1
        level_items = state.count("BLU Level Increased by 5", player)
        current_level = base_level + (level_items * 5)
        if current_level >= target_level:
            return True
    
    # Check DOH Jobs (start at level 1 with crystal)
    for job in ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 1
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    # Check DOL Jobs (start at level 1 with crystal)
    for job in ["MIN","BTN","FSH"]:
        if state.has(f"{job} Job Crystal", player):
            base_level = 1
            level_items = state.count(f"{job} Level Increased by 5", player)
            current_level = base_level + (level_items * 5)
            if current_level >= target_level:
                return True
    
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee():
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Fighter Level:15| or |Black Belt Level:15| or |Thief Level:15|"