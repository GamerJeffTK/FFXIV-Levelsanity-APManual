# hooks/Data.py - Simplified version without Level Gate items

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
    
    # REMOVED: Level gate items - using anyClassLevel function instead
    
    # ARR Jobs
    for job in ARR_JOB:
        # Level increases - using "Level Increased by 5" naming
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 18,  # Each gives 5 levels, need 18 for levels 15-100 (85 levels / 5 = 17, +1 buffer)
           "progression": True,
        })

        # Job unlock - All ARR jobs get "ARR Starter Job" category with default cap
        item_table.append({
            "name": f"{job} Job Crystal (default cap 10)",
            "category": ["Job Crystal", "DOW/DOM", "ARR Starter Job"],
            "count": 1,
            "early": True,
            "progression": True,
        })

    # HW Jobs
    for job in HW_JOB:
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 14,  # Levels 35-100 (65 levels / 5 = 13, +1 buffer)
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 30)",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # STB Jobs
    for job in STB_JOB:
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 11,  # Levels 55-100 (45 levels / 5 = 9, +2 buffer)
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 50)",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # SHB Jobs
    for job in SHB_JOB:
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 9,  # Levels 65-100 (35 levels / 5 = 7, +2 buffer)
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 60)",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # EW Jobs
    for job in EW_JOB:
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 7,  # Levels 75-100 (25 levels / 5 = 5, +2 buffer)
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 70)",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # DT Jobs
    for job in DT_JOB:
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 5,  # Levels 85-100 (15 levels / 5 = 3, +2 buffer)
           "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 80)",
            "category": ["Job Crystal", "DOW/DOM"],
            "count": 1,
            "progression": True,
        })

    # BLU
    item_table.append({
        "name": "BLU Level Increased by 5",
        "category": ["BLU Level Progression", "DOW/DOM", "Level Progression"],
        "count": 16,  # Levels 5-80 (75 levels / 5 = 15, +1 buffer)
        "progression": True,
    })

    item_table.append({
        "name": "BLU Job Crystal (default cap 5)",
        "category": ["Job Crystal", "DOW/DOM"],
        "count": 1,
        "progression": True,
    })

    # DOH Jobs
    for job in DOH:
        item_table.append({
            "name": f"{job} Level Increased by 5",
            "category": [f"{job} Level Progression", "DOH", "Level Progression"],
            "count": 20,  # Levels 5-100 (95 levels / 5 = 19, +1 buffer)
            "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 5)",
            "category": ["DOH Job Crystal", "DOH"],
            "count": 1,
            "progression": True,
        })

    # DOL Jobs
    for job in DOL:
        item_table.append({
            "name": f"{job} Level Increased by 5",
            "category": [f"{job} Level Progression", "DOL", "Level Progression"],
            "count": 20,  # Levels 5-100 (95 levels / 5 = 19, +1 buffer)
            "progression": True,
        })

        item_table.append({
            "name": f"{job} Job Crystal (default cap 5)",
            "category": ["DOL Job Crystal", "DOL"],
            "count": 1,
            "progression": True,
        })
    
    # Dungeons and Trials from duties.csv - ALL PROGRESSION ITEMS
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
            "category": ["Dungeon", "ARR", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "ARR", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Dungeon", "HW", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "HW", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Dungeon", "StB", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "StB", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Dungeon", "ShB", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "ShB", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Dungeon", "EW", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "EW", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Dungeon", "DT", "Duty"],
            "count": 1,
            "progression": True,
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
            "category": ["Trial", "DT", "Duty"],
            "count": 1,
            "progression": True,
        })
    
    # Alliance Raids - Major 24-player content
    alliance_raids = [
        # Crystal Tower (ARR)
        "The Labyrinth of the Ancients", "Syrcus Tower", "The World of Darkness",
        
        # Shadow of Mhach (HW)
        "The Void Ark", "The Weeping City of Mhach", "Dun Scaith",
        
        # Return to Ivalice (StB)
        "The Royal City of Rabanastre", "The Ridorana Lighthouse", "The Orbonne Monastery",
        
        # YoRHa Dark Apocalypse (ShB)
        "The Copied Factory", "The Puppets' Bunker", "The Tower at Paradigm's Breach",
        
        # Myths of the Realm (EW)
        "Aglaia", "Euphrosyne", "Thaleia",
        
        # Jeuno Alliance (DT)
        "Jeuno: The First Walk", "San d'Oria: The Second Walk"
    ]
    
    # Categorize alliance raids by expansion
    alliance_raid_expansions = {
        "The Labyrinth of the Ancients": "ARR", "Syrcus Tower": "ARR", "The World of Darkness": "ARR",
        "The Void Ark": "HW", "The Weeping City of Mhach": "HW", "Dun Scaith": "HW",
        "The Royal City of Rabanastre": "StB", "The Ridorana Lighthouse": "StB", "The Orbonne Monastery": "StB",
        "The Copied Factory": "ShB", "The Puppets' Bunker": "ShB", "The Tower at Paradigm's Breach": "ShB",
        "Aglaia": "EW", "Euphrosyne": "EW", "Thaleia": "EW",
        "Jeuno: The First Walk": "DT", "San d'Oria: The Second Walk": "DT"
    }
    
    for raid in alliance_raids:
        expansion = alliance_raid_expansions[raid]
        item_table.append({
            "name": raid,
            "category": ["Alliance Raid", expansion, "Duty"],
            "count": 1,
            "progression": True,
        })

    # Normal Raids (8-player raid content) - abbreviated for space
    normal_raids_data = [
        # ARR
        ("The Binding Coil of Bahamut - Turn 1", "ARR"),
        ("The Binding Coil of Bahamut - Turn 2", "ARR"),
        ("The Binding Coil of Bahamut - Turn 3", "ARR"),
        ("The Binding Coil of Bahamut - Turn 4", "ARR"),
        ("The Binding Coil of Bahamut - Turn 5", "ARR"),
        ("The Second Coil of Bahamut - Turn 1", "ARR"),
        ("The Second Coil of Bahamut - Turn 2", "ARR"),
        ("The Second Coil of Bahamut - Turn 3", "ARR"),
        ("The Second Coil of Bahamut - Turn 4", "ARR"),
        ("The Final Coil of Bahamut - Turn 1", "ARR"),
        ("The Final Coil of Bahamut - Turn 2", "ARR"),
        ("The Final Coil of Bahamut - Turn 3", "ARR"),
        ("The Final Coil of Bahamut - Turn 4", "ARR"),
        
        # HW
        ("Alexander - The Fist of the Father", "HW"),
        ("Alexander - The Cuff of the Father", "HW"),
        ("Alexander - The Arm of the Father", "HW"),
        ("Alexander - The Burden of the Father", "HW"),
        
        # StB
        ("Deltascape V1.0", "StB"),
        ("Deltascape V2.0", "StB"),
        ("Deltascape V3.0", "StB"),
        ("Deltascape V4.0", "StB"),
        
        # ShB
        ("Eden's Gate: Resurrection", "ShB"),
        ("Eden's Gate: Descent", "ShB"),
        ("Eden's Gate: Inundation", "ShB"),
        ("Eden's Gate: Sepulture", "ShB"),
        
        # EW
        ("Asphodelos: The First Circle", "EW"),
        ("Asphodelos: The Second Circle", "EW"),
        ("Asphodelos: The Third Circle", "EW"),
        ("Asphodelos: The Fourth Circle", "EW"),
        
        # DT
        ("AAC Light-heavyweight M1", "DT"),
        ("AAC Light-heavyweight M2", "DT"),
        ("AAC Light-heavyweight M3", "DT"),
        ("AAC Light-heavyweight M4", "DT")
    ]
    
    for raid, expansion in normal_raids_data:
        item_table.append({
            "name": raid,
            "category": ["Normal Raid", expansion, "Duty"],
            "count": 1,
            "progression": True,
        })

    # Savage Raids - Limited examples
    savage_raids_data = [
        ("The Second Coil of Bahamut (Savage) - Turn 1", "ARR"),
        ("The Second Coil of Bahamut (Savage) - Turn 2", "ARR"),
        ("Alexander - The Fist of the Father (Savage)", "HW"),
        ("Alexander - The Cuff of the Father (Savage)", "HW")
    ]
    
    for raid, expansion in savage_raids_data:
        item_table.append({
            "name": raid,
            "category": ["Savage Raid", expansion, "Duty"],
            "count": 1,
            "progression": True,
        })

    # Guildhests - Tutorial group content (ARR only)
    guildhests = [
        "Basic Training: Enemy Parties", "Under the Armor", "Basic Training: Enemy Strongholds",
        "Hero on the Half Shell", "Pulling Poison Posies", "Stinging Back",
        "All's Well that Ends in the Well", "Flicking Sticks and Taking Names",
        "More than a Feeler", "Annoy the Void", "Shadow and Claw",
        "Long Live the Queen", "Ward Up", "Solemn Trinity"
    ]
    
    for guildhest in guildhests:
        item_table.append({
            "name": guildhest,
            "category": ["Guildhest", "ARR", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Variant Dungeons (EW)
    variant_dungeons = ["The Sil'dihn Subterrane", "Mount Rokkon", "Aloalo Island"]
    
    for variant in variant_dungeons:
        item_table.append({
            "name": variant,
            "category": ["Variant Dungeon", "EW", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Bozja Content (ShB)
    bozja_content = ["Castrum Lacus Litore", "Delubrum Reginae", "The Dalriada"]
    
    for bozja in bozja_content:
        item_table.append({
            "name": bozja,
            "category": ["Bozja", "ShB", "Duty"],
            "count": 1,
            "progression": True,
        })
    
    # Add Faded Job Crystals for victory condition validation
    # This prevents validation errors regardless of which victory condition is selected
    # The actual count will be adjusted later in World.py based on the selected goal
    item_table.append({
        "name": "A Faded Job Crystal",
        "category": ["Victory Item"],
        "count": 50,  # Default count for validation - will be adjusted in World.py
        "progression": True,
    })
    
    return item_table

def after_load_location_file(location_table: list) -> list:
    
    # Add early accessible starter locations in Manual region for early job crystals and items
    # These don't require any job crystals, making them perfect for early placement
    starter_locations = [
        "Begin Your Adventure",
        "Complete Character Creation", 
        "Finish Opening Cutscene",
        "Reach Level 5 on Any Job",
        "Reach Level 10 on Any Job", 
        "Unlock Your First Dungeon",
        "Complete Your First Guildhest",
        "Join a Grand Company",
        "Unlock Retainers",
        "Complete Main Story Quest: The Gridanian Envoy",
        "Complete Main Story Quest: The Ul'dahn Envoy", 
        "Complete Main Story Quest: The Lominsan Envoy",
        "Unlock Chocobo Companion",
        "Complete First Class Quest",
        "Visit All Three Starting Cities",
        "Unlock Market Board Access",
        "Unlock Aetheryte System",
        "Complete Tutorial: Combat Basics",
        "Complete Tutorial: Equipment Basics",
        "Complete Tutorial: Inventory Management",
        "Reach Level 15 on Any Job",
        "Earn 1,000 Gil",
        "Equip Your First Weapon",
        "Learn Your First Combat Skill"
    ]
    
    for location in starter_locations:
        location_table.append({
            "name": location,
            "category": ["Starter"],
            "region": "Manual",
            # No requires - these are always accessible for early item placement
        })
    
    # Add level locations every level for each job
    for job in ARR_JOB:
        for level in range(1, 101):  # Every level from 1 to 100
            if level <= 10:
                # Levels 1-10 are free with job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 10)|"
                })
            else:
                # Calculate items needed based on 5-level increments
                items_needed = (level - 10 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 10)|"
                })

    for job in HW_JOB:
        for level in range(30, 101):  # Every level from 30 to 100
            if level <= 30:
                # Level 30 requires level 50 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 30)| and {{anyClassLevel(50)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 30
                items_needed = (level - 30 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 30)| and {{anyClassLevel(50)}}"
                })

    for job in STB_JOB:
        for level in range(50, 101):  # Every level from 50 to 100
            if level <= 50:
                # Level 50 requires level 50 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 50)| and {{anyClassLevel(50)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 50
                items_needed = (level - 50 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 50)| and {{anyClassLevel(50)}}"
                })

    for job in SHB_JOB:
        for level in range(60, 101):  # Every level from 60 to 100
            if level <= 60:
                # Level 60 requires level 60 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 60)| and {{anyClassLevel(60)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 60
                items_needed = (level - 60 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 60)| and {{anyClassLevel(60)}}"
                })

    for job in EW_JOB:
        for level in range(70, 101):  # Every level from 70 to 100
            if level <= 70:
                # Level 70 requires level 70 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 70)| and {{anyClassLevel(70)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 70
                items_needed = (level - 70 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 70)| and {{anyClassLevel(70)}}"
                })

    for job in DT_JOB:
        for level in range(80, 101):  # Every level from 80 to 100
            if level <= 80:
                # Level 80 requires level 80 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 80)| and {{anyClassLevel(80)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 80
                items_needed = (level - 80 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 80)| and {{anyClassLevel(80)}}"
                })

    # BLU levels (max 80) - starts at level 1, requires level 50 on any job
    for level in range(1, 81):  # Every level from 1 to 80
        if level <= 5:
            # Levels 1-5 require level 50 on any job and job crystal
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Job Crystal (default cap 5)| and {{anyClassLevel(50)}}"
            })
        else:
            # Calculate items needed based on 5-level increments from 5
            items_needed = (level - 5 + 4) // 5  # Round up division
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal (default cap 5)| and {{anyClassLevel(50)}}"
            })

    # DOH levels - starts at level 1, requires level 15 on any job
    for job in DOH:
        for level in range(1, 101):  # Every level from 1 to 100
            if level <= 5:
                # Levels 1-5 require level 15 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 5)| and {{anyClassLevel(15)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 5
                items_needed = (level - 5 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOH"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 5)| and {{anyClassLevel(15)}}"
                })

    # DOL levels - starts at level 1, requires level 15 on any job
    for job in DOL:
        for level in range(1, 101):  # Every level from 1 to 100
            if level <= 5:
                # Levels 1-5 require level 15 on any job and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 5)| and {{anyClassLevel(15)}}"
                })
            else:
                # Calculate items needed based on 5-level increments from 5
                items_needed = (level - 5 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOL"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 5)| and {{anyClassLevel(15)}}"
                })

    # Simple duty completion locations - using anyClassLevel directly
    key_duties = [
        {"name": "Sastasha", "level": 18, "requires": "{anyClassLevel(18)}"},
        {"name": "The Praetorium", "level": 50, "requires": "{anyClassLevel(50)}"},
        {"name": "The Vault", "level": 58, "requires": "{anyClassLevel(58)}"},  # Simplified - HW content just needs level
        {"name": "Ala Mhigo", "level": 70, "requires": "{anyClassLevel(70)}"},  # Simplified - StB content just needs level
        {"name": "Amaurot", "level": 80, "requires": "{anyClassLevel(80)}"},   # Simplified - ShB content just needs level
        {"name": "The Dead Ends", "level": 90, "requires": "{anyClassLevel(90)}"}, # Simplified - EW content just needs level
        {"name": "Alexandria", "level": 100, "requires": "{anyClassLevel(100)}"}   # Simplified - DT content just needs level
    ]
    
    for duty in key_duties:
        location_table.append({
            "name": f"Complete {duty['name']}",
            "category": ["Duty"],
            "region": "Manual",
            "requires": duty["requires"]
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
            "requires": f"|{job} Job Crystal (default cap 10)|"  # Require specific job crystal with cap
        }

    # DOH Jobs - Level 15 requirement + specific job crystal
    for job in DOH:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(15)}} and |{job} Job Crystal (default cap 5)|"  # Using anyClassLevel directly
        }

    # DOL Jobs - Level 15 requirement + specific job crystal
    for job in DOL:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(15)}} and |{job} Job Crystal (default cap 5)|"  # Using anyClassLevel directly
        }

    # HW Jobs - Level 50 requirement + specific job crystal
    for job in HW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(50)}} and |{job} Job Crystal (default cap 30)|"  # Using anyClassLevel directly
        }

    # STB Jobs - Level 50 requirement + specific job crystal
    for job in STB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(50)}} and |{job} Job Crystal (default cap 50)|"  # Using anyClassLevel directly
        }

    # BLU - Level 50 requirement + specific job crystal
    region_table["BLU"] = {
        "starting": False,
        "connects_to": [],
        "requires": "{anyClassLevel(50)} and |BLU Job Crystal (default cap 5)|"  # Using anyClassLevel directly
    }

    # SHB Jobs - Level 60 requirement + specific job crystal
    for job in SHB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(60)}} and |{job} Job Crystal (default cap 60)|"  # Using anyClassLevel directly
        }

    # EW Jobs - Level 70 requirement + specific job crystal
    for job in EW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(70)}} and |{job} Job Crystal (default cap 70)|"  # Using anyClassLevel directly
        }

    # DT Jobs - Level 80 requirement + specific job crystal
    for job in DT_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"{{anyClassLevel(80)}} and |{job} Job Crystal (default cap 80)|"  # Using anyClassLevel directly
        }

    return region_table

def after_load_category_file(category_table: dict) -> dict:
    # Keep categories simple - all jobs get categories but some are hidden based on expansion selection
    for job in ARR_JOB + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL + ["BLU"]:
        category_table[job] = {}
    
    # Hide broad job type categories
    category_table["DOW/DOM"] = {"hidden": True}
    category_table["DOL"] = {"hidden": True}
    category_table["DOH"] = {"hidden": True}
    category_table["Level Progression"] = {"hidden": True}
    
    # Add expansion-based categories
    category_table["ARR"] = {"hidden": True}
    category_table["HW"] = {"hidden": True}
    category_table["StB"] = {"hidden": True}
    category_table["ShB"] = {"hidden": True}
    category_table["EW"] = {"hidden": True}
    category_table["DT"] = {"hidden": True}
    
    return category_table

def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

def after_load_option_file(option_table: dict) -> dict:
    return option_table

def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> dict | bool:
    return False