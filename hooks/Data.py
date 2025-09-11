# hooks/Data.py - Fixed version with consistent naming and proper connections

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
        # Level increases - FIXED: using "Level Increased by 5" naming
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 18,  # Each gives 5 levels, need 18 for levels 15-100 (85 levels / 5 = 17, +1 buffer)
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
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 14,  # Levels 35-100 (65 levels / 5 = 13, +1 buffer)
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
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 11,  # Levels 55-100 (45 levels / 5 = 9, +2 buffer)
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
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 9,  # Levels 65-100 (35 levels / 5 = 7, +2 buffer)
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
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 7,  # Levels 75-100 (25 levels / 5 = 5, +2 buffer)
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
           "name": f"{job} Level Increased by 5",
           "category": [f"{job}", "DOW/DOM"],
           "count": 5,  # Levels 85-100 (15 levels / 5 = 3, +2 buffer)
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
        "name": "BLU Level Increased by 5",
        "category": ["BLU", "DOW/DOM"],
        "count": 16,  # Levels 5-80 (75 levels / 5 = 15, +1 buffer)
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
            "name": f"{job} Level Increased by 5",
            "category": [f"{job}", "DOH"],
            "count": 20,  # Levels 5-100 (95 levels / 5 = 19, +1 buffer)
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
            "name": f"{job} Level Increased by 5",
            "category": [f"{job}", "DOL"],
            "count": 20,  # Levels 5-100 (95 levels / 5 = 19, +1 buffer)
            "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal",
            "category": ["Job Crystal", "DOL"],
            "count": 1,
            "progression": True,
        })
    
    # Dungeons and Trials from duties.csv
    # ARR Dungeons
    dungeons_arr = [
        "Sastasha", "The Tam-Tara Deepcroft", "Copperbell Mines", "Halatali", 
        "The Thousand Maws of Toto-Rak", "Haukke Manor", "Brayflox's Longstop", 
        "The Sunken Temple of Qarn", "Cutter's Cry", "The Stone Vigil", 
        "Dzemael Darkhold", "The Aurum Vale", "Castrum Meridianum", "The Praetorium",
        "The Wanderer's Palace", "Amdapor Keep", "Pharos Sirius", "Copperbell Mines (Hard)",
        "Haukke Manor (Hard)", "The Lost City of Amdapor", "Halatali (Hard)", 
        "Brayflox's Longstop (Hard)", "Hullbreaker Isle", "The Tam-Tara Deepcroft (Hard)",
        "The Stone Vigil (Hard)", "Snowcloak", "Sastasha (Hard)", 
        "The Sunken Temple of Qarn (Hard)", "The Keeper of the Lake", 
        "The Wanderer's Palace (Hard)", "Amdapor Keep (Hard)"
    ]
    
    for dungeon in dungeons_arr:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "ARR"],
            "count": 1,
        })

    # ARR Trials
    trials_arr = [
        "The Bowl of Embers", "The Navel", "The Howling Eye", "The Porta Decumana",
        "The Bowl of Embers (Hard)", "The Howling Eye (Hard)", "The Navel (Hard)",
        "Thornmarch (Hard)", "A Relic Reborn: the Chimera", "A Relic Reborn: the Hydra",
        "The Whorleater (Hard)", "Battle on the Big Bridge", "The Striking Tree (Hard)",
        "The Akh Afah Amphitheatre (Hard)", "The Dragon's Neck", "The Chrysalis",
        "Battle in the Big Keep", "Urth's Fount", "The Minstrel's Ballad: Ultima's Bane",
        "The Howling Eye (Extreme)", "The Navel (Extreme)", "The Bowl of Embers (Extreme)",
        "Thornmarch (Extreme)", "The Whorleater (Extreme)", "The Striking Tree (Extreme)",
        "The Akh Afah Amphitheatre (Extreme)"
    ]
    
    for trial in trials_arr:
        item_table.append({
            "name": trial,
            "category": ["Trial", "ARR"],
            "count": 1,
        })

    # HW Dungeons
    dungeons_hw = [
        "The Dusk Vigil", "Sohm Al", "The Aery", "The Vault", "The Great Gubal Library",
        "The Aetherochemical Research Facility", "Neverreap", "The Fractal Continuum",
        "Saint Mocianne's Arboretum", "Pharos Sirius (Hard)", "The Antitower",
        "The Lost City of Amdapor (Hard)", "Sohr Khai", "Hullbreaker Isle (Hard)",
        "Xelphatol", "The Great Gubal Library (Hard)", "Baelsar's Wall", "Sohm Al (Hard)"
    ]
    
    for dungeon in dungeons_hw:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "HW"],
            "count": 1,
        })

    # HW Trials
    trials_hw = [
        "Thok ast Thok (Hard)", "The Limitless Blue (Hard)", "The Singularity Reactor",
        "Containment Bay S1T7", "The Final Steps of Faith", "Containment Bay P1T6",
        "Containment Bay Z1T9", "The Limitless Blue (Extreme)", "Thok ast Thok (Extreme)",
        "The Minstrel's Ballad: Thordan's Reign", "Containment Bay S1T7 (Extreme)",
        "The Minstrel's Ballad: Nidhogg's Rage", "Containment Bay P1T6 (Extreme)",
        "Containment Bay Z1T9 (Extreme)"
    ]
    
    for trial in trials_hw:
        item_table.append({
            "name": trial,
            "category": ["Trial", "HW"],
            "count": 1,
        })

    # StB Dungeons
    dungeons_stb = [
        "The Sirensong Sea", "Shisui of the Violet Tides", "Bardam's Mettle", "Doma Castle",
        "Castrum Abania", "Ala Mhigo", "Kugane Castle", "The Temple of the Fist",
        "The Drowned City of Skalla", "Hells' Lid", "The Fractal Continuum (Hard)",
        "The Swallow's Compass", "The Burn", "Saint Mocianne's Arboretum (Hard)",
        "The Ghimlyt Dark"
    ]
    
    for dungeon in dungeons_stb:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "StB"],
            "count": 1,
        })

    # StB Trials
    trials_stb = [
        "The Pool of Tribute", "Emanation", "The Royal Menagerie", "The Jade Stoa",
        "Castrum Fluminis", "The Great Hunt", "Hells' Kier", "The Wreath of Snakes",
        "Kugane Ohashi", "The Pool of Tribute (Extreme)", "Emanation (Extreme)",
        "The Minstrel's Ballad: Shinryu's Domain", "The Jade Stoa (Extreme)",
        "The Minstrel's Ballad: Tsukuyomi's Pain", "The Great Hunt (Extreme)",
        "Hells' Kier (Extreme)", "The Wreath of Snakes (Extreme)"
    ]
    
    for trial in trials_stb:
        item_table.append({
            "name": trial,
            "category": ["Trial", "StB"],
            "count": 1,
        })

    # ShB Dungeons
    dungeons_shb = [
        "Holminster Switch", "Dohn Mheg", "The Qitana Ravel", "Malikah's Well",
        "Mt. Gulg", "Amaurot", "The Twinning", "Akadaemia Anyder", "The Grand Cosmos",
        "Anamnesis Anyder", "The Heroes' Gauntlet", "Matoya's Relict", "Paglth'an"
    ]
    
    for dungeon in dungeons_shb:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "ShB"],
            "count": 1,
        })

    # ShB Trials
    trials_shb = [
        "The Dancing Plague", "The Crown of the Immaculate", "The Dying Gasp",
        "Cinder Drift", "The Seat of Sacrifice", "Castrum Marinum", "The Cloud Deck",
        "The Dancing Plague (Extreme)", "The Crown of the Immaculate (Extreme)",
        "The Minstrel's Ballad: Hades's Elegy", "Cinder Drift (Extreme)",
        "Memoria Misera (Extreme)", "The Seat of Sacrifice (Extreme)",
        "Castrum Marinum (Extreme)", "The Cloud Deck (Extreme)"
    ]
    
    for trial in trials_shb:
        item_table.append({
            "name": trial,
            "category": ["Trial", "ShB"],
            "count": 1,
        })

    # EW Dungeons
    dungeons_ew = [
        "The Tower of Zot", "The Tower of Babil", "Vanaspati", "Ktisis Hyperboreia",
        "The Aitiascope", "The Dead Ends", "Smileton", "The Stigma Dreamscape",
        "Alzadaal's Legacy", "The Fell Court of Troia", "Lapis Manalis",
        "The Aetherfont", "The Lunar Subterrane"
    ]
    
    for dungeon in dungeons_ew:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "EW"],
            "count": 1,
        })

    # EW Trials
    trials_ew = [
        "The Dark Inside", "The Mothercrystal", "The Final Day", "Storm's Crown",
        "Mount Ordeals", "The Voidcast Dais", "The Abyssal Fracture", "The Gilded Araya",
        "The Minstrel's Ballad: Zodiark's Fall", "The Minstrel's Ballad: Hydaelyn's Call",
        "The Minstrel's Ballad: Endsinger's Aria", "Storm's Crown (Extreme)",
        "Mount Ordeals (Extreme)", "The Voidcast Dais (Extreme)", "The Abyssal Fracture (Extreme)"
    ]
    
    for trial in trials_ew:
        item_table.append({
            "name": trial,
            "category": ["Trial", "EW"],
            "count": 1,
        })

    # DT Dungeons
    dungeons_dt = [
        "Ihuykatumu", "Worqor Zormor", "The Skydeep Cenote", "Vanguard", "Origenics",
        "Alexandria", "Tender Valley", "The Strayborough Deadwalk", "Yuweyawata Field Station",
        "The Underkeep", "The Meso Terminal"
    ]
    
    for dungeon in dungeons_dt:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "DT"],
            "count": 1,
        })

    # DT Trials
    trials_dt = [
        "Worqor Lar Dor", "Everkeep", "The Interphos", "Recollection", "The Ageless Necropolis",
        "Worqor Lar Dor (Extreme)", "Everkeep (Extreme)", "The Minstrel's Ballad: Sphene's Burden",
        "Recollection (Extreme)", "The Minstrel's Ballad: Necron's Embrace"
    ]
    
    for trial in trials_dt:
        item_table.append({
            "name": trial,
            "category": ["Trial", "DT"],
            "count": 1,
        })
    
    return item_table
    
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

    # Add level locations every 2 levels for each job
    for job in ARR_JOB:
        for level in range(2, 101, 2):  # Every 2 levels from 2 to 100
            if level <= 10:
                # Levels 2-10 are free with job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal|"
                })
            else:
                # Calculate items needed based on 5-level increments
                items_needed = (level - 10) // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal|"
                })

    for job in HW_JOB:
        for level in range(30, 101, 2):  # Every 2 levels from 30 to 100
            if level <= 50:
                # Levels 30-50 require Level 50 Access
                items_needed = (level - 30) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 50 Access|"
                })
            elif level <= 60:
                # Levels 52-60 require Level 60 Access
                items_needed = (level - 30) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 60 Access|"
                })
            elif level <= 70:
                # Levels 62-70 require Level 70 Access
                items_needed = (level - 30) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            elif level <= 80:
                # Levels 72-80 require Level 80 Access
                items_needed = (level - 30) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = (level - 30) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    for job in STB_JOB:
        for level in range(50, 101, 2):  # Every 2 levels from 50 to 100
            if level <= 60:
                # Levels 50-60 require Level 50 Access
                items_needed = (level - 50) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 50 Access|"
                })
            elif level <= 70:
                # Levels 62-70 require Level 60 Access
                items_needed = (level - 50) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 60 Access|"
                })
            elif level <= 80:
                # Levels 72-80 require Level 70 Access
                items_needed = (level - 50) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = (level - 50) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    for job in SHB_JOB:
        for level in range(60, 101, 2):  # Every 2 levels from 60 to 100
            if level <= 70:
                # Levels 60-70 require Level 60 Access
                items_needed = (level - 60) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 60 Access|"
                })
            elif level <= 80:
                # Levels 72-80 require Level 70 Access
                items_needed = (level - 60) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = (level - 60) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    for job in EW_JOB:
        for level in range(70, 101, 2):  # Every 2 levels from 70 to 100
            if level <= 80:
                # Levels 70-80 require Level 70 Access
                items_needed = (level - 70) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = (level - 70) // 5 + 1
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    for job in DT_JOB:
        for level in range(80, 101, 2):  # Every 2 levels from 80 to 100
            # All DT job levels require Level 80 Access
            items_needed = (level - 80) // 5 + 1
            location_table.append({
                "name": f"{job} Level {level}",
                "category": [f"{job}", "DOW/DOM"],
                "region": f"{job}",
                "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
            })

    # BLU levels every 2 (max 80) - starts at level 1, requires Level 50 Access
    for level in range(2, 81, 2):  # Every 2 levels from 2 to 80
        if level <= 50:
            # Levels 2-50 require Level 50 Access
            items_needed = level // 5
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal| and |Level 50 Access|"
            })
        elif level <= 60:
            # Levels 52-60 require Level 60 Access
            items_needed = level // 5
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal| and |Level 60 Access|"
            })
        elif level <= 70:
            # Levels 62-70 require Level 70 Access
            items_needed = level // 5
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal| and |Level 70 Access|"
            })
        else:
            # Levels 72-80 require Level 80 Access
            items_needed = level // 5
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal| and |Level 80 Access|"
            })

    # DOH levels every 2 - starts at level 1, requires Level 15 Access
    for job in DOH:
        for level in range(2, 101, 2):  # Every 2 levels from 2 to 100
            if level <= 50:
                # Levels 2-50 require Level 15 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 15 Access|"
                })
            elif level <= 60:
                # Levels 52-60 require Level 50 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 50 Access|"
                })
            elif level <= 70:
                # Levels 62-70 require Level 60 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 60 Access|"
                })
            elif level <= 80:
                # Levels 72-80 require Level 70 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    # DOL levels every 2 - starts at level 1, requires Level 15 Access
    for job in DOL:
        for level in range(2, 101, 2):  # Every 2 levels from 2 to 100
            if level <= 50:
                # Levels 2-50 require Level 15 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 15 Access|"
                })
            elif level <= 60:
                # Levels 52-60 require Level 50 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 50 Access|"
                })
            elif level <= 70:
                # Levels 62-70 require Level 60 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 60 Access|"
                })
            elif level <= 80:
                # Levels 72-80 require Level 70 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 70 Access|"
                })
            else:
                # Levels 82-100 require Level 80 Access
                items_needed = level // 5
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal| and |Level 80 Access|"
                })

    return location_table

def after_load_region_file(region_table: dict) -> dict:
    # All non-ARR job regions for connections
    all_other_jobs = ["DRK", "MCH", "AST", "SAM", "RDM", "GNB", "DNC", "RPR", "SGE", "VPR", "PCT", "CRP", "BSM", "ARM", "GSM", "LTW", "WVR", "ALC", "CUL", "MIN", "BTN", "FSH", "BLU"]

    # ARR Jobs - Starting regions that connect to ALL other job regions
    for job in ARR_JOB:
        region_table[job] = {
            "starting": True,
            "connects_to": all_other_jobs,
            "requires": f"|{job} Job Crystal|"  # Require specific job crystal
        }

    # DOH Jobs - Level 15 requirement + specific job crystal
    for job in DOH:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 15 Access| and |{job} Job Crystal|"
        }

    # DOL Jobs - Level 15 requirement + specific job crystal
    for job in DOL:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 15 Access| and |{job} Job Crystal|"
        }

    # HW Jobs - Level 50 requirement + specific job crystal
    for job in HW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 50 Access| and |{job} Job Crystal|"
        }

    # STB Jobs - Level 50 requirement + specific job crystal
    for job in STB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 50 Access| and |{job} Job Crystal|"
        }

    # BLU - Level 50 requirement + specific job crystal
    region_table["BLU"] = {
        "starting": False,
        "connects_to": [],
        "requires": "|Level 50 Access| and |BLU Job Crystal|"
    }

    # SHB Jobs - Level 60 requirement + specific job crystal
    for job in SHB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 60 Access| and |{job} Job Crystal|"
        }

    # EW Jobs - Level 70 requirement + specific job crystal
    for job in EW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 70 Access| and |{job} Job Crystal|"
        }

    # DT Jobs - Level 80 requirement + specific job crystal
    for job in DT_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 80 Access| and |{job} Job Crystal|"
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