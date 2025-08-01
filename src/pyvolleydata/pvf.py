import pandas as pd
from . import helpers as h
from datetime import datetime


def load_pvf_officials(seasons = None):
    """
    Load cleaned pvf officials data from the volleydata repository.

    Parameters
    ----------
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

        All years must be 2024 or later.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the schedule with the following columns:

        ================================  ===========
        Column Name                        Type
        ================================  ===========
        match_id                           int
        season                             int
        match_datetime                     string
        officials_type                     string
        full_name                          string
        first_name                         string
        last_name                          string
        level                              string
        ================================  ===========
    
    Examples
    --------
    >>> load_pvf_officials(2025)
    >>> load_pvf_officials([2024, 2025])
    >>> load_pvf_officials()
    """

    if isinstance(seasons, int):
        seasons = [seasons]
    if isinstance(seasons, list):
        h.validate_seasons(seasons, league_start_year=2024)
    elif seasons is None:
        seasons = list(range(2024, datetime.now().year + 1))
    else:
        raise TypeError(f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}")
    
    officials = pd.read_csv("https://github.com/awosoga/volleydata/releases/download/pvf-officials/pvf_officials.csv")
    officials = officials[officials['season'].isin(seasons)]
    return officials


def load_pvf_points_log(seasons = None):
    """
    Load cleaned pvf point log data from the volleydata repository.

    Parameters
    ----------
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

        All years must be 2024 or later.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the schedule with the following columns:

        ================================  ===========
        Column Name                        Type
        ================================  ===========
        match_id                           int
        season                             int
        match_datetime                     string
        home_team_name                     string
        away_team_name                     string
        team_involved                      string
        jersey_number                      int         
        action                             string
        outcome                            string
        set                                int
        point_number                       int
        point_winner                       string
        home_score                         int
        away_score                         int                           
        ================================  ===========
    
    Examples
    --------
    >>> load_pvf_points_log(2025)
    >>> load_pvf_points_log([2024, 2025])
    >>> load_pvf_points_log()
    """

    if isinstance(seasons, int):
        seasons = [seasons]
    if isinstance(seasons, list):
        h.validate_seasons(seasons, league_start_year=2024)
    elif seasons is None:
        seasons = list(range(2024, datetime.now().year + 1))
    else:
        raise TypeError(f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}")
    
    points_log = pd.read_csv("https://github.com/awosoga/volleydata/releases/download/pvf-points-log/pvf_points_log.csv")
    points_log = points_log[points_log['season'].isin(seasons)]
    return points_log


def load_pvf_pbp(seasons = None):
    """
    Load cleaned pvf play-by-play data from the volleydata repository.

    Parameters
    ----------
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

        All years must be 2024 or later.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the schedule with the following columns:

        ================================  ===========
        Column Name                        Type
        ================================  ===========
        match_id                           int
        season                             int
        match_datetime                     string
        set                                int
        set_start_time                     string
        set_end_time                       string
        set_duration                       int
        set_home_score                     int
        set_away_score                     int
        event_type                         string
        event_time                         string
        libero_enters                      bool
        team_involved                      string
        libero_jersey_number               int
        libero_subsitute_jersey_number     int
        rally_start_time                   string
        rally_end_time                     string
        point_team                         string
        call_approved                      bool
        player_in_jersey_number            int
        player_out_jersey_number           int
        challenge_reason                   string
        challenge_method                   string
        challenge_response                 string
        challenge_result                   string
        home_score_after_challenge         int
        away_score_after_challenge         int
        ================================  ===========
    
    Examples
    --------
    >>> load_pvf_pbp(2025)
    >>> load_pvf_pbp([2024, 2025])
    >>> load_pvf_pbp()
    """

    if isinstance(seasons, int):
        seasons = [seasons]
    if isinstance(seasons, list):
        h.validate_seasons(seasons, league_start_year=2024)
    elif seasons is None:
        seasons = list(range(2024, datetime.now().year + 1))
    else:
        raise TypeError(f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}")
    
    pbp = pd.read_csv("https://github.com/awosoga/volleydata/releases/download/pvf-pbp/pvf_pbp.csv")
    pbp = pbp[pbp['season'].isin(seasons)]
    return pbp


def load_pvf_player_boxscore(seasons = None):
    """
    Load cleaned pvf player boxscore data from the volleydata repository.

    Parameters
    ----------
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

        All years must be 2024 or later.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the schedule with the following columns:

        ================================  ===========
        Column Name                        Type
        ================================  ===========
        match_id                           int
        season                             int
        match_datetime                     string
        player_id                          int
        player_name                        string
        first_name                         string
        last_name                          string
        jersey_number                      int
        primary_position                   int
        roster_status                      string
        is_foreign                         bool
        is_confederation                   bool
        is_captain                         bool
        is_libero                          bool
        set_1_is_starter                   bool
        set_1_starting_position            int
        set_2_is_starter                   bool
        set_2_starting_position            int
        set_3_is_starter                   bool
        set_3_starting_position            int
        set_4_is_starter                   bool
        set_4_starting_position            int
        set_5_is_starter                   bool
        set_5_starting_position            int
        team_name                          string
        team_short_name                    string
        team_code                          string
        team_color                         string              
        ================================  ===========
    
    Examples
    --------
    >>> load_pvf_pbp(2025)
    >>> load_pvf_pbp([2024, 2025])
    >>> load_pvf_pbp()
    """

    if isinstance(seasons, int):
        seasons = [seasons]
    if isinstance(seasons, list):
        h.validate_seasons(seasons, league_start_year=2024)
    elif seasons is None:
        seasons = list(range(2024, datetime.now().year + 1))
    else:
        raise TypeError(f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}")
    
    player_boxscore = pd.read_csv("https://github.com/awosoga/volleydata/releases/download/pvf-player-boxscore/pvf_player_boxscore.csv")
    player_boxscore = player_boxscore[player_boxscore['season'].isin(seasons)]
    return player_boxscore


def load_pvf_team_staff(seasons = None):
    """
    Load cleaned pvf team staff data from the volleydata repository.

    Parameters
    ----------
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

        All years must be 2024 or later.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the schedule with the following columns:

        ================================  ===========
        Column Name                        Type
        ================================  ===========
        match_id                           int
        season                             int
        match_datetime                     string
        team_name                          string
        staff_type                         string
        full_name                          string
        first_name                         string
        last_name                          string        
        ================================  ===========
    
    Examples
    --------
    >>> load_pvf_team_staff(2025)
    >>> load_pvf_team_staff([2024, 2025])
    >>> load_pvf_team_staff()
    """

    if isinstance(seasons, int):
        seasons = [seasons]
    if isinstance(seasons, list):
        h.validate_seasons(seasons, league_start_year=2024)
    elif seasons is None:
        seasons = list(range(2024, datetime.now().year + 1))
    else:
        raise TypeError(f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}")
    
    team_staff = pd.read_csv("https://github.com/awosoga/volleydata/releases/download/pvf-team-staff/pvf_team_staff.csv")
    team_staff = team_staff[team_staff['season'].isin(seasons)]
    return team_staff