# hooks/Data.py - Minimal working version

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

def after_load_item_file(item_table: list) -> list:
    
    # Simple level threshold items
    item_table.append({
        "name": "Level 15 Access",
        "category": ["Level Gate"],
        "count": 1,
        "progression": True,
    })
    
    item_table.append({
        "name": "Level 50 Access",
        "category": ["Level Gate"],
        "count": 1,
        "progression": True,
    })
    
    item_table.append({
        "name": "Level 60 Access",
        "category": ["Level Gate"],
        "count": 1,
        "progression": True,
    })
    
    item_table.append({
        "name": "Level 70 Access",
        "category": ["Level Gate"],
        "count": 1,
        "progression": True,
    })
    
    item_table.append({
        "name": "Level 80 Access",
        "category": ["Level Gate"],
        "count": 1,
        "progression": True,
    })

    # ARR Jobs
    for job in ARR_JOB:
        # Level increases (simplified count)
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,  # Simplified count
           "progression": True,
        })

        # Job unlock
        if job != "NIN":
            item_table.append({
                "name": f"{job} Job Crystal",
                "category": ["Job Crystal", "DOW/DOM", "ARR Starter Job"],
                "count": 1,
                "progression": True,
            })
        else:
            item_table.append({
                "name": f"{job} Job Crystal",
                "category": ["Job Crystal", "DOW/DOM"],
                "count": 1,
                "progression": True,
            })

    # HW Jobs
    for job in HW_JOB:
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # STB Jobs
    for job in STB_JOB:
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # SHB Jobs
    for job in SHB_JOB:
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # EW Jobs
    for job in EW_JOB:
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # DT Jobs
    for job in DT_JOB:
        item_table.append({
           "name": f"{job} Level Increase",
           "category": [f"{job}", "DOW/DOM"],
           "count": 50,
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # BLU
    item_table.append({
        "name": "BLU Level Increase",
        "category": ["BLU", "DOW/DOM"],
        "count": 50,
        "progression": True,
    })

    item_table.append({
        "name": "BLU Job Crystal",
        "category": ["Job Crystal", "DOW/DOM"],
        "count": 1,
        "progression": True,
    })

    # DOH Jobs
    for job in DOH:
        item_table.append({
            "name": f"{job} Level Increase",
            "category": [f"{job}", "DOH"],
            "count": 50,
            "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOH"],
            "count": 1,
            "progression": True,
        })

    # DOL Jobs
    for job in DOL:
        item_table.append({
            "name": f"{job} Level Increase",
            "category": [f"{job}", "DOL"],
            "count": 50,
            "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOL"],
            "count": 1,
            "progression": True,
        })
    
    return item_table

def after_load_location_file(location_table: list) -> list:
    
    # Simple level milestone locations
    location_table.append({
        "name": "Reach Level 15 on Any Job",
        "category": ["Level Milestone"],
        "region": "Manual",
        "place_item": ["Level 15 Access"]
    })
    
    location_table.append({
        "name": "Reach Level 50 on Any Job",
        "category": ["Level Milestone"],
        "region": "Manual",
        "place_item": ["Level 50 Access"]
    })
    
    location_table.append({
        "name": "Reach Level 60 on Any Job",
        "category": ["Level Milestone"],
        "region": "Manual",
        "place_item": ["Level 60 Access"]
    })
    
    location_table.append({
        "name": "Reach Level 70 on Any Job",
        "category": ["Level Milestone"],
        "region": "Manual",
        "place_item": ["Level 70 Access"]
    })
    
    location_table.append({
        "name": "Reach Level 80 on Any Job",
        "category": ["Level Milestone"],
        "region": "Manual",
        "place_item": ["Level 80 Access"]
    })

    # Add level locations every 5 levels for each job
    for job in ARR_JOB:
        for level in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
            if level <= 10:
                # Levels 5 and 10 are free with job crystal (within the default cap of 10)
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal|"
                })
            else:
                # Levels 15+ require level increase items (starting from level 11)
                items_needed = (level - 10) // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
                })

    for job in HW_JOB:
        for level in [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
            items_needed = (level - 30) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    for job in STB_JOB:
        for level in [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
            items_needed = (level - 50) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    for job in SHB_JOB:
        for level in [60, 65, 70, 75, 80, 85, 90, 95, 100]:
            items_needed = (level - 60) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    for job in EW_JOB:
        for level in [70, 75, 80, 85, 90, 95, 100]:
            items_needed = (level - 70) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    for job in DT_JOB:
        for level in [80, 85, 90, 95, 100]:
            items_needed = (level - 80) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    # BLU levels every 5 (max 80) - starts at level 1, no free cap
    for level in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]:
        items_needed = level // 5
        location_table.append({
            "name": f"BLU Level {level}",
            "category": ["BLU", "DOW/DOM"],
            "region": "BLU",
            "requires": f"|BLU Level Increased by 5:{items_needed}| AND |BLU Job Crystal|"
        })

    # DOH levels every 5 - starts at level 1, no free cap
    for job in DOH:
        for level in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
            items_needed = level // 5
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOH"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    # DOL levels every 5 - starts at level 1, no free cap
    for job in DOL:
        for level in [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]:
            items_needed = level // 5
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOL"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| AND |{job} Job Crystal|"
            })

    return location_table

def after_load_region_file(region_table: dict) -> dict:

    # ARR Jobs - Starting regions, no requirements
    for job in ARR_JOB:
        region_table[job] = {
            "starting": True,
            "connects_to": []
        }

    # HW Jobs - Simple level 50 requirement
    for job in HW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 50 Access|"
        }

    # STB Jobs - Level 50 requirement
    for job in STB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 50 Access|"
        }

    # BLU - Level 50 requirement
    region_table["BLU"] = {
        "starting": False,
        "connects_to": [],
        "requires": "|Level 50 Access|"
    }

    # SHB Jobs - Level 60 requirement
    for job in SHB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 60 Access|"
        }

    # EW Jobs - Level 70 requirement
    for job in EW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 70 Access|"
        }

    # DT Jobs - Level 80 requirement
    for job in DT_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 80 Access|"
        }

    # DOH Jobs - Level 15 requirement
    for job in DOH:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 15 Access|"
        }

    # DOL Jobs - Level 15 requirement
    for job in DOL:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": "|Level 15 Access|"
        }

    return region_table

def after_load_category_file(category_table: dict) -> dict:
    # Keep categories simple
    for job in ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL + ["BLU"]:
        category_table[job] = {}
    
    return category_table

def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

def after_load_option_file(option_table: dict) -> dict:
    return option_table

def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> dict | bool:
    return False