from Options import Option, Range, Toggle, Choice


class FadedJobCrystalsRequired(Range):
    """Number of Faded Job Crystals required for victory condition."""
    display_name = "Faded Job Crystals Required"
    range_start = 1
    range_end = 50
    default = 25


class TotalLevelsRequired(Range):
    """Total levels across all jobs required for victory condition (0 = disabled)."""
    display_name = "Total Levels Required"
    range_start = 0
    range_end = 2400
    default = 1700


class StartingArrJobCrystals(Range):
    """Number of ARR Starter Job Crystals to start with."""
    display_name = "Starting ARR Job Crystals"
    range_start = 0
    range_end = 9
    default = 1


class StartingDohJobCrystals(Range):
    """Number of Disciple of Hand Job Crystals to start with."""
    display_name = "Starting DoH Job Crystals"
    range_start = 0
    range_end = 8
    default = 0


class StartingDolJobCrystals(Range):
    """Number of Disciple of Land Job Crystals to start with."""
    display_name = "Starting DoL Job Crystals"
    range_start = 0
    range_end = 3
    default = 0


class StartingLevelIncreaseItems(Range):
    """Number of 'Level Increased by 5' items to start with (distributed randomly across jobs)."""
    display_name = "Starting Level Increase Items"
    range_start = 0
    range_end = 200
    default = 1


class StartingDuties(Range):
    """Number of random duties (dungeons, trials, raids) to start with."""
    display_name = "Starting Duties"
    range_start = 0
    range_end = 100
    default = 2


class IncludeExtremeDifficulty(Toggle):
    """Include Extreme difficulty trials and savage raids in the item pool."""
    display_name = "Include Extreme Difficulty"
    default = False


class IncludeDungeons(Toggle):
    """Include dungeons in the item pool."""
    display_name = "Include Dungeons"
    default = True


class IncludeTrials(Toggle):
    """Include trials in the item pool."""
    display_name = "Include Trials"
    default = True


class IncludeRaids(Toggle):
    """Include raids (Normal, Alliance, Savage) in the item pool."""
    display_name = "Include Raids"
    default = False


class IncludeGuildhests(Toggle):
    """Include guildhests in the item pool."""
    display_name = "Include Guildhests"
    default = False


class IncludeVariantDungeons(Toggle):
    """Include variant dungeons in the item pool."""
    display_name = "Include Variant Dungeons"
    default = False


class IncludeBozjaContent(Toggle):
    """Include Bozja content in the item pool."""
    display_name = "Include Bozja Content"
    default = False


class IncludedExpansions(Choice):
    """Which expansions to include content from."""
    display_name = "Included Expansions"
    option_arr_only = 0
    option_arr_hw = 1
    option_arr_hw_stb = 2
    option_arr_hw_stb_shb = 3
    option_arr_hw_stb_shb_ew = 4
    option_all_expansions = 5
    default = 0


class Goal(Choice):
    """How to End your Randomized playthrough."""
    display_name = "Goal"
    option_the_crystal_of_completion = 0
    option_a_certain_amount_of_levels = 1
    default = 1


class DLCEnabled(Toggle):
    """Is the DLC enabled?"""
    display_name = "DLC Enabled"
    default = True


# Example options for Manual framework
class ExampleToggle(Toggle):
    """This is a Toggle. A simple boolean, aka True or False set the initial value with "default" """
    display_name = "Example Toggle"
    default = False


class ExampleChoice(Choice):
    """This is a Choice. Let the user pick from a list of values. allow_custom_value let a player define their own text value. Currently the only use for Choice in Manual outside of hooks is the goal"""
    display_name = "Example Choice"
    option_start = 0
    option_test = 1
    default = 0


class ExampleRange(Range):
    """This is a Range. Allow the player to specify a value between 'start' and 'end'. if you include a "values" you can define the label for certain values. Currently the only use for Range in Manual outside of hooks is 'filler_trap' """
    display_name = "Example Range"
    range_start = 0
    range_end = 10
    default = 1


# Dictionary mapping for easier access in game logic
manual_ffxivlevelsanity_pumpkinjacktr_options = {
    "faded_job_crystals_required": FadedJobCrystalsRequired,
    "total_levels_required": TotalLevelsRequired,
    "starting_arr_job_crystals": StartingArrJobCrystals,
    "starting_doh_job_crystals": StartingDohJobCrystals,
    "starting_dol_job_crystals": StartingDolJobCrystals,
    "starting_level_increase_items": StartingLevelIncreaseItems,
    "starting_duties": StartingDuties,
    "include_extreme_difficulty": IncludeExtremeDifficulty,
    "include_dungeons": IncludeDungeons,
    "include_trials": IncludeTrials,
    "include_raids": IncludeRaids,
    "include_guildhests": IncludeGuildhests,
    "include_variant_dungeons": IncludeVariantDungeons,
    "include_bozja_content": IncludeBozjaContent,
    "included_expansions": IncludedExpansions,
    "goal": Goal,
    "DLC_enabled": DLCEnabled,
    "Example_Toggle": ExampleToggle,
    "Example_Choice": ExampleChoice,
    "Example_Range": ExampleRange,
}