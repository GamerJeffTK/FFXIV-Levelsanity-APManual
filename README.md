# FFXIV Levelsanity

A Manual Archipelago randomizer for Final Fantasy XIV Online that focuses on job progression and duty completion.

## What is FFXIV Levelsanity?

This randomizer transforms FFXIV's job system into an Archipelago-compatible progression game. Instead of naturally leveling jobs through gameplay, you must find **Job Crystals** and **Level Progression Items** scattered throughout the multiworld to unlock and advance your jobs.

## How It Works

### Job System
- **Job Crystals** unlock specific jobs and provide initial levels:
  - ARR jobs start at level 10 with their crystal
  - Expansion jobs start at higher levels (30-80 depending on expansion)
  - DOH/DOL jobs start at level 5

- **Level Increased by 5** items advance your jobs in 5-level increments
- Each job has locations for every individual level (1-100 for most jobs)

### Duties as Items
- Dungeons, trials, raids, and other duties become progression items
- Early duties (level ≤20) are marked as early items for smoother progression
- Duties unlock access to new content and areas

### Victory Conditions
Choose between:
- **Crystal Completion**: Collect a certain number of "A Faded Job Crystal" items
- **Level Goals**: Reach specific level thresholds across job categories (DOW/DOM, DOH, DOL)

## Progression Flow

1. **Start** with random ARR job crystals, DOH crystals, DOL crystal, and some level/duty items (configured by player in yaml)
2. **Level Access Gates** at 15, 50, 60, 70, and 80 unlock higher-level content and expansion jobs
3. **Job Regions** require their specific crystal plus appropriate level access
4. **Manual Tracking** - you track your actual in-game progress to match your Archipelago items

## Installation & Setup

1. Place the apworld in your Archipelago `custom_worlds` directory, or just double-click after downloading
2. Generate a seed with your FFXIV Levelsanity yaml configured and placed in `Players`
3. Use the Manual Client to track your progression
4. Play FFXIV normally but restrict yourself to only use jobs/levels/duties you've "unlocked" via items received

## Key Features

- **2400+ Locations**: Every job level from 1-100 across all jobs
- **500+ Items**: Job crystals, level progression, duties from all expansions
- **Flexible Victory**: Choose your completion goal
- **Early Game Balance**: Starting items and early duties ensure smooth progression
- **Full Expansion Support**: Content from A Realm Reborn through Dawntrail

## Options

- **Starting Items**: Customize how many crystals and progression items you start with
- **Content Toggles**: Enable/disable specific types of duties
- **Expansion Selection**: Choose which expansions to include
- **Victory Conditions**: Set your completion requirements

---

*This is a Manual game for Archipelago - you manually track your progress and restrict your gameplay based on items received. No game modification is required.*
