# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table

ARR_JOB = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH","NIN"]
HW_JOB = ["DRK","MCH","AST"]
STB_JOB = ["SAM","RDM"]
SHB_JOB = ["GNB","DNC"]
EW_JOB = ["RPR","SGE"]
DT_JOB = ["VPR","PCT"]
DOH = ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL"]
DOL = ["MIN","BTN","FSH"]
OVERALL_JOBS = ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL + ["BLU"]

def generate_level_list():
    level_list = []
    
    max_level = 101
    max_blu = 81
    
    for job in ARR_JOB:
        for i in range(1, 11):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked (default cap 10)|"
                })

    for job in ARR_JOB:
        for i in range(11, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-10}| AND |{job} unlocked (default cap 10)|"
                })

    for job in HW_JOB:
        for i in range(30, 31):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in HW_JOB:
        for i in range(31, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    for job in STB_JOB:
        for i in range(50, 51):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in STB_JOB:
        for i in range(51, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    for job in SHB_JOB:
        for i in range(60, 61):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in SHB_JOB:
        for i in range(61, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    for job in EW_JOB:
        for i in range(70, 71):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in EW_JOB:
        for i in range(71, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    for job in DT_JOB:
        for i in range(80, 81):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in DT_JOB:
        for i in range(81, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })
    
    for i in range(1, 2):
        level_list.append({
            "name":f"BLU level {i}",
            "category": ["BLU Level", "DOW/DOM", "BLU"],
            "region": "BLU",
            "requires": "|BLU unlocked|",
            })

    for i in range(2, max_blu):
        level_list.append({
            "name":f"BLU level {i}",
            "category": ["BLU Level", "DOW/DOM", "BLU"],
            "region": "BLU",
            "requires": f"|1 BLU Level:{i-1}| AND |BLU unlocked|",
            })

    for job in DOH:
        for i in range(1, 2):
             level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOH", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })

    for job in DOH:
        for i in range(2, max_level):
             level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOH", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    for job in DOL:
        for i in range(1, 2):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOL", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked|",
                })
    
    for job in DOL:
        for i in range(2, max_level):
            level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOL", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|",
                })

    return level_list
level_locations = generate_level_list()

# called after the items.json file has been loaded, before any item loading or processing has occurred
# if you need access to the items after processing to add ids, etc., you should use the hooks in World.py
def after_load_item_file(item_table: list) -> list:
    
    #crafters
    DOH = ["CRP","BSM","ARM","GSM","LTW","WVR","ALC","CUL",]
    #gatherers
    DOL = ["MIN","BTN","FSH",]

    max_level = 100
    max_blu = 80

    for job in ARR_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 10,
           "filler": True,
           })

        if job != "NIN":
            item_table.append({
                "name":f"{job} unlocked (default cap 10)",
                "category": ["Job Unlock", "DOW/DOM", "ARR Starter Job", "ARR Job"],
                "count": 1,
                "progression": True,
                })
        else:
            item_table.append({
                "name":f"{job} unlocked (default cap 10)",
                "category": ["Job Unlock", "DOW/DOM", "ARR Job"],
                "count": 1,
                "progression" : True,
                })

    for job in HW_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 30,
           "filler": True,
           })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "HW Job"],
            "count": 1,
            "progression": True,
            })

    for job in STB_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 50,
           "filler": True,
           })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "STB Job"],
            "count": 1,
            "progression": True,
            })

    for job in SHB_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 60,
           "filler": True,
           })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "SHB Job"],
            "count": 1,
            "progression": True,
            })

    for job in EW_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 70,
           "filler": True,
           })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "EW Job"],
            "count": 1,
            "progression": True,
            })

    for job in DT_JOB:
        item_table.append({
           "name":f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 80,
           "filler": True,
           })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "DT Job"],
            "count": 1,
            "progression": True,
            })

    item_table.append({
        "name":f"1 BLU Level",
        "category": ["BLU Level Cap", "DOW/DOM", "BLU"],
        "count": max_blu,
        "filler": True,
        })

    item_table.append({
            "name":f"BLU unlocked",
            "category": ["Job Unlock", "DOW/DOM", "Limited Job"],
            "count": 1,
            "progression": True,
            })

    for job in DOH:
        item_table.append({
            "name": f"1 {job} Level",
            "category": [f"{job} Level Cap", "DOH", f"{job}"],
            "count": max_level,
            "filler": True,
            })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock","DOH"],
            "count": 1,
            "progression": True,
            })

    for job in DOL:
        item_table.append({
            "name": f"1 {job} Level",
            "category": [f"{job} Level Cap", "DOL", f"{job}"],
            "count": max_level,
            "filler": True,
            })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOL"],
            "count": 1,
            "progression": True,
            })
    return item_table

