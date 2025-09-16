# hooks/Data.py - Fixed version with early duties and proper logic

# called after the game.json file has been loaded
def after_load_game_file(game_table: dict) -> dict:
    return game_table

ARR_JOB = ["PLD","WAR","DRG","MNK","BRD","BLM","WHM","SMN/SCH"]
ARR_NON_STARTER = ["NIN"]  # NIN is ARR but not a starter job
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
        # Level increases - back to all being early
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 18,  # Each gives 5 levels, need 18 for levels 15-100 (85 levels / 5 = 17, +1 buffer)
           "early": True,
           "progression": True,
        })

        # Job unlock - All ARR jobs get "ARR Starter Job" category
        item_table.append({
            "name": f"{job} Job Crystal (default cap 10)",
            "category": ["Job Crystal", "DOW/DOM", "ARR Starter Job"],
            "count": 1,
            "early": True,
            "progression": True,
        })

    # ARR Non-Starter Jobs (like NIN)
    for job in ARR_NON_STARTER:
        # Level increases
        item_table.append({
           "name": f"{job} Level Increased by 5",
           "category": [f"{job} Level Progression", "DOW/DOM", "Level Progression"],
           "count": 18,
           "early": True,
           "progression": True,
        })

        # Job unlock - ARR job but NOT starter job
        item_table.append({
            "name": f"{job} Job Crystal (default cap 10)",
            "category": ["Job Crystal", "DOW/DOM"],  # No "ARR Starter Job" category
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

        # All DOH job crystals are early again
        item_table.append({
            "name": f"{job} Job Crystal (default cap 5)",
            "category": ["DOH Job Crystal", "DOH"],
            "count": 1,
            "early": True,
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

        # All DOL job crystals are early again
        item_table.append({
            "name": f"{job} Job Crystal (default cap 5)",
            "category": ["DOL Job Crystal", "DOL"],
            "count": 1,
            "early": True,
            "progression": True,
        })
    
    # Dungeons and Trials from duties.csv - ALL PROGRESSION ITEMS
    # ARR Dungeons - Early ones marked as early
    dungeons_arr_early = [
        # Level < 35 dungeons - these should be early
        "Sastasha", "The Tam-Tara Deepcroft", "Copperbell Mines", "Halatali", 
        "The Thousand Maws of Toto-Rak", "Haukke Manor", "Brayflox's Longstop"
    ]
    
    dungeons_arr_regular = [
        "The Sunken Temple of Qarn", "Cutter's Cry", "The Stone Vigil", 
        "Dzemael Darkhold", "The Aurum Vale", "Castrum Meridianum", "The Praetorium",
        "The Wanderer's Palace", "Amdapor Keep", "Pharos Sirius", "Copperbell Mines (Hard)",
        "Haukke Manor (Hard)", "The Lost City of Amdapor", "Halatali (Hard)", 
        "Brayflox's Longstop (Hard)", "Hullbreaker Isle", "The Tam-Tara Deepcroft (Hard)",
        "The Stone Vigil (Hard)", "Snowcloak", "Sastasha (Hard)", 
        "The Sunken Temple of Qarn (Hard)", "The Keeper of the Lake", 
        "The Wanderer's Palace (Hard)", "Amdapor Keep (Hard)"
    ]
    
    # Early dungeons
    for dungeon in dungeons_arr_early:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "ARR", "Duty", "Early Duty"],
            "count": 1,
            "early": True,
            "progression": True,
        })
    
    # Regular ARR dungeons
    for dungeon in dungeons_arr_regular:
        item_table.append({
            "name": dungeon,
            "category": ["Dungeon", "ARR", "Duty"],
            "count": 1,
            "progression": True,
        })

    # ARR Trials - Early ones marked as early
    trials_arr_early = [
        "The Bowl of Embers",  # Level 22
    ]
    
    trials_arr_regular = [
        "The Navel", "The Howling Eye", "The Porta Decumana",
        "The Bowl of Embers (Hard)", "The Howling Eye (Hard)", "The Navel (Hard)",
        "Thornmarch (Hard)", "A Relic Reborn: the Chimera", "A Relic Reborn: the Hydra",
        "The Whorleater (Hard)", "Battle on the Big Bridge", "The Striking Tree (Hard)",
        "The Akh Afah Amphitheatre (Hard)", "The Dragon's Neck", "The Chrysalis",
        "Battle in the Big Keep", "Urth's Fount", "The Minstrel's Ballad: Ultima's Bane",
        "The Howling Eye (Extreme)", "The Navel (Extreme)", "The Bowl of Embers (Extreme)",
        "Thornmarch (Extreme)", "The Whorleater (Extreme)", "The Striking Tree (Extreme)",
        "The Akh Afah Amphitheatre (Extreme)"
    ]
    
    # Early trials
    for trial in trials_arr_early:
        item_table.append({
            "name": trial,
            "category": ["Trial", "ARR", "Duty", "Early Duty"],
            "count": 1,
            "early": True,
            "progression": True,
        })
    
    # Regular ARR trials
    for trial in trials_arr_regular:
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
    
    for raid in alliance_raids:
        item_table.append({
            "name": raid,
            "category": ["Alliance Raid", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Normal Raids (8-player raid content)
    normal_raids = [
        # Binding Coil of Bahamut (ARR)
        "The Binding Coil of Bahamut - Turn 1", "The Binding Coil of Bahamut - Turn 2",
        "The Binding Coil of Bahamut - Turn 3", "The Binding Coil of Bahamut - Turn 4",
        "The Binding Coil of Bahamut - Turn 5", "The Second Coil of Bahamut - Turn 1",
        "The Second Coil of Bahamut - Turn 2", "The Second Coil of Bahamut - Turn 3",
        "The Second Coil of Bahamut - Turn 4", "The Final Coil of Bahamut - Turn 1",
        "The Final Coil of Bahamut - Turn 2", "The Final Coil of Bahamut - Turn 3",
        "The Final Coil of Bahamut - Turn 4",
        
        # Alexander (HW)
        "Alexander - The Fist of the Father", "Alexander - The Cuff of the Father",
        "Alexander - The Arm of the Father", "Alexander - The Burden of the Father",
        "Alexander - The Fist of the Son", "Alexander - The Cuff of the Son",
        "Alexander - The Arm of the Son", "Alexander - The Burden of the Son",
        "Alexander - The Eyes of the Creator", "Alexander - The Breath of the Creator",
        "Alexander - The Heart of the Creator", "Alexander - The Soul of the Creator",
        
        # Omega (StB)
        "Deltascape V1.0", "Deltascape V2.0", "Deltascape V3.0", "Deltascape V4.0",
        "Sigmascape V1.0", "Sigmascape V2.0", "Sigmascape V3.0", "Sigmascape V4.0",
        "Alphascape V1.0", "Alphascape V2.0", "Alphascape V3.0", "Alphascape V4.0",
        
        # Eden (ShB)
        "Eden's Gate: Resurrection", "Eden's Gate: Descent", "Eden's Gate: Inundation", "Eden's Gate: Sepulture",
        "Eden's Verse: Fulmination", "Eden's Verse: Furor", "Eden's Verse: Iconoclasm", "Eden's Verse: Refulgence",
        "Eden's Promise: Umbra", "Eden's Promise: Litany", "Eden's Promise: Anamorphosis", "Eden's Promise: Eternity",
        
        # Pandaemonium (EW)
        "Asphodelos: The First Circle", "Asphodelos: The Second Circle", "Asphodelos: The Third Circle", "Asphodelos: The Fourth Circle",
        "Abyssos: The Fifth Circle", "Abyssos: The Sixth Circle", "Abyssos: The Seventh Circle", "Abyssos: The Eighth Circle",
        "Anabaseios: The Ninth Circle", "Anabaseios: The Tenth Circle", "Anabaseios: The Eleventh Circle", "Anabaseios: The Twelfth Circle",
        
        # Arcadion (DT)
        "AAC Light-heavyweight M1", "AAC Light-heavyweight M2", "AAC Light-heavyweight M3", "AAC Light-heavyweight M4",
        "AAC Cruiserweight M1", "AAC Cruiserweight M2", "AAC Cruiserweight M3", "AAC Cruiserweight M4"
    ]
    
    for raid in normal_raids:
        item_table.append({
            "name": raid,
            "category": ["Normal Raid", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Savage Raids - Extreme difficulty versions (subset to keep manageable)
    savage_raids = [
        # Second Coil Savage (ARR)
        "The Second Coil of Bahamut (Savage) - Turn 1", "The Second Coil of Bahamut (Savage) - Turn 2",
        "The Second Coil of Bahamut (Savage) - Turn 3", "The Second Coil of Bahamut (Savage) - Turn 4",
        
        # Alexander Savage (HW) - First tier only
        "Alexander - The Fist of the Father (Savage)", "Alexander - The Cuff of the Father (Savage)",
        "Alexander - The Arm of the Father (Savage)", "Alexander - The Burden of the Father (Savage)"
    ]
    
    for raid in savage_raids:
        item_table.append({
            "name": raid,
            "category": ["Savage Raid", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Guildhests - Tutorial group content - Early ones marked as early
    guildhests_early = [
        # Level < 35 guildhests
        "Basic Training: Enemy Parties", "Under the Armor", "Basic Training: Enemy Strongholds",
        "Hero on the Half Shell", "Pulling Poison Posies", "Stinging Back",
        "All's Well that Ends in the Well", "Flicking Sticks and Taking Names",
        "More than a Feeler", "Annoy the Void"
    ]
    
    guildhests_regular = [
        "Shadow and Claw", "Long Live the Queen", "Ward Up", "Solemn Trinity"
    ]
    
    # Early guildhests
    for guildhest in guildhests_early:
        item_table.append({
            "name": guildhest,
            "category": ["Guildhest", "ARR", "Duty", "Early Duty"],
            "count": 1,
            "early": True,
            "progression": True,
        })
    
    # Regular guildhests
    for guildhest in guildhests_regular:
        item_table.append({
            "name": guildhest,
            "category": ["Guildhest", "ARR", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Variant Dungeons (EW) - Special solo/small group content
    variant_dungeons = [
        "The Sil'dihn Subterrane", "Mount Rokkon", "Aloalo Island"
    ]
    
    for variant in variant_dungeons:
        item_table.append({
            "name": variant,
            "category": ["Variant Dungeon", "EW", "Duty"],
            "count": 1,
            "progression": True,
        })

    # Bozja Content (ShB) - Special alliance raid series
    bozja_content = [
        "Castrum Lacus Litore", "Delubrum Reginae", "The Dalriada"
    ]
    
    for bozja in bozja_content:
        item_table.append({
            "name": bozja,
            "category": ["Bozja", "ShB", "Duty"],
            "count": 1,
            "progression": True,
        })
    
    return item_table

def after_load_location_file(location_table: list) -> list:
    
    # Simple level milestone locations - now all require any job reaching that level
    location_table.append({
        "name": "Reach Level 15 on Any Job",
        "category": ["Level Milestone", "Early Location"],
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

    # Add more early milestone locations to accommodate early items
    early_milestones = [
        {"level": 5, "name": "First Steps: Reach Level 5"},
        {"level": 10, "name": "Getting Started: Reach Level 10"},  
        {"level": 20, "name": "Novice: Reach Level 20"},
        {"level": 25, "name": "Apprentice: Reach Level 25"},
        {"level": 30, "name": "Journeyman: Reach Level 30"},
    ]
    
    for milestone in early_milestones:
        location_table.append({
            "name": milestone["name"],
            "category": ["Level Milestone", "Early Location"],
            "region": "Manual",
            "requires": f"{{anyClassLevel({milestone['level']})}}"
        })

    # Add level locations every level for each job
    # ARR Starter Jobs
    for job in ARR_JOB:
        for level in range(1, 101):  # Every level from 1 to 100
            # Mark early job levels as early locations for key jobs
            is_early_location = (job in ["PLD", "WAR", "WHM"] and level <= 20)
            categories = [f"{job}", "DOW/DOM"]
            if is_early_location:
                categories.append("Early Location")
                
            if level <= 10:
                # Levels 1-10 are free with job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 10)|"
                })
            else:
                # Calculate items needed based on 5-level increments
                items_needed = (level - 10 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 10)|"
                })

    # ARR Non-Starter Jobs (like NIN)
    for job in ARR_NON_STARTER:
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
                # Level 30 requires Level 50 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 30)| and |Level 50 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 30
                items_needed = (level - 30 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 30)| and |Level 50 Access|"
                })

    for job in STB_JOB:
        for level in range(50, 101):  # Every level from 50 to 100
            if level <= 50:
                # Level 50 requires Level 50 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 50)| and |Level 50 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 50
                items_needed = (level - 50 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 50)| and |Level 50 Access|"
                })

    for job in SHB_JOB:
        for level in range(60, 101):  # Every level from 60 to 100
            if level <= 60:
                # Level 60 requires Level 60 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 60)| and |Level 60 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 60
                items_needed = (level - 60 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 60)| and |Level 60 Access|"
                })

    for job in EW_JOB:
        for level in range(70, 101):  # Every level from 70 to 100
            if level <= 70:
                # Level 70 requires Level 70 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 70)| and |Level 70 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 70
                items_needed = (level - 70 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 70)| and |Level 70 Access|"
                })

    for job in DT_JOB:
        for level in range(80, 101):  # Every level from 80 to 100
            if level <= 80:
                # Level 80 requires Level 80 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 80)| and |Level 80 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 80
                items_needed = (level - 80 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": [f"{job}", "DOW/DOM"],
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 80)| and |Level 80 Access|"
                })

    # BLU levels (max 80) - starts at level 1, requires Level 50 Access
    for level in range(1, 81):  # Every level from 1 to 80
        if level <= 5:
            # Levels 1-5 require Level 50 Access and job crystal
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Job Crystal (default cap 5)| and |Level 50 Access|"
            })
        else:
            # Calculate items needed based on 5-level increments from 5
            items_needed = (level - 5 + 4) // 5  # Round up division
            location_table.append({
                "name": f"BLU Level {level}",
                "category": ["BLU", "DOW/DOM"],
                "region": "BLU",
                "requires": f"|BLU Level Increased by 5:{items_needed}| and |BLU Job Crystal (default cap 5)| and |Level 50 Access|"
            })

    # DOH levels - starts at level 1, requires Level 15 Access
    for job in DOH:
        for level in range(1, 101):  # Every level from 1 to 100
            # Mark early levels for key DOH jobs as early locations
            is_early_location = (job in ["CRP", "BSM"] and level <= 15)  # CRP and BSM levels 1-15 are early
            categories = [f"{job}", "DOH"]
            if is_early_location:
                categories.append("Early Location")
                
            if level <= 5:
                # Levels 1-5 require Level 15 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 5)| and |Level 15 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 5
                items_needed = (level - 5 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 5)| and |Level 15 Access|"
                })

    # DOL levels - starts at level 1, requires Level 15 Access
    for job in DOL:
        for level in range(1, 101):  # Every level from 1 to 100
            # Mark early levels for key DOL jobs as early locations
            is_early_location = (job in ["MIN", "BTN"] and level <= 15)  # MIN and BTN levels 1-15 are early
            categories = [f"{job}", "DOL"]
            if is_early_location:
                categories.append("Early Location")
                
            if level <= 5:
                # Levels 1-5 require Level 15 Access and job crystal
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Job Crystal (default cap 5)| and |Level 15 Access|"
                })
            else:
                # Calculate items needed based on 5-level increments from 5
                items_needed = (level - 5 + 4) // 5  # Round up division
                location_table.append({
                    "name": f"{job} Level {level}",
                    "category": categories,
                    "region": f"{job}",
                    "requires": f"|{job} Level Increased by 5:{items_needed}| and |{job} Job Crystal (default cap 5)| and |Level 15 Access|"
                })

    # Simple duty completion locations - basic level requirements for key duties
    key_duties = [
        {"name": "Sastasha", "level": 18, "requires": "{anyClassLevel(18)}"},
        {"name": "The Praetorium", "level": 50, "requires": "|Level 50 Access| and {anyClassLevel(50)}"},
        {"name": "The Vault", "level": 58, "requires": "|Level 50 Access| and {anyClassLevel(58)}"},
        {"name": "Ala Mhigo", "level": 70, "requires": "|Level 70 Access| and {anyClassLevel(70)}"},
        {"name": "Amaurot", "level": 80, "requires": "|Level 80 Access| and {anyClassLevel(80)}"},
        {"name": "The Dead Ends", "level": 90, "requires": "|Level 80 Access| and {anyClassLevel(90)}"},
        {"name": "Alexandria", "level": 100, "requires": "|Level 80 Access| and {anyClassLevel(100)}"}
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
    all_other_jobs = ["DRK", "MCH", "AST", "SAM", "RDM", "GNB", "DNC", "RPR", "SGE", "VPR", "PCT", "CRP", "BSM", "ARM", "GSM", "LTW", "WVR", "ALC", "CUL", "MIN", "BTN", "FSH", "BLU", "NIN"]

    # ARR Starter Jobs - Starting regions that connect to ALL other job regions
    for job in ARR_JOB:
        region_table[job] = {
            "starting": True,
            "connects_to": all_other_jobs,
            "requires": f"|{job} Job Crystal (default cap 10)|"  # Require specific job crystal with cap
        }

    # ARR Non-Starter Jobs (like NIN) - Starting regions but different crystal requirements
    for job in ARR_NON_STARTER:
        region_table[job] = {
            "starting": True,  # Still starting, just not in starter category
            "connects_to": all_other_jobs,
            "requires": f"|{job} Job Crystal (default cap 10)|"  # Same crystal naming
        }

    # DOH Jobs - Level 15 requirement + specific job crystal
    for job in DOH:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 15 Access| and |{job} Job Crystal (default cap 5)|"
        }

    # DOL Jobs - Level 15 requirement + specific job crystal
    for job in DOL:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 15 Access| and |{job} Job Crystal (default cap 5)|"
        }

    # HW Jobs - Level 50 requirement + specific job crystal
    for job in HW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 50 Access| and |{job} Job Crystal (default cap 30)|"
        }

    # STB Jobs - Level 50 requirement + specific job crystal
    for job in STB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 50 Access| and |{job} Job Crystal (default cap 50)|"
        }

    # BLU - Level 50 requirement + specific job crystal
    region_table["BLU"] = {
        "starting": False,
        "connects_to": [],
        "requires": "|Level 50 Access| and |BLU Job Crystal (default cap 5)|"
    }

    # SHB Jobs - Level 60 requirement + specific job crystal
    for job in SHB_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 60 Access| and |{job} Job Crystal (default cap 60)|"
        }

    # EW Jobs - Level 70 requirement + specific job crystal
    for job in EW_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 70 Access| and |{job} Job Crystal (default cap 70)|"
        }

    # DT Jobs - Level 80 requirement + specific job crystal
    for job in DT_JOB:
        region_table[job] = {
            "starting": False,
            "connects_to": [],
            "requires": f"|Level 80 Access| and |{job} Job Crystal (default cap 80)|"
        }

    return region_table

def after_load_category_file(category_table: dict) -> dict:
    # Keep categories simple - include all job types
    all_jobs = ARR_JOB + ARR_NON_STARTER + HW_JOB + STB_JOB + SHB_JOB + EW_JOB + DT_JOB + DOH + DOL + ["BLU"]
    for job in all_jobs:
        category_table[job] = {}
    
    # Hide broad job type categories and internal categories
    category_table["DOW/DOM"] = {"hidden": True}
    category_table["DOL"] = {"hidden": True}
    category_table["DOH"] = {"hidden": True}
    category_table["Level Progression"] = {"hidden": True}
    category_table["Early Duty"] = {"hidden": True}
    category_table["Early Location"] = {"hidden": True}
    
    return category_table

def after_load_progressive_item_file(progressive_item_table: list) -> list:
    return progressive_item_table

def after_load_option_file(option_table: dict) -> dict:
    return option_table

def after_load_meta_file(meta_table: dict) -> dict:
    return meta_table

def hook_interpret_slot_data(world, player: int, slot_data: dict[str, any]) -> dict | bool:
    return False