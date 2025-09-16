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

# Import the new option-based generation function
from .Data import add_duty_items_based_on_options

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

# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Update victory locations based on options
    faded_crystals_required = get_option_value(multiworld, player, "faded_job_crystals_required")
    total_levels_required = get_option_value(multiworld, player, "total_levels_required")
    
    # Update the victory location requirements
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name == "The Crystal of Completion":
                    # Update the manual location data
                    world.location_name_to_location[location.name]["requires"] = f"|A Faded Job Crystal:{faded_crystals_required}|"
                elif location.name == "A certain amount of levels":
                    if total_levels_required > 0:
                        # Calculate percentage needed for level-based victory
                        dow_dom_percent = 75  # Default 75%
                        dol_percent = 75
                        doh_percent = 75
                        world.location_name_to_location[location.name]["requires"] = f"|@DOW/DOM:{dow_dom_percent}%| and |@DOL:{dol_percent}%| and |@DOH:{doh_percent}%|"
                    else:
                        # If total_levels_required is 0, make this location unreachable
                        world.location_name_to_location[location.name]["requires"] = "false"

    # Remove locations from the world that are disabled by options
    locationNamesToRemove: list[str] = []
    
    # If total_levels_required is 0, remove the level-based victory
    if total_levels_required == 0:
        locationNamesToRemove.append("A certain amount of levels")
    
    # If faded_crystals_required is 0 (hypothetically), remove crystal-based victory
    # (This shouldn't happen with current option constraints, but keeping for safety)
    if faded_crystals_required == 0:
        locationNamesToRemove.append("The Crystal of Completion")

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    # Update the Faded Job Crystal count based on options
    faded_crystals_required = get_option_value(multiworld, player, "faded_job_crystals_required")
    if "A Faded Job Crystal" in item_config:
        item_config["A Faded Job Crystal"] = faded_crystals_required
    
    # Add more duties based on player options
    additional_duties = add_duty_items_based_on_options([], multiworld, player)
    
    # Add the additional duties to the world's item table
    for duty_item in additional_duties:
        # Only add if it's not already in the item table
        if not any(item["name"] == duty_item["name"] for item in world.item_table):
            world.item_table.append(duty_item)
            world.item_name_to_item[duty_item["name"]] = duty_item
            
            # Add to item_config so it gets created
            item_config[duty_item["name"]] = duty_item.get("count", 1)
            
            # Update category groups
            for category in duty_item.get("category", []):
                if category not in world.item_name_groups:
                    world.item_name_groups[category] = []
                if duty_item["name"] not in world.item_name_groups[category]:
                    world.item_name_groups[category].append(duty_item["name"])
    
    # Remove duties that shouldn't be included based on options
    duties_to_remove = []
    
    # Check expansion settings
    included_expansions = get_option_value(multiworld, player, "included_expansions")
    expansion_names = ["ARR", "HW", "StB", "ShB", "EW", "DT"]
    included_exp_names = expansion_names[:included_expansions + 1]
    
    # Check content type settings
    include_dungeons = is_option_enabled(multiworld, player, "include_dungeons")
    include_trials = is_option_enabled(multiworld, player, "include_trials")
    include_extreme_difficulty = is_option_enabled(multiworld, player, "include_extreme_difficulty")
    
    for item_name, item_data in world.item_name_to_item.items():
        if "Duty" in item_data.get("category", []):
            should_remove = False
            
            # Check expansion inclusion
            item_expansions = [cat for cat in item_data.get("category", []) if cat in expansion_names]
            if item_expansions and not any(exp in included_exp_names for exp in item_expansions):
                should_remove = True
            
            # Check content type inclusion
            if not include_dungeons and "Dungeon" in item_data.get("category", []):
                should_remove = True
            elif not include_trials and "Trial" in item_data.get("category", []):
                should_remove = True
            elif not include_extreme_difficulty and "Extreme" in item_data.get("category", []):
                should_remove = True
            
            if should_remove:
                duties_to_remove.append(item_name)
    
    # Remove excluded duties from item_config
    for duty_name in duties_to_remove:
        if duty_name in item_config:
            item_config[duty_name] = 0  # Set count to 0 instead of removing to avoid KeyError
    
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Handle starting items based on options
    starting_arr = get_option_value(multiworld, player, "starting_arr_job_crystals")
    starting_doh = get_option_value(multiworld, player, "starting_doh_job_crystals")
    starting_dol = get_option_value(multiworld, player, "starting_dol_job_crystals")
    starting_levels = get_option_value(multiworld, player, "starting_level_increase_items")
    starting_duties = get_option_value(multiworld, player, "starting_duties")
    
    # Find items to start with
    items_to_start = []
    
    # ARR Job Crystals
    arr_crystals = [item for item in item_pool 
                   if item.name in world.item_name_to_item 
                   and "ARR Starter Job" in world.item_name_to_item[item.name].get("category", [])]
    world.random.shuffle(arr_crystals)
    for i in range(min(starting_arr, len(arr_crystals))):
        items_to_start.append(arr_crystals[i])
    
    # DOH Job Crystals  
    doh_crystals = [item for item in item_pool 
                   if item.name in world.item_name_to_item 
                   and "DOH Job Crystal" in world.item_name_to_item[item.name].get("category", [])]
    world.random.shuffle(doh_crystals)
    for i in range(min(starting_doh, len(doh_crystals))):
        items_to_start.append(doh_crystals[i])
    
    # DOL Job Crystals
    dol_crystals = [item for item in item_pool 
                   if item.name in world.item_name_to_item 
                   and "DOL Job Crystal" in world.item_name_to_item[item.name].get("category", [])]
    world.random.shuffle(dol_crystals)
    for i in range(min(starting_dol, len(dol_crystals))):
        items_to_start.append(dol_crystals[i])
    
    # Level Progression Items
    level_items = [item for item in item_pool 
                  if item.name in world.item_name_to_item 
                  and "Level Progression" in world.item_name_to_item[item.name].get("category", [])]
    world.random.shuffle(level_items)
    for i in range(min(starting_levels, len(level_items))):
        items_to_start.append(level_items[i])
    
    # Duty Items
    duty_items = [item for item in item_pool 
                 if item.name in world.item_name_to_item 
                 and "Duty" in world.item_name_to_item[item.name].get("category", [])]
    world.random.shuffle(duty_items)
    for i in range(min(starting_duties, len(duty_items))):
        items_to_start.append(duty_items[i])
    
    # Move selected items to starting items
    for item in items_to_start:
        multiworld.push_precollected(item)
        item_pool.remove(item)
    
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    # Force placement of critical early story duties to appropriate level ranges
    # This ensures story progression makes sense
    
    from worlds.generic.Rules import forbid_items_for_player
    
    # Define story duties that should appear early
    critical_early_duties = [
        "Sastasha", "The Tam-Tara Deepcroft", "Copperbell Mines", 
        "The Bowl of Embers", "Halatali", "The Navel"
    ]
    
    # Define endgame duties that shouldn't appear too early
    endgame_duties = []
    for item_name, item_data in world.item_name_to_item.items():
        if ("Duty" in item_data.get("category", []) and 
            any(exp in item_data.get("category", []) for exp in ["EW", "DT"])):
            endgame_duties.append(item_name)
    
    # Apply targeted restrictions
    for region in multiworld.regions:
        if region.player == player:
            for location in region.locations:
                # Extract level from location name
                import re
                level_pattern = r"Level (\d+)"
                match = re.search(level_pattern, location.name)
                
                if match:
                    level = int(match.group(1))
                    
                    # Prevent critical early duties from appearing in very high level locations (80+)
                    if level >= 80:
                        forbid_items_for_player(location, set(critical_early_duties), player)
                    
                    # Prevent endgame duties from appearing in very low level locations (1-35)
                    elif level <= 35:
                        forbid_items_for_player(location, set(endgame_duties), player)
    
    # Use early placement for story progression duties
    # The "early" property is already set in the duty generation, so AP will try to place them early

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
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
    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass