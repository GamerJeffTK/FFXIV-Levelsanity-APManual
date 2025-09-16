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

# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names

    # Add your code here to calculate which locations to remove based on options
    # For example, remove content based on expansion selection
    included_expansions = get_option_value(multiworld, player, "included_expansions")
    
    if included_expansions < 5:  # Not all expansions
        expansions_to_remove = []
        if included_expansions < 4:  # No EW
            expansions_to_remove.extend(["EW", "DT"])
        if included_expansions < 3:  # No ShB
            expansions_to_remove.extend(["ShB"])
        if included_expansions < 2:  # No StB
            expansions_to_remove.extend(["StB"])
        if included_expansions < 1:  # No HW
            expansions_to_remove.extend(["HW"])
            
        for region in multiworld.regions:
            if region.player == player:
                for location in list(region.locations):
                    # Check if location should be removed based on expansion
                    location_data = world.location_name_to_location.get(location.name, {})
                    location_categories = location_data.get("category", [])
                    
                    # Remove locations from excluded expansions
                    for exp in expansions_to_remove:
                        if exp in location_categories:
                            locationNamesToRemove.append(location.name)
                            break

    # Update victory conditions based on YAML options
    faded_crystals_required = get_option_value(multiworld, player, "faded_job_crystals_required")
    total_levels_required = get_option_value(multiworld, player, "total_levels_required")
    
    # Find and update victory locations
    for region in multiworld.regions:
        if region.player == player:
            for location in region.locations:
                location_data = world.location_name_to_location.get(location.name, {})
                
                if location.name == "Complete Job Crystal Collection":
                    if faded_crystals_required == 0:
                        # Disable this victory condition
                        locationNamesToRemove.append(location.name)
                    else:
                        # Update the requirement
                        location_data["requires"] = f"|A Faded Job Crystal:{faded_crystals_required}|"
                        
                elif location.name == "Reach Sufficient Total Levels":
                    if total_levels_required == 0:
                        # Disable this victory condition  
                        locationNamesToRemove.append(location.name)
                    else:
                        # Update the requirement
                        location_data["requires"] = f"{{TotalLevelsReached({total_levels_required})}}"

    # Remove disabled locations
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    # Filter items based on options
    include_extreme = get_option_value(multiworld, player, "include_extreme_difficulty")
    include_dungeons = get_option_value(multiworld, player, "include_dungeons")
    include_trials = get_option_value(multiworld, player, "include_trials")
    include_raids = get_option_value(multiworld, player, "include_raids")
    include_guildhests = get_option_value(multiworld, player, "include_guildhests")
    include_variant = get_option_value(multiworld, player, "include_variant_dungeons")
    include_bozja = get_option_value(multiworld, player, "include_bozja_content")
    included_expansions = get_option_value(multiworld, player, "included_expansions")
    
    # Build list of items to remove based on options
    items_to_remove = []
    
    # Filter by content type
    for item_name, item_data in world.item_name_to_item.items():
        if item_name in item_config:
            categories = item_data.get("category", [])
            
            # Check extreme/savage content
            if not include_extreme:
                if any(cat in categories for cat in ["Savage Raid"]) or "(Extreme)" in item_name or "(Savage)" in item_name:
                    items_to_remove.append(item_name)
                    continue
            
            # Check content types
            if not include_dungeons and "Dungeon" in categories:
                items_to_remove.append(item_name)
                continue
            if not include_trials and "Trial" in categories:
                items_to_remove.append(item_name)
                continue
            if not include_raids and any(cat in categories for cat in ["Normal Raid", "Alliance Raid", "Savage Raid"]):
                items_to_remove.append(item_name)
                continue
            if not include_guildhests and "Guildhest" in categories:
                items_to_remove.append(item_name)
                continue
            if not include_variant and "Variant Dungeon" in categories:
                items_to_remove.append(item_name)
                continue
            if not include_bozja and "Bozja" in categories:
                items_to_remove.append(item_name)
                continue
            
            # Check expansion filtering
            if included_expansions < 5:  # Not all expansions
                expansion_categories = []
                if included_expansions < 4:  # No EW/DT
                    expansion_categories.extend(["EW", "DT"])
                if included_expansions < 3:  # No ShB
                    expansion_categories.extend(["ShB"])
                if included_expansions < 2:  # No StB
                    expansion_categories.extend(["StB"])
                if included_expansions < 1:  # No HW
                    expansion_categories.extend(["HW"])
                
                if any(exp in categories for exp in expansion_categories):
                    items_to_remove.append(item_name)
                    continue
    
    # Remove filtered items
    for item_name in items_to_remove:
        if item_name in item_config:
            del item_config[item_name]
    
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Handle YAML option-based starting items
    # This integrates with the YAML configuration to override default starting items
    
    # Get option values
    starting_arr_crystals = get_option_value(multiworld, player, "starting_arr_job_crystals")
    starting_doh_crystals = get_option_value(multiworld, player, "starting_doh_job_crystals")
    starting_dol_crystals = get_option_value(multiworld, player, "starting_dol_job_crystals")
    starting_level_items = get_option_value(multiworld, player, "starting_level_increase_items")
    starting_duties = get_option_value(multiworld, player, "starting_duties")
    
    # Helper function to add starting items
    def add_starting_items_by_category(category: str, count: int):
        if count <= 0:
            return
        available_items = [item for item in item_pool if category in world.item_name_to_item.get(item.name, {}).get("category", [])]
        world.random.shuffle(available_items)
        items_to_start = available_items[:count]
        for item in items_to_start:
            multiworld.push_precollected(item)
            item_pool.remove(item)
    
    # Add starting items based on options
    add_starting_items_by_category("ARR Starter Job", starting_arr_crystals)
    add_starting_items_by_category("DOH Job Crystal", starting_doh_crystals)
    add_starting_items_by_category("DOL Job Crystal", starting_dol_crystals)
    add_starting_items_by_category("Level Progression", starting_level_items)
    
    # For duties, prioritize early duties
    if starting_duties > 0:
        # First try to get early duties
        early_duty_items = [item for item in item_pool if "Early Duty" in world.item_name_to_item.get(item.name, {}).get("category", [])]
        other_duty_items = [item for item in item_pool if "Duty" in world.item_name_to_item.get(item.name, {}).get("category", []) and "Early Duty" not in world.item_name_to_item.get(item.name, {}).get("category", [])]
        
        world.random.shuffle(early_duty_items)
        world.random.shuffle(other_duty_items)
        
        # Combine with early duties first
        all_duty_items = early_duty_items + other_duty_items
        duties_to_start = all_duty_items[:starting_duties]
        
        for item in duties_to_start:
            multiworld.push_precollected(item)
            item_pool.remove(item)
    
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