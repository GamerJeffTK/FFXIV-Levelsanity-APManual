# Object classes from AP that represent different types of options that you can create
from BaseClasses import PlandoOptions
from Options import Toggle, DefaultOnToggle, Choice, Range, OptionSet, PerGameCommonOptions, Option, OptionGroup, Visibility
from worlds.AutoWorld import World
from Utils import get_fuzzy_results
from typing import Type

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

class FadedJobCrystalsRequired(Range):
    """
    Number of Faded Job Crystals required for victory condition.
    """
    display_name = "Faded Job Crystals Required"
    range_start = 1
    range_end = 50
    default = 25

class TotalLevelsRequired(Range):
    """
    Total levels across all jobs required for victory condition (0 = disabled).
    """
    display_name = "Total Levels Required"
    range_start = 0
    range_end = 2400  # 24 jobs * 100 levels max
    default = 200

class StartingARRJobCrystals(Range):
    """
    Number of ARR Starter Job Crystals to start with.
    """
    display_name = "Starting ARR Job Crystals"
    range_start = 0
    range_end = 9  # Total number of ARR jobs
    default = 3

class StartingDOHJobCrystals(Range):
    """
    Number of Disciple of Hand Job Crystals to start with.
    """
    display_name = "Starting DOH Job Crystals"
    range_start = 0
    range_end = 8  # Total number of DOH jobs
    default = 1

class StartingDOLJobCrystals(Range):
    """
    Number of Disciple of Land Job Crystals to start with.
    """
    display_name = "Starting DOL Job Crystals"
    range_start = 0
    range_end = 3  # Total number of DOL jobs
    default = 1

class StartingLevelIncreaseItems(Range):
    """
    Number of 'Level Increased by 5' items to start with (distributed randomly across jobs).
    """
    display_name = "Starting Level Increase Items"
    range_start = 0
    range_end = 200  # Reasonable cap for starting level items
    default = 10

class StartingDuties(Range):
    """
    Number of random duties (dungeons, trials, raids) to start with.
    """
    display_name = "Starting Duties"
    range_start = 0
    range_end = 100  # Reasonable cap for starting duties
    default = 5

class IncludeExtremeDifficulty(Toggle):
    """
    Include Extreme difficulty trials and savage raids in the item pool.
    """
    display_name = "Include Extreme/Savage Content"
    default = False

class IncludeDungeons(DefaultOnToggle):
    """
    Include dungeons in the item pool.
    """
    display_name = "Include Dungeons"

class IncludeTrials(DefaultOnToggle):
    """
    Include trials in the item pool.
    """
    display_name = "Include Trials"

class IncludeRaids(DefaultOnToggle):
    """
    Include raids (Normal, Alliance, Savage) in the item pool.
    """
    display_name = "Include Raids"
    default = False

class IncludeGuildhests(Toggle):
    """
    Include guildhests in the item pool.
    """
    display_name = "Include Guildhests"
    default = False

class IncludeVariantDungeons(DefaultOnToggle):
    """
    Include variant dungeons in the item pool.
    """
    display_name = "Include Variant Dungeons"
    default = False

class IncludeBozjaContent(DefaultOnToggle):
    """
    Include Bozja content in the item pool.
    """
    display_name = "Include Bozja Content"
    default = False

class IncludedExpansions(Choice):
    """
    Which expansions to include content from.
    """
    display_name = "Included Expansions"
    option_arr_only = 0
    option_arr_hw = 1
    option_arr_hw_stb = 2
    option_arr_hw_stb_shb = 3
    option_arr_hw_stb_shb_ew = 4
    option_all_expansions = 5
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    # Victory Conditions
    options["faded_job_crystals_required"] = FadedJobCrystalsRequired
    options["total_levels_required"] = TotalLevelsRequired
    
    # Starting Items
    options["starting_arr_job_crystals"] = StartingARRJobCrystals
    options["starting_doh_job_crystals"] = StartingDOHJobCrystals
    options["starting_dol_job_crystals"] = StartingDOLJobCrystals
    options["starting_level_increase_items"] = StartingLevelIncreaseItems
    options["starting_duties"] = StartingDuties
    
    # Progression Settings
    options["include_extreme_difficulty"] = IncludeExtremeDifficulty
    
    # Content Toggles
    options["include_dungeons"] = IncludeDungeons
    options["include_trials"] = IncludeTrials
    options["include_raids"] = IncludeRaids
    options["include_guildhests"] = IncludeGuildhests
    options["include_variant_dungeons"] = IncludeVariantDungeons
    options["include_bozja_content"] = IncludeBozjaContent
    
    # Expansion Selection
    options["included_expansions"] = IncludedExpansions
    
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]) -> None:
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"
    
    # Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options
    
    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Option]]) -> dict[str, list[Option]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups