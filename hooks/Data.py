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
    
    # ARR Jobs: Start at level 1, have default cap of 10
    for job in ARR_JOB:
        for i in range(1, 11):  # Levels 1-10
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|{job} unlocked (default cap 10)|"
            })

    for job in ARR_JOB:
        for i in range(11, max_level):  # Levels 11-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-10}| AND |{job} unlocked (default cap 10)|"
            })

    # HW Jobs: Start at level 30
    for job in HW_JOB:
        level_list.append({
            "name": f"{job} level 30",
            "category": [f"{job} Level", "DOW/DOM", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(31, max_level):  # Levels 31-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    # STB Jobs: Start at level 50
    for job in STB_JOB:
        level_list.append({
            "name": f"{job} level 50",
            "category": [f"{job} Level", "DOW/DOM", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(51, max_level):  # Levels 51-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    # SHB Jobs: Start at level 60
    for job in SHB_JOB:
        level_list.append({
            "name": f"{job} level 60",
            "category": [f"{job} Level", "DOW/DOM", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(61, max_level):  # Levels 61-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    # EW Jobs: Start at level 70
    for job in EW_JOB:
        level_list.append({
            "name": f"{job} level 70",
            "category": [f"{job} Level", "DOW/DOM", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(71, max_level):  # Levels 71-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    # DT Jobs: Start at level 80
    for job in DT_JOB:
        level_list.append({
            "name": f"{job} level 80",
            "category": [f"{job} Level", "DOW/DOM", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(81, max_level):  # Levels 81-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOW/DOM", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })
    
    # BLU: Special case, starts at level 1, max 80
    level_list.append({
        "name": "BLU level 1",
        "category": ["BLU Level", "DOW/DOM", "BLU"],
        "region": "BLU",
        "requires": "|BLU unlocked|"
    })

    for i in range(2, max_blu):  # Levels 2-80
        level_list.append({
            "name": f"BLU level {i}",
            "category": ["BLU Level", "DOW/DOM", "BLU"],
            "region": "BLU",
            "requires": f"|1 BLU Level:{i-1}| AND |BLU unlocked|"
        })

    # DOH Jobs: Start at level 1
    for job in DOH:
        level_list.append({
            "name": f"{job} level 1",
            "category": [f"{job} Level", "DOH", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(2, max_level):  # Levels 2-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOH", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    # DOL Jobs: Start at level 1
    for job in DOL:
        level_list.append({
            "name": f"{job} level 1",
            "category": [f"{job} Level", "DOL", f"{job}"],
            "region": f"{job}",
            "requires": f"|{job} unlocked|"
        })
        
        for i in range(2, max_level):  # Levels 2-100
            level_list.append({
                "name": f"{job} level {i}",
                "category": [f"{job} Level", "DOL", f"{job}"],
                "region": f"{job}",
                "requires": f"|1 {job} Level:{i-1}| AND |{job} unlocked|"
            })

    return level_list

level_locations = generate_level_list()

def after_load_item_file(item_table: list) -> list:
    # FIXED: Use consistent max levels with generate_level_list()
    max_level = 100  
    max_blu = 80     

    # ARR Jobs
    for job in ARR_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 10,  # Levels 11-100
           "progression": True,
        })

        if job != "NIN":
            item_table.append({
                "name": f"{job} unlocked (default cap 10)",
                "category": ["Job Unlock", "DOW/DOM", "ARR Starter Job", "ARR Job"],
                "count": 1,
                "progression": True,
            })
        else:
            item_table.append({
                "name": f"{job} unlocked (default cap 10)",
                "category": ["Job Unlock", "DOW/DOM", "ARR Job"],
                "count": 1,
                "progression": True,
            })

    # HW Jobs
    for job in HW_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 30,  # Levels 31-100
           "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "HW Job"],
            "count": 1,
            "progression": True,
        })

    # STB Jobs
    for job in STB_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 50,  # Levels 51-100
           "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "STB Job"],
            "count": 1,
            "progression": True,
        })

    # SHB Jobs
    for job in SHB_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 60,  # Levels 61-100
           "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "SHB Job"],
            "count": 1,
            "progression": True,
        })

    # EW Jobs
    for job in EW_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 70,  # Levels 71-100
           "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "EW Job"],
            "count": 1,
            "progression": True,
        })

    # DT Jobs
    for job in DT_JOB:
        item_table.append({
           "name": f"1 {job} Level",
           "category": [f"{job} Level Cap", "DOW/DOM", f"{job}"],
           "count": max_level - 80,  # Levels 81-100
           "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock", "DOW/DOM", "DT Job"],
            "count": 1,
            "progression": True,
        })

    # BLU
    item_table.append({
        "name": "1 BLU Level",
        "category": ["BLU Level Cap", "DOW/DOM", "BLU"],
        "count": max_blu - 1,  # Levels 2-80
        "progression": True,
    })

    item_table.append({
        "name": "BLU unlocked",
        "category": ["Job Unlock", "DOW/DOM", "Limited Job"],
        "count": 1,
        "progression": True,
    })

    # DOH Jobs
    for job in DOH:
        item_table.append({
            "name": f"1 {job} Level",
            "category": [f"{job} Level Cap", "DOH", f"{job}"],
            "count": max_level - 1,  # Levels 2-100
            "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
            "category": ["Job Unlock","DOH"],
            "count": 1,
            "progression": True,
        })

    # DOL Jobs
    for job in DOL:
        item_table.append({
            "name": f"1 {job} Level",
            "category": [f"{job} Level Cap", "DOL", f"{job}"],
            "count": max_level - 1,  # Levels 2-100
            "progression": True,
        })

        item_table.append({
            "name": f"{job} unlocked",
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

    
    # ARR Jobs - Starting jobs that connect to all other jobs
    for job in ARR_JOB:
        region_table[job] = {
            "starting": True,
            "connects_to": ["DRK", "MCH", "AST", "SAM", "RDM", "BLU", "GNB", "DNC", "RPR", "SGE", "VPR", "PCT", "CRP", "BSM", "ARM", "GSM", "LTW", "WVR", "ALC", "CUL", "MIN", "BTN", "FSH"],
            "requires": f"|{job} unlocked (default cap 10)|"
        }

    # HW Jobs
    for job in HW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}"
        }

    # STB Jobs
    for job in STB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}"
        }

    # BLU
    region_table["BLU"] = {
        "starting": False,
        "connects_to": [],
        "requires": "|BLU unlocked| AND {anyClassLevel(50)}"
    }

    # SHB Jobs
    for job in SHB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(60)}"
        }

    # EW Jobs
    for job in EW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(70)}"
        }

    # DT Jobs
    for job in DT_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(80)}"
        }

    # DOH Jobs
    for job in DOH:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}"
        }

    # DOL Jobs
    for job in DOL:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}"
        }

    return region_table

# called after the categories.json file has been loaded
def after_load_category_file(category_table: dict) -> dict:
    
    # ARR Jobs
    for job in ARR_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked (default cap 10)|"
        }

    # HW Jobs
    for job in HW_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}"
        }

    # STB Jobs
    for job in STB_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(50)}"
        }

    # SHB Jobs
    for job in SHB_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(60)}"
        }

    # EW Jobs
    for job in EW_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(70)}"
        }

    # DT Jobs
    for job in DT_JOB:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(80)}"
        }

    # DOH Jobs
    for job in DOH:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}"
        }

    # DOL Jobs
    for job in DOL:
        category_table[job] = {
            "hidden": True,
            "requires": f"|{job} unlocked| AND " + "{anyClassLevel(15)}"
        }

    # BLU - FIXED: Syntax error in requires string
    category_table["BLU"] = {
        "hidden": True,
        "requires": "|BLU unlocked| AND {anyClassLevel(50)}"  # Fixed missing opening brace
    }

    return category_table

def after_load_option_file(option_table: dict) -> dict:
    return option_table

def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> dict | bool:
    return False