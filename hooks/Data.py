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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:50| OR |1 WAR Level:50| OR |1 DRG Level:50| OR |1 MNK Level:50| OR |1 BRD Level:50| OR |1 BLM Level:50| OR |1 WHM Level:50| OR |1 SMN/SCH Level:50| OR |1 NIN Level:50| OR |1 BLU Level:50| OR |1 DRK Level:20| OR |1 MCH Level:20| OR |1 AST Level:20| OR |1 SAM Level:10| OR |1 RDM Level:10|)",
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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:60| OR |1 WAR Level:60| OR |1 DRG Level:60| OR |1 MNK Level:60| OR |1 BRD Level:60| OR |1 BLM Level:60| OR |1 WHM Level:60| OR |1 SMN/SCH Level:60| OR |1 NIN Level:60| OR |1 BLU Level:60| OR |1 DRK Level:30| OR |1 MCH Level:30| OR |1 AST Level:30| OR |1 SAM Level:20| OR |1 RDM Level:20| OR |1 GNB Level:10| OR |1 DNC Level:10|)",
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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:70| OR |1 WAR Level:70| OR |1 DRG Level:70| OR |1 MNK Level:70| OR |1 BRD Level:70| OR |1 BLM Level:70| OR |1 WHM Level:70| OR |1 SMN/SCH Level:70| OR |1 NIN Level:70| OR |1 BLU Level:70| OR |1 DRK Level:40| OR |1 MCH Level:40| OR |1 AST Level:40| OR |1 SAM Level:30| OR |1 RDM Level:30| OR |1 GNB Level:20| OR |1 DNC Level:20| OR |1 RPR Level:10| OR |1 SGE Level:10|)",
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
            "category": ["BLU Level", "DOW/DOM", f"{job}"],
            "region": "BLU",
            "requires": "|BLU unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
            })

    for i in range(2, max_blu):
        level_list.append({
            "name":f"BLU level {i}",
            "category": ["BLU Level", "DOW/DOM", f"{job}"],
            "region": "BLU",
            "requires": f"|1 BLU Level:{i-1}| AND |BLU unlocked|",
            })

    for job in DOH:
        for i in range(1, 2):
             level_list.append({
                "name":f"{job} level {i}",
                "category": [f"{job} Level", "DOH", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked| AND (|1 PLD Level:15| OR |1 WAR Level:15| OR |1 DRG Level:15| OR |1 MNK Level:15| OR |1 BRD Level:15| OR |1 BLM Level:15| OR |1 WHM Level:15| OR |1 SMN/SCH Level:15| OR |1 NIN Level:15|)",
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
                "requires": f"|{job} unlocked| AND (|1 PLD Level:15| OR |1 WAR Level:15| OR |1 DRG Level:15| OR |1 MNK Level:15| OR |1 BRD Level:15| OR |1 BLM Level:15| OR |1 WHM Level:15| OR |1 SMN/SCH Level:15| OR |1 NIN Level:15|)",
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
           "progression": True,
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
           "progression": True,
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
           "progression": True,
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
           "progression": True,
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
           "progression": True,
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
           "progression": True,
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
        "progression": True,
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
            "progression": True,
            })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "Crafting Job"],
            "count": 1,
            "progression": True,
            })

    for job in DOL:
        item_table.append({
            "name": f"1 {job} Level",
            "category": [f"{job} Level Cap", "DOL", f"{job}"],
            "count": max_level,
            "progression": True,
            })

        item_table.append({
            "name":f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "Gathering Job"],
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
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
                        }
                    })
        if sub in STB_JOB:
            for job in STB_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
                        }
                    })
        if sub == "BLU":
                region_table.update({
                    "BLU": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|BLU unlocked| AND (|1 PLD Level:40| OR |1 WAR Level:40| OR |1 DRG Level:40| OR |1 MNK Level:40| OR |1 BRD Level:40| OR |1 BLM Level:40| OR |1 WHM Level:40| OR |1 SMN/SCH Level:40| OR |1 NIN Level:40|)",
                        }
                    })
        if sub in SHB_JOB:
            for job in SHB_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:50| OR |1 WAR Level:50| OR |1 DRG Level:50| OR |1 MNK Level:50| OR |1 BRD Level:50| OR |1 BLM Level:50| OR |1 WHM Level:50| OR |1 SMN/SCH Level:50| OR |1 NIN Level:50| OR |1 BLU Level:50| OR |1 DRK Level:20| OR |1 MCH Level:20| OR |1 AST Level:20| OR |1 SAM Level:10| OR |1 RDM Level:10|)",
                        }
                    })
        if sub in EW_JOB:
            for job in EW_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:60| OR |1 WAR Level:60| OR |1 DRG Level:60| OR |1 MNK Level:60| OR |1 BRD Level:60| OR |1 BLM Level:60| OR |1 WHM Level:60| OR |1 SMN/SCH Level:60| OR |1 NIN Level:60| OR |1 BLU Level:60| OR |1 DRK Level:30| OR |1 MCH Level:30| OR |1 AST Level:30| OR |1 SAM Level:20| OR |1 RDM Level:20| OR |1 GNB Level:10| OR |1 DNC Level:10|)",
                        }
                    })
        if sub in DT_JOB:
            for job in DT_JOB:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:70| OR |1 WAR Level:70| OR |1 DRG Level:70| OR |1 MNK Level:70| OR |1 BRD Level:70| OR |1 BLM Level:70| OR |1 WHM Level:70| OR |1 SMN/SCH Level:70| OR |1 NIN Level:70| OR |1 BLU Level:70| OR |1 DRK Level:40| OR |1 MCH Level:40| OR |1 AST Level:40| OR |1 SAM Level:30| OR |1 RDM Level:30| OR |1 GNB Level:20| OR |1 DNC Level:20| OR |1 RPR Level:10| OR |1 SGE Level:10|)",
                        }
                    })
        if sub in DOH:
            for job in DOH:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:5| OR |1 WAR Level:5| OR |1 DRG Level:5| OR |1 MNK Level:5| OR |1 BRD Level:5| OR |1 BLM Level:5| OR |1 WHM Level:5| OR |1 SMN/SCH Level:5| OR |1 NIN Level:5|)",
                        }
                    })
        if sub in DOL:
            for job in DOL:
                region_table.update({
                    f"{job}": {
                        "starting": False,
                        "connects_to": [],
                        "requires": f"|{job} unlocked| AND (|1 PLD Level:5| OR |1 WAR Level:5| OR |1 DRG Level:5| OR |1 MNK Level:5| OR |1 BRD Level:5| OR |1 BLM Level:5| OR |1 WHM Level:5| OR |1 SMN/SCH Level:5| OR |1 NIN Level:5|)",
                        }
                    })

    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
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