# NOTE: Progressive items are not currently supported in Manual. Once they are,
#       this hook will provide the ability to meaningfully change those.
def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_location_file(location_table: list) -> list:
    #add level locations
    location_table.extend(level_locations)

    return location_table

# called after the locations.json file has been loaded, before any location loading or processing has occurred
# if you need access to the locations after processing to add ids, etc., you should use the hooks in World.py
def after_load_region_file(region_table: dict) -> dict:
    region_table = {}
    for sub in OVERALL_JOBS:
        if sub in ARR_JOB:
            for job in ARR_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": True,
                        "connects_to": ["DRK", "MCH", "AST", "SAM", "RDM", "BLU", "GNB", "DNC", "RPR", "SGE", "VPR", "PCT", "CRP", "BSM", "ARM", "GSM", "LTW", "WVR", "ALC", "CUL", "MIN", "BTN", "FSH"],
                        "requires": f"|{job} unlocked (default cap 10)|"
                        }
                    })
        if sub in HW_JOB:
            for job in HW_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}",
                        }
                    })
        if sub in STB_JOB:
            for job in STB_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}",
                        }
                    })
        if sub == "BLU":
                region_table.update({
                    "BLU": {
                        "starting": False,
                        "connects_to": [],
                        "requires": "|BLU unlocked| AND {anyClassLevel(50)}",
                        }
                    })
        if sub in SHB_JOB:
            for job in SHB_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(60)}",
                        }
                    })
        if sub in EW_JOB:
            for job in EW_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(70)}",
                        }
                    })
        if sub in DT_JOB:
            for job in DT_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(80)}",
                        }
                    })
        if sub in DOH:
            for job in DOH:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}",
                        }
                    })
        if sub in DOL:
            for job in DOL:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}",
                        }
                    })

    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    category_table = {}
    for sub in OVERALL_JOBS:
        for job in ARR_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked (default cap 10)|",
                    }
                })
        for job in HW_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}",
                    }
                })
        for job in STB_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}",
                    }
                })
        for job in SHB_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(60)}",
                    }
                })
        for job in EW_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(70)}",
                    }
                })
        for job in DT_JOB:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(80)}",
                    }
                })
        for job in DOH:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}",
                    }
                })
        for job in DOL:
            category_table.update({
                f"{job}": {
                    "hidden": True,
                    "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}",
                    }
                })
        if sub == "BLU":
            category_table.update({
                "BLU": {
                    "hidden": True,
                    "requires": "|{BLU unlocked| AND " + "{anyClassLevel(50)}",
                    }
                })
    return category_table

# called after the categories.json file has been loaded
def after_load_option_file(option_table: dict) -> dict:
    # option_table["core"] is the dictionary of modification of existing options
    # option_table["user"] is the dictionary of custom options
    return option_table

# called after the meta.json file has been loaded and just before the properties of the apworld are defined. You can use this hook to change what is displayed on the webhost
# for more info check https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/world%20api.md#webworld-class
def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

# called when an external tool (eg Universal Tracker) ask for slot data to be read
# use this if you want to restore more data
# return True if you want to trigger a regeneration if you changed anything
def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> dict | bool:
    return False
