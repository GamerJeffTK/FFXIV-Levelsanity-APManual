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
    Number of Faded Job Crystals required for the "Collect All Faded Job Crystals" victory condition.
    Only applies if that victory condition is selected.
    """
    display_name = "Faded Job Crystals Required"
    range_start = 1
    range_end = 100
    default = 50

class TotalLevelsRequired(Range):
    """
    Total levels across all jobs required for the "Reach Total Level Goal" victory condition.
    Only applies if that victory condition is selected. This counts the sum of all your job levels.
    """
    display_name = "Total Levels Required"
    range_start = 50
    range_end = 2400  # 24 jobs * 100 levels max
    default = 500

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
    # Victory Condition Configuration
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
    # Update the goal option to have better descriptions and aliases
    if hasattr(options.type_hints, 'goal'):
        goal_option = options.type_hints['goal']
        
        # Update descriptions to be clearer about what each victory condition does
        goal_option.display_name = "Victory Condition"
        goal_option.__doc__ = """Choose your victory condition:
        - Max Level: Get any single job to maximum level (scales with expansions)
        - Total Levels: Reach a total sum of levels across all unlocked jobs
        - Faded Crystals: Collect the specified number of Faded Job Crystal McGuffins"""
        
        # Add some aliases for easier configuration
        goal_option.aliases.update({
            "max_level": 0,
            "level_sum": 1, 
            "crystals": 2,
            "any_max": 0,
            "total": 1,
            "mcguffin": 2
        })
        # Update the options dict so aliases work
        goal_option.options.update(goal_option.aliases)

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Option]]) -> dict[str, list[Option]]:
    # Group victory condition options together
    groups['Victory Conditions'] = [
        FadedJobCrystalsRequired,
        TotalLevelsRequired
    ]
    
    groups['Starting Items'] = [
        StartingARRJobCrystals,
        StartingDOHJobCrystals, 
        StartingDOLJobCrystals,
        StartingLevelIncreaseItems,
        StartingDuties
    ]
    
    groups['Content Selection'] = [
        IncludedExpansions,
        IncludeDungeons,
        IncludeTrials,
        IncludeRaids,
        IncludeExtremeDifficulty,
        IncludeGuildhests,
        IncludeVariantDungeons,
        IncludeBozjaContent
    ]
    
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups