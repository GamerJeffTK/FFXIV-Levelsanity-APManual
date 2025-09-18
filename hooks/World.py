# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################

def get_expansion_limits(expansion_choice):
    """Returns the jobs, max level, and available expansions for the chosen expansion setting"""
    ARR_JOB = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]
    HW_JOB = ["DRK","MCH","AST"]
    STB_JOB = ["SAM","RDM","BLU"]  # BLU is a StB job
    SHB_JOB = ["GNB","DNC"]
    EW_JOB = ["RPR","SGE"]
    DT_JOB = ["VPR","PCT"]
    DOH = ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]
    DOL = ["MIN","BTN","FSH"]
    
    if expansion_choice == 0:  # ARR only
        return ARR_JOB + DOH + DOL, 50, ["ARR"]
    elif expansion_choice == 1:  # ARR + HW  
        return ARR_JOB + HW_JOB + DOH + DOL, 60, ["ARR", "HW"]
    elif expansion_choice == 2:  # ARR + HW + StB
        return ARR_JOB + HW_JOB + STB_JOB + DOH + DOL, 70, ["ARR", "HW", "StB"]
    elif expansion_choice == 3:  # ARR + HW + StB + ShB
        return ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + DOH + DOL, 80, ["ARR", "HW", "StB", "ShB"]
    elif expansion_choice == 4:  # ARR + HW + StB + ShB + EW
        return ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DOH + DOL, 90, ["ARR", "HW", "StB", "ShB", "EW"]
    else:  # All expansions (5)
        return ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL, 100, ["ARR", "HW", "StB", "ShB", "EW", "DT"]

# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Get expansion limits
    expansion_choice = get_option_value(multiworld, player, 'included_expansions')
    available_jobs, max_level, available_expansions = get_expansion_limits(expansion_choice)
    
    # Define all possible jobs
    all_jobs = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN","DRK","MCH","AST","SAM","RDM","BLU","GNB","DNC","RPR","SGE","VPR","PCT","CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL","MIN","BTN","FSH"]
    
    # Filter locations from regions
    regions_to_process = [r for r in multiworld.regions if r.player == player]
    
    for region in regions_to_process:
        # Check if this is a job region that shouldn't exist - mark all its locations for removal
        if region.name in all_jobs and region.name not in available_jobs:
            # Remove all locations from this unavailable job region
            region.locations.clear()
            continue
        
        # Filter locations within remaining regions
        locations_to_remove = []
        for location in list(region.locations):
            should_remove = False
            
            # Check if location is for a job that shouldn't exist
            location_job = None
            for job in all_jobs:
                if location.name.startswith(f"{job} Level "):
                    location_job = job
                    break
            
            if location_job and location_job not in available_jobs:
                should_remove = True
            elif location_job:
                # Check if location is for a level above max level
                level_str = location.name.replace(f"{location_job} Level ", "")
                try:
                    level = int(level_str)
                    if level > max_level:
                        should_remove = True
                    # Special case for BLU - cap at 80 even in EW/DT expansions
                    elif location_job == "BLU" and level > min(80, max_level):
                        should_remove = True
                except ValueError:
                    pass
            
            if should_remove:
                locations_to_remove.append(location)
        
        # Remove locations from region
        for location in locations_to_remove:
            region.locations.remove(location)

    logging.info(f"Expansion filtering: Using {available_jobs} jobs with max level {max_level} for expansions {available_expansions}")

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    # Get expansion limits  
    expansion_choice = get_option_value(multiworld, player, 'included_expansions')
    available_jobs, max_level, available_expansions = get_expansion_limits(expansion_choice)
    
    # Define all possible jobs
    all_jobs = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN","DRK","MCH","AST","SAM","RDM","BLU","GNB","DNC","RPR","SGE","VPR","PCT","CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL","MIN","BTN","FSH"]
    
    # Filter items that shouldn't exist
    items_to_remove = []
    for item_name in list(item_config.keys()):
        should_remove = False
        
        # Check job crystal and level progression items
        for job in all_jobs:
            if job not in available_jobs and (f"{job} Job Crystal" in item_name or f"{job} Level Increased by 5" in item_name):
                should_remove = True
                break
        
        # Check duty items from wrong expansions
        if not should_remove:
            item_data = world.item_name_to_item.get(item_name, {})
            categories = item_data.get("category", [])
            for category in categories:
                if category in ["HW", "StB", "ShB", "EW", "DT"] and category not in available_expansions:
                    should_remove = True
                    break
        
        if should_remove:
            items_to_remove.append(item_name)
    
    # Remove filtered items by setting their count to 0
    for item_name in items_to_remove:
        item_config[item_name] = 0
    
    logging.info(f"Expansion filtering: Removed {len(items_to_remove)} items not available in selected expansions")
    
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove: list[str] = [] # List of item names

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass