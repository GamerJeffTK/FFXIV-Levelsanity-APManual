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

# Import job lists from Data hooks
ARR_JOB = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]
HW_JOB = ["DRK","MCH","AST"]
STB_JOB = ["SAM","RDM"]
SHB_JOB = ["GNB","DNC"]
EW_JOB = ["RPR","SGE"]
DT_JOB = ["VPR","PCT"]
DOH = ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]
DOL = ["MIN","BTN","FSH"]

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

# Helper functions for expansion filtering
def get_max_level(expansions: int) -> int:
    """Get the maximum level based on enabled expansions"""
    if expansions == 0:  # ARR only
        return 50
    elif expansions == 1:  # ARR + HW
        return 60
    elif expansions == 2:  # ARR + HW + StB
        return 70
    elif expansions == 3:  # ARR + HW + StB + ShB
        return 80
    elif expansions == 4:  # ARR + HW + StB + ShB + EW
        return 90
    else:  # All expansions
        return 100

def get_blu_max_level(expansions: int) -> int:
    """Get BLU's maximum level based on enabled expansions"""
    if expansions < 2:  # BLU not available before StB
        return 0
    elif expansions == 2:  # StB
        return 50
    elif expansions == 3:  # ShB
        return 70
    else:  # EW and beyond - BLU caps at 80
        return 80

def get_enabled_jobs(expansions: int) -> tuple[list[str], list[str], list[str], list[str]]:
    """Get enabled jobs by expansion, returns (dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled)"""
    dow_dom_jobs = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]  # ARR
    doh_jobs = ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]
    dol_jobs = ["MIN","BTN","FSH"]
    
    if expansions >= 1:  # HW
        dow_dom_jobs.extend(["DRK","MCH","AST"])
    if expansions >= 2:  # StB
        dow_dom_jobs.extend(["SAM","RDM"])
    if expansions >= 3:  # ShB
        dow_dom_jobs.extend(["GNB","DNC"])
    if expansions >= 4:  # EW
        dow_dom_jobs.extend(["RPR","SGE"])
    if expansions >= 5:  # DT
        dow_dom_jobs.extend(["VPR","PCT"])
    
    # BLU is available from StB onwards
    blu_enabled = expansions >= 2
    
    return dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled

def get_enabled_expansion_tags(expansions: int) -> list[str]:
    """Get enabled expansion tags for duties"""
    tags = ["ARR"]
    if expansions >= 1:
        tags.append("HW")
    if expansions >= 2:
        tags.append("StB")
    if expansions >= 3:
        tags.append("ShB")
    if expansions >= 4:
        tags.append("EW")
    if expansions >= 5:
        tags.append("DT")
    return tags

def get_duty_expansion_mapping() -> dict[str, str]:
    """Get the mapping of duties to their expansions"""
    return {
        # ARR Dungeons
        "Sastasha": "ARR", "The Tam-Tara Deepcroft": "ARR", "Copperbell Mines": "ARR", "Halatali": "ARR",
        "The Thousand Maws of Toto-Rak": "ARR", "Haukke Manor": "ARR", "Brayflox's Longstop": "ARR",
        "The Sunken Temple of Qarn": "ARR", "Cutter's Cry": "ARR", "The Stone Vigil": "ARR",
        "Dzemael Darkhold": "ARR", "The Aurum Vale": "ARR", "Castrum Meridianum": "ARR", "The Praetorium": "ARR",
        "The Wanderer's Palace": "ARR", "Amdapor Keep": "ARR", "Pharos Sirius": "ARR", "Copperbell Mines (Hard)": "ARR",
        "Haukke Manor (Hard)": "ARR", "The Lost City of Amdapor": "ARR", "Halatali (Hard)": "ARR",
        "Brayflox's Longstop (Hard)": "ARR", "Hullbreaker Isle": "ARR", "The Tam-Tara Deepcroft (Hard)": "ARR",
        "The Stone Vigil (Hard)": "ARR", "Snowcloak": "ARR", "Sastasha (Hard)": "ARR",
        "The Sunken Temple of Qarn (Hard)": "ARR", "The Keeper of the Lake": "ARR",
        "The Wanderer's Palace (Hard)": "ARR", "Amdapor Keep (Hard)": "ARR",
        
        # ARR Trials
        "The Bowl of Embers": "ARR", "The Navel": "ARR", "The Howling Eye": "ARR", "The Porta Decumana": "ARR",
        "The Bowl of Embers (Hard)": "ARR", "The Howling Eye (Hard)": "ARR", "The Navel (Hard)": "ARR",
        "Thornmarch (Hard)": "ARR", "A Relic Reborn: the Chimera": "ARR", "A Relic Reborn: the Hydra": "ARR",
        "The Whorleater (Hard)": "ARR", "Battle on the Big Bridge": "ARR", "The Striking Tree (Hard)": "ARR",
        "The Akh Afah Amphitheatre (Hard)": "ARR", "The Dragon's Neck": "ARR", "The Chrysalis": "ARR",
        "Battle in the Big Keep": "ARR", "Urth's Fount": "ARR", "The Minstrel's Ballad: Ultima's Bane": "ARR",
        "The Howling Eye (Extreme)": "ARR", "The Navel (Extreme)": "ARR", "The Bowl of Embers (Extreme)": "ARR",
        "Thornmarch (Extreme)": "ARR", "The Whorleater (Extreme)": "ARR", "The Striking Tree (Extreme)": "ARR",
        "The Akh Afah Amphitheatre (Extreme)": "ARR",
        
        # ARR Raids
        "The Binding Coil of Bahamut - Turn 1": "ARR", "The Binding Coil of Bahamut - Turn 2": "ARR",
        "The Binding Coil of Bahamut - Turn 3": "ARR", "The Binding Coil of Bahamut - Turn 4": "ARR",
        "The Binding Coil of Bahamut - Turn 5": "ARR", "The Second Coil of Bahamut - Turn 1": "ARR",
        "The Second Coil of Bahamut - Turn 2": "ARR", "The Second Coil of Bahamut - Turn 3": "ARR",
        "The Second Coil of Bahamut - Turn 4": "ARR", "The Final Coil of Bahamut - Turn 1": "ARR",
        "The Final Coil of Bahamut - Turn 2": "ARR", "The Final Coil of Bahamut - Turn 3": "ARR",
        "The Final Coil of Bahamut - Turn 4": "ARR", "The Second Coil of Bahamut (Savage) - Turn 1": "ARR",
        "The Second Coil of Bahamut (Savage) - Turn 2": "ARR", "The Labyrinth of the Ancients": "ARR",
        "Syrcus Tower": "ARR", "The World of Darkness": "ARR",
        
        # ARR Guildhests
        "Basic Training: Enemy Parties": "ARR", "Under the Armor": "ARR", "Basic Training: Enemy Strongholds": "ARR",
        "Hero on the Half Shell": "ARR", "Pulling Poison Posies": "ARR", "Stinging Back": "ARR",
        "All's Well that Ends in the Well": "ARR", "Flicking Sticks and Taking Names": "ARR",
        "More than a Feeler": "ARR", "Annoy the Void": "ARR", "Shadow and Claw": "ARR",
        "Long Live the Queen": "ARR", "Ward Up": "ARR", "Solemn Trinity": "ARR",
        
        # HW Dungeons
        "The Dusk Vigil": "HW", "Sohm Al": "HW", "The Aery": "HW", "The Vault": "HW", "The Great Gubal Library": "HW",
        "The Aetherochemical Research Facility": "HW", "Neverreap": "HW", "The Fractal Continuum": "HW",
        "Saint Mocianne's Arboretum": "HW", "Pharos Sirius (Hard)": "HW", "The Antitower": "HW",
        "The Lost City of Amdapor (Hard)": "HW", "Sohr Khai": "HW", "Hullbreaker Isle (Hard)": "HW",
        "Xelphatol": "HW", "The Great Gubal Library (Hard)": "HW", "Baelsar's Wall": "HW", "Sohm Al (Hard)": "HW",
        
        # HW Trials  
        "Thok ast Thok (Hard)": "HW", "The Limitless Blue (Hard)": "HW", "The Singularity Reactor": "HW",
        "Containment Bay S1T7": "HW", "The Final Steps of Faith": "HW", "Containment Bay P1T6": "HW",
        "Containment Bay Z1T9": "HW", "The Limitless Blue (Extreme)": "HW", "Thok ast Thok (Extreme)": "HW",
        "The Minstrel's Ballad: Thordan's Reign": "HW", "Containment Bay S1T7 (Extreme)": "HW",
        "The Minstrel's Ballad: Nidhogg's Rage": "HW", "Containment Bay P1T6 (Extreme)": "HW",
        "Containment Bay Z1T9 (Extreme)": "HW",
        
        # HW Raids
        "Alexander - The Fist of the Father": "HW", "Alexander - The Cuff of the Father": "HW",
        "Alexander - The Arm of the Father": "HW", "Alexander - The Burden of the Father": "HW",
        "The Void Ark": "HW", "The Weeping City of Mhach": "HW", "Dun Scaith": "HW",
        
        # StB Dungeons
        "The Sirensong Sea": "StB", "Shisui of the Violet Tides": "StB", "Bardam's Mettle": "StB", "Doma Castle": "StB",
        "Castrum Abania": "StB", "Ala Mhigo": "StB", "Kugane Castle": "StB", "The Temple of the Fist": "StB",
        "The Drowned City of Skalla": "StB", "Hells' Lid": "StB", "The Fractal Continuum (Hard)": "StB",
        "The Swallow's Compass": "StB", "The Burn": "StB", "Saint Mocianne's Arboretum (Hard)": "StB",
        "The Ghimlyt Dark": "StB",
        
        # StB Trials
        "The Pool of Tribute": "StB", "Emanation": "StB", "The Royal Menagerie": "StB", "The Jade Stoa": "StB",
        "Castrum Fluminis": "StB", "The Great Hunt": "StB", "Hells' Kier": "StB", "The Wreath of Snakes": "StB",
        "Kugane Ohashi": "StB", "The Pool of Tribute (Extreme)": "StB", "Emanation (Extreme)": "StB",
        "The Minstrel's Ballad: Shinryu's Domain": "StB", "The Jade Stoa (Extreme)": "StB",
        "The Minstrel's Ballad: Tsukuyomi's Pain": "StB", "The Great Hunt (Extreme)": "StB",
        "Hells' Kier (Extreme)": "StB", "The Wreath of Snakes (Extreme)": "StB",
        
        # StB Raids
        "Deltascape V1.0": "StB", "Deltascape V2.0": "StB", "Deltascape V3.0": "StB", "Deltascape V4.0": "StB",
        "The Royal City of Rabanastre": "StB", "The Ridorana Lighthouse": "StB", "The Orbonne Monastery": "StB",
        
        # ShB Dungeons  
        "Holminster Switch": "ShB", "Dohn Mheg": "ShB", "The Qitana Ravel": "ShB", "Malikah's Well": "ShB",
        "Mt. Gulg": "ShB", "Amaurot": "ShB", "The Twinning": "ShB", "Akadaemia Anyder": "ShB",
        "The Grand Cosmos": "ShB", "Anamnesis Anyder": "ShB", "The Heroes' Gauntlet": "ShB",
        "Matoya's Relict": "ShB", "Paglth'an": "ShB",
        
        # ShB Trials
        "The Dancing Plague": "ShB", "The Crown of the Immaculate": "ShB", "The Dying Gasp": "ShB",
        "Cinder Drift": "ShB", "The Seat of Sacrifice": "ShB", "Castrum Marinum": "ShB", "The Cloud Deck": "ShB",
        "The Dancing Plague (Extreme)": "ShB", "The Crown of the Immaculate (Extreme)": "ShB",
        "The Minstrel's Ballad: Hades's Elegy": "ShB", "Cinder Drift (Extreme)": "ShB",
        "Memoria Misera (Extreme)": "ShB", "The Seat of Sacrifice (Extreme)": "ShB",
        "Castrum Marinum (Extreme)": "ShB", "The Cloud Deck (Extreme)": "ShB",
        
        # ShB Raids
        "Eden's Gate: Resurrection": "ShB", "Eden's Gate: Descent": "ShB", "Eden's Gate: Inundation": "ShB", 
        "Eden's Gate: Sepulture": "ShB", "The Copied Factory": "ShB", "The Puppets' Bunker": "ShB", 
        "The Tower at Paradigm's Breach": "ShB", "Castrum Lacus Litore": "ShB", "Delubrum Reginae": "ShB", 
        "The Dalriada": "ShB",
        
        # EW Dungeons
        "The Tower of Zot": "EW", "The Tower of Babil": "EW", "Vanaspati": "EW", "Ktisis Hyperboreia": "EW",
        "The Aitiascope": "EW", "The Dead Ends": "EW", "Smileton": "EW", "The Stigma Dreamscape": "EW",
        "Alzadaal's Legacy": "EW", "The Fell Court of Troia": "EW", "Lapis Manalis": "EW",
        "The Aetherfont": "EW", "The Lunar Subterrane": "EW",
        
        # EW Trials
        "The Dark Inside": "EW", "The Mothercrystal": "EW", "The Final Day": "EW", "Storm's Crown": "EW",
        "Mount Ordeals": "EW", "The Voidcast Dais": "EW", "The Abyssal Fracture": "EW", "The Gilded Araya": "EW",
        "The Minstrel's Ballad: Zodiark's Fall": "EW", "The Minstrel's Ballad: Hydaelyn's Call": "EW",
        "The Minstrel's Ballad: Endsinger's Aria": "EW", "Storm's Crown (Extreme)": "EW",
        "Mount Ordeals (Extreme)": "EW", "The Voidcast Dais (Extreme)": "EW", "The Abyssal Fracture (Extreme)": "EW",
        
        # EW Raids
        "Asphodelos: The First Circle": "EW", "Asphodelos: The Second Circle": "EW", "Asphodelos: The Third Circle": "EW", 
        "Asphodelos: The Fourth Circle": "EW", "Aglaia": "EW", "Euphrosyne": "EW", "Thaleia": "EW",
        "The Sil'dihn Subterrane": "EW", "Mount Rokkon": "EW", "Aloalo Island": "EW",
        
        # DT Dungeons
        "Ihuykatumu": "DT", "Worqor Zormor": "DT", "The Skydeep Cenote": "DT", "Vanguard": "DT",
        "Origenics": "DT", "Alexandria": "DT", "Tender Valley": "DT", "The Strayborough Deadwalk": "DT",
        "Yuweyawata Field Station": "DT", "The Underkeep": "DT", "The Meso Terminal": "DT",
        
        # DT Trials
        "Worqor Lar Dor": "DT", "Everkeep": "DT", "The Interphos": "DT", "Recollection": "DT",
        "The Ageless Necropolis": "DT", "Worqor Lar Dor (Extreme)": "DT", "Everkeep (Extreme)": "DT",
        "The Minstrel's Ballad: Sphene's Burden": "DT", "Recollection (Extreme)": "DT",
        "The Minstrel's Ballad: Necron's Embrace": "DT",
        
        # DT Raids
        "AAC Light-heavyweight M1": "DT", "AAC Light-heavyweight M2": "DT", "AAC Light-heavyweight M3": "DT", 
        "AAC Light-heavyweight M4": "DT", "Jeuno: The First Walk": "DT", "San d'Oria: The Second Walk": "DT"
    }

def should_remove_item(item_name: str, expansions: int, max_level: int, blu_max_level: int, enabled_jobs: tuple, multiworld, player: int) -> bool:
    """Determine if an item should be removed based on expansion settings and content toggles"""
    dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled = enabled_jobs
    enabled_expansion_tags = get_enabled_expansion_tags(expansions)
    
    # Check if it's a job crystal or level progression item
    for job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN","DRK","MCH","AST","SAM","RDM","GNB","DNC","RPR","SGE","VPR","PCT"]:
        if job in item_name:
            if job not in dow_dom_jobs:
                return True
            # For level progression items, check if they exceed the level cap
            if "Level Increased by 5" in item_name:
                if job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]:  # ARR jobs
                    required_items = (max_level - 10) // 5 if max_level > 10 else 0
                elif job in ["DRK","MCH","AST"]:  # HW jobs
                    required_items = (max_level - 30) // 5 if max_level > 30 else 0
                elif job in ["SAM","RDM"]:  # StB jobs
                    required_items = (max_level - 50) // 5 if max_level > 50 else 0
                elif job in ["GNB","DNC"]:  # ShB jobs
                    required_items = (max_level - 60) // 5 if max_level > 60 else 0
                elif job in ["RPR","SGE"]:  # EW jobs
                    required_items = (max_level - 70) // 5 if max_level > 70 else 0
                elif job in ["VPR","PCT"]:  # DT jobs
                    required_items = (max_level - 80) // 5 if max_level > 80 else 0
                # If we don't need any progression items for this job, remove them
                if required_items <= 0:
                    return True
            break
    
    # Check BLU specifically
    if "BLU" in item_name:
        if not blu_enabled:
            return True
        if "Level Increased by 5" in item_name:
            required_items = (blu_max_level - 1) // 5 if blu_max_level > 1 else 0
            if required_items <= 0:
                return True
    
    # Check DOH jobs
    for job in doh_jobs:
        if job in item_name and "Level Increased by 5" in item_name:
            required_items = (max_level - 5) // 5 if max_level > 5 else 0
            if required_items <= 0:
                return True
            break
    
    # Check DOL jobs  
    for job in dol_jobs:
        if job in item_name and "Level Increased by 5" in item_name:
            required_items = (max_level - 5) // 5 if max_level > 5 else 0
            if required_items <= 0:
                return True
            break
    
    # Check duties by expansion - comprehensive mapping
    duty_expansions = get_duty_expansion_mapping()
    
    # Check if this is a duty from a disabled expansion
    for duty, expansion in duty_expansions.items():
        if duty in item_name and expansion not in enabled_expansion_tags:
            return True
    
    # Check content type toggles - only apply to duties, not job crystals or level progression items
    if any(duty in item_name for duty in duty_expansions.keys()):
        # Check if dungeons are disabled
        if not get_option_value(multiworld, player, "include_dungeons"):
            # Check if this is a dungeon (including hard modes)
            dungeon_indicators = [
                "Sastasha", "The Tam-Tara Deepcroft", "Copperbell Mines", "Halatali",
                "The Thousand Maws of Toto-Rak", "Haukke Manor", "Brayflox's Longstop",
                "The Sunken Temple of Qarn", "Cutter's Cry", "The Stone Vigil",
                "Dzemael Darkhold", "The Aurum Vale", "Castrum Meridianum", "The Praetorium",
                "The Wanderer's Palace", "Amdapor Keep", "Pharos Sirius",
                "The Lost City of Amdapor", "Hullbreaker Isle", "Snowcloak",
                "The Keeper of the Lake", "The Dusk Vigil", "Sohm Al", "The Aery",
                "The Vault", "The Great Gubal Library", "The Aetherochemical Research Facility",
                "Neverreap", "The Fractal Continuum", "Saint Mocianne's Arboretum",
                "The Antitower", "Xelphatol", "Baelsar's Wall", "The Sirensong Sea",
                "Shisui of the Violet Tides", "Bardam's Mettle", "Doma Castle",
                "Castrum Abania", "Ala Mhigo", "Kugane Castle", "The Temple of the Fist",
                "The Drowned City of Skalla", "Hells' Lid", "The Swallow's Compass",
                "The Burn", "The Ghimlyt Dark", "Holminster Switch", "Dohn Mheg",
                "The Qitana Ravel", "Malikah's Well", "Mt. Gulg", "Amaurot",
                "The Twinning", "Akadaemia Anyder", "The Grand Cosmos",
                "Anamnesis Anyder", "The Heroes' Gauntlet", "Matoya's Relict",
                "Paglth'an", "The Tower of Zot", "The Tower of Babil", "Vanaspati",
                "Ktisis Hyperboreia", "The Aitiascope", "The Dead Ends", "Smileton",
                "The Stigma Dreamscape", "Alzadaal's Legacy", "The Fell Court of Troia",
                "Lapis Manalis", "The Aetherfont", "The Lunar Subterrane",
                "Ihuykatumu", "Worqor Zormor", "The Skydeep Cenote", "Vanguard",
                "Origenics", "Alexandria", "Tender Valley", "The Strayborough Deadwalk",
                "Yuweyawata Field Station", "The Underkeep", "The Meso Terminal"
            ]
            if any(dungeon in item_name for dungeon in dungeon_indicators):
                return True
        
        # Check if trials are disabled
        if not get_option_value(multiworld, player, "include_trials"):
            trial_indicators = [
                "The Bowl of Embers", "The Navel", "The Howling Eye", "The Porta Decumana",
                "Thornmarch", "A Relic Reborn", "The Whorleater", "Battle on the Big Bridge",
                "The Striking Tree", "The Akh Afah Amphitheatre", "The Dragon's Neck",
                "The Chrysalis", "Battle in the Big Keep", "Urth's Fount",
                "The Minstrel's Ballad", "Thok ast Thok", "The Limitless Blue",
                "The Singularity Reactor", "Containment Bay", "The Final Steps of Faith",
                "The Pool of Tribute", "Emanation", "The Royal Menagerie",
                "The Jade Stoa", "Castrum Fluminis", "The Great Hunt", "Hells' Kier",
                "The Wreath of Snakes", "Kugane Ohashi", "The Dancing Plague",
                "The Crown of the Immaculate", "The Dying Gasp", "Cinder Drift",
                "The Seat of Sacrifice", "Castrum Marinum", "The Cloud Deck",
                "Memoria Misera", "The Dark Inside", "The Mothercrystal", "The Final Day",
                "Storm's Crown", "Mount Ordeals", "The Voidcast Dais",
                "The Abyssal Fracture", "The Gilded Araya", "Worqor Lar Dor",
                "Everkeep", "The Interphos", "Recollection", "The Ageless Necropolis"
            ]
            if any(trial in item_name for trial in trial_indicators):
                return True
        
        # Check if raids are disabled
        if not get_option_value(multiworld, player, "include_raids"):
            raid_indicators = [
                "The Binding Coil", "The Second Coil", "The Final Coil",
                "The Labyrinth of the Ancients", "Syrcus Tower", "The World of Darkness",
                "Alexander", "The Void Ark", "The Weeping City", "Dun Scaith",
                "Deltascape", "Sigmascape", "Alphascape", "The Royal City of Rabanastre",
                "The Ridorana Lighthouse", "The Orbonne Monastery", "Eden's Gate",
                "Eden's Verse", "Eden's Promise", "The Copied Factory",
                "The Puppets' Bunker", "The Tower at Paradigm's Breach",
                "Asphodelos", "Abyssos", "Anabaseios", "Aglaia", "Euphrosyne",
                "Thaleia", "AAC Light-heavyweight", "AAC Cruiserweight",
                "Jeuno: The First Walk", "San d'Oria: The Second Walk"
            ]
            if any(raid in item_name for raid in raid_indicators):
                return True
        
        # Check if guildhests are disabled
        if not get_option_value(multiworld, player, "include_guildhests"):
            guildhest_indicators = [
                "Basic Training: Enemy Parties", "Under the Armor",
                "Basic Training: Enemy Strongholds", "Hero on the Half Shell",
                "Pulling Poison Posies", "Stinging Back",
                "All's Well that Ends in the Well", "Flicking Sticks and Taking Names",
                "More than a Feeler", "Annoy the Void", "Shadow and Claw",
                "Long Live the Queen", "Ward Up", "Solemn Trinity"
            ]
            if any(guildhest in item_name for guildhest in guildhest_indicators):
                return True
        
        # Check if variant dungeons are disabled
        if not get_option_value(multiworld, player, "include_variant_dungeons"):
            variant_indicators = ["The Sil'dihn Subterrane", "Mount Rokkon", "Aloalo Island"]
            if any(variant in item_name for variant in variant_indicators):
                return True
        
        # Check if Bozja content is disabled
        if not get_option_value(multiworld, player, "include_bozja_content"):
            bozja_indicators = ["Castrum Lacus Litore", "Delubrum Reginae", "The Dalriada"]
            if any(bozja in item_name for bozja in bozja_indicators):
                return True
        
        # Check if extreme difficulty is disabled
        if not get_option_value(multiworld, player, "include_extreme_difficulty"):
            if "(Extreme)" in item_name or "(Savage)" in item_name or "The Minstrel's Ballad:" in item_name:
                return True
    
    return False

def should_remove_location(location_name: str, expansions: int, max_level: int, blu_max_level: int, enabled_jobs: tuple, multiworld, player: int) -> bool:
    """Determine if a location should be removed based on expansion settings and content toggles"""
    dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled = enabled_jobs
    
    # Check job level locations
    for job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN","DRK","MCH","AST","SAM","RDM","GNB","DNC","RPR","SGE","VPR","PCT"]:
        if f"{job} Level " in location_name:
            if job not in dow_dom_jobs:
                return True
            # Check if level exceeds cap
            try:
                level_str = location_name.split(f"{job} Level ")[1]
                level = int(level_str)
                if level > max_level:
                    return True
            except (IndexError, ValueError):
                pass
            break
    
    # Check BLU specifically
    if "BLU Level " in location_name:
        if not blu_enabled:
            return True
        try:
            level_str = location_name.split("BLU Level ")[1]
            level = int(level_str)
            if level > blu_max_level:
                return True
        except (IndexError, ValueError):
            pass
    
    # Check DOH/DOL job levels
    for job in doh_jobs + dol_jobs:
        if f"{job} Level " in location_name:
            try:
                level_str = location_name.split(f"{job} Level ")[1]
                level = int(level_str)
                if level > max_level:
                    return True
            except (IndexError, ValueError):
                pass
            break
    
    # Check duty completion locations
    if "Complete " in location_name:
        duty_name = location_name.replace("Complete ", "")
        duty_expansions = get_duty_expansion_mapping()
        
        if duty_name in duty_expansions:
            expansion = duty_expansions[duty_name]
            enabled_expansion_tags = get_enabled_expansion_tags(expansions)
            if expansion not in enabled_expansion_tags:
                return True
            
            # Check content type toggles for duty completion locations
            # Check if dungeons are disabled
            if not get_option_value(multiworld, player, "include_dungeons"):
                dungeon_indicators = [
                    "Sastasha", "The Tam-Tara Deepcroft", "Copperbell Mines", "Halatali",
                    "The Thousand Maws of Toto-Rak", "Haukke Manor", "Brayflox's Longstop",
                    "The Sunken Temple of Qarn", "Cutter's Cry", "The Stone Vigil",
                    "Dzemael Darkhold", "The Aurum Vale", "Castrum Meridianum", "The Praetorium",
                    "The Wanderer's Palace", "Amdapor Keep", "Pharos Sirius",
                    "The Lost City of Amdapor", "Hullbreaker Isle", "Snowcloak",
                    "The Keeper of the Lake", "The Dusk Vigil", "Sohm Al", "The Aery",
                    "The Vault", "The Great Gubal Library", "The Aetherochemical Research Facility",
                    "Neverreap", "The Fractal Continuum", "Saint Mocianne's Arboretum",
                    "The Antitower", "Xelphatol", "Baelsar's Wall", "The Sirensong Sea",
                    "Shisui of the Violet Tides", "Bardam's Mettle", "Doma Castle",
                    "Castrum Abania", "Ala Mhigo", "Kugane Castle", "The Temple of the Fist",
                    "The Drowned City of Skalla", "Hells' Lid", "The Swallow's Compass",
                    "The Burn", "The Ghimlyt Dark", "Holminster Switch", "Dohn Mheg",
                    "The Qitana Ravel", "Malikah's Well", "Mt. Gulg", "Amaurot",
                    "The Twinning", "Akadaemia Anyder", "The Grand Cosmos",
                    "Anamnesis Anyder", "The Heroes' Gauntlet", "Matoya's Relict",
                    "Paglth'an", "The Tower of Zot", "The Tower of Babil", "Vanaspati",
                    "Ktisis Hyperboreia", "The Aitiascope", "The Dead Ends", "Smileton",
                    "The Stigma Dreamscape", "Alzadaal's Legacy", "The Fell Court of Troia",
                    "Lapis Manalis", "The Aetherfont", "The Lunar Subterrane",
                    "Ihuykatumu", "Worqor Zormor", "The Skydeep Cenote", "Vanguard",
                    "Origenics", "Alexandria", "Tender Valley", "The Strayborough Deadwalk",
                    "Yuweyawata Field Station", "The Underkeep", "The Meso Terminal"
                ]
                if duty_name in dungeon_indicators:
                    return True
            
            # Check if trials are disabled
            if not get_option_value(multiworld, player, "include_trials"):
                trial_indicators = [
                    "The Bowl of Embers", "The Navel", "The Howling Eye", "The Porta Decumana",
                    "Thornmarch", "A Relic Reborn", "The Whorleater", "Battle on the Big Bridge",
                    "The Striking Tree", "The Akh Afah Amphitheatre", "The Dragon's Neck",
                    "The Chrysalis", "Battle in the Big Keep", "Urth's Fount",
                    "The Minstrel's Ballad", "Thok ast Thok", "The Limitless Blue",
                    "The Singularity Reactor", "Containment Bay", "The Final Steps of Faith",
                    "The Pool of Tribute", "Emanation", "The Royal Menagerie",
                    "The Jade Stoa", "Castrum Fluminis", "The Great Hunt", "Hells' Kier",
                    "The Wreath of Snakes", "Kugane Ohashi", "The Dancing Plague",
                    "The Crown of the Immaculate", "The Dying Gasp", "Cinder Drift",
                    "The Seat of Sacrifice", "Castrum Marinum", "The Cloud Deck",
                    "Memoria Misera", "The Dark Inside", "The Mothercrystal", "The Final Day",
                    "Storm's Crown", "Mount Ordeals", "The Voidcast Dais",
                    "The Abyssal Fracture", "The Gilded Araya", "Worqor Lar Dor",
                    "Everkeep", "The Interphos", "Recollection", "The Ageless Necropolis"
                ]
                if any(trial in duty_name for trial in trial_indicators):
                    return True
    
    return False


# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Get expansion settings
    expansions = get_option_value(multiworld, player, "included_expansions")
    max_level = get_max_level(expansions)
    blu_max_level = get_blu_max_level(expansions)
    enabled_jobs = get_enabled_jobs(expansions)
    
    # Remove locations from disabled expansions/levels
    locationNamesToRemove: list[str] = []
    
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if should_remove_location(location.name, expansions, max_level, blu_max_level, enabled_jobs, multiworld, player):
                    locationNamesToRemove.append(location.name)
    
    # Remove the locations
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    # Get expansion settings
    expansions = get_option_value(multiworld, player, "included_expansions")
    max_level = get_max_level(expansions)
    blu_max_level = get_blu_max_level(expansions)
    enabled_jobs = get_enabled_jobs(expansions)
    dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled = enabled_jobs
    
    # Adjust Faded Job Crystals count based on selected goal
    # The item is already added in Data.py for validation, now we adjust the count
    goal = get_option_value(multiworld, player, "goal")
    if goal == 2:  # "Collect All Faded Job Crystals" victory condition
        faded_crystals_required = get_option_value(multiworld, player, "faded_job_crystals_required")
        item_config["A Faded Job Crystal"] = faded_crystals_required
    # If goal != 2, we keep the default count (50) that was set in Data.py
    
    # Filter items based on expansion settings
    filtered_config = {}
    
    for item_name, config in item_config.items():
        if not should_remove_item(item_name, expansions, max_level, blu_max_level, enabled_jobs, multiworld, player):
            # For level progression items, adjust counts based on level caps
            if "Level Increased by 5" in item_name:
                # Calculate the required number of items based on level caps
                required_count = 0
                
                # Check each job type
                for job in dow_dom_jobs:
                    if job in item_name:
                        if job in ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]:  # ARR jobs
                            required_count = max(0, (max_level - 10 + 4) // 5)
                        elif job in ["DRK","MCH","AST"]:  # HW jobs
                            required_count = max(0, (max_level - 30 + 4) // 5)
                        elif job in ["SAM","RDM"]:  # StB jobs
                            required_count = max(0, (max_level - 50 + 4) // 5)
                        elif job in ["GNB","DNC"]:  # ShB jobs
                            required_count = max(0, (max_level - 60 + 4) // 5)
                        elif job in ["RPR","SGE"]:  # EW jobs
                            required_count = max(0, (max_level - 70 + 4) // 5)
                        elif job in ["VPR","PCT"]:  # DT jobs
                            required_count = max(0, (max_level - 80 + 4) // 5)
                        break
                
                # Check BLU specifically
                if "BLU" in item_name and blu_enabled:
                    required_count = max(0, (blu_max_level - 1 + 4) // 5)
                
                # Check DOH/DOL jobs
                for job in doh_jobs + dol_jobs:
                    if job in item_name:
                        required_count = max(0, (max_level - 5 + 4) // 5)
                        break
                
                # Update the config with the adjusted count
                if required_count > 0:
                    if isinstance(config, int):
                        filtered_config[item_name] = required_count
                    else:
                        # If it's a dict config, we need to adjust it proportionally
                        total_original = sum(config.values()) if isinstance(config, dict) else config
                        if total_original > 0:
                            ratio = required_count / total_original
                            if isinstance(config, dict):
                                new_config = {}
                                for classification, count in config.items():
                                    new_count = max(1, int(count * ratio))
                                    new_config[classification] = new_count
                                filtered_config[item_name] = new_config
                            else:
                                filtered_config[item_name] = required_count
            else:
                # For non-level items, keep the original config
                filtered_config[item_name] = config
    
    return filtered_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Filter starting items based on content toggles to ensure consistency
    # Get expansion settings
    expansions = get_option_value(multiworld, player, "included_expansions")
    max_level = get_max_level(expansions)
    blu_max_level = get_blu_max_level(expansions)
    enabled_jobs = get_enabled_jobs(expansions)
    
    # Remove items that should be filtered out
    items_to_remove = []
    for item in item_pool:
        if should_remove_item(item.name, expansions, max_level, blu_max_level, enabled_jobs, multiworld, player):
            items_to_remove.append(item)
    
    for item in items_to_remove:
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

# Custom client_data override to dynamically filter categories based on expansion settings
def get_filtered_categories(world: World, multiworld: MultiWorld, player: int) -> dict:
    """Return a filtered category table based on the player's expansion settings"""
    from ..Data import category_table
    
    # Get expansion settings
    expansions = get_option_value(multiworld, player, "included_expansions")
    enabled_jobs = get_enabled_jobs(expansions)
    dow_dom_jobs, doh_jobs, dol_jobs, blu_enabled = enabled_jobs
    
    # Create a copy of the category table to modify
    filtered_categories = category_table.copy()
    
    # Hide job categories for disabled jobs
    all_jobs = ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL + ["BLU"]
    enabled_job_names = dow_dom_jobs + doh_jobs + dol_jobs
    if blu_enabled:
        enabled_job_names.append("BLU")
    
    for job in all_jobs:
        if job not in enabled_job_names:
            filtered_categories[job] = {"hidden": True}
            # Also hide the level progression category for this job
            filtered_categories[f"{job} Level Progression"] = {"hidden": True}
    
    # Hide expansion-based categories
    enabled_expansion_tags = get_enabled_expansion_tags(expansions)
    expansion_tags = ["ARR", "HW", "StB", "ShB", "EW", "DT"]
    
    for expansion in expansion_tags:
        if expansion not in enabled_expansion_tags:
            filtered_categories[expansion] = {"hidden": True}
    
    return filtered_categories