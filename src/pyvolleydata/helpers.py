import pandas as pd
from datetime import datetime


def get_data(league, seasons, data_type):
    """
    Loads data for a specified league and season(s) from the volleydata repository.

    Parameters
    ----------
    league : str
        A string specifying which of 'mlv', 'pvf', or 'au' to load data for.

    data_type : str
        The type of data to fetch (e.g., 'pbp', 'events_log')
        
    seasons : int, list of int, or None, optional
        Season(s) to load. By default, None loads all available seasons.
        - int : Single season year (e.g., 2025)
        - list of int : Multiple seasons (e.g., [2024, 2025])
        - None : Load all available seasons

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the merged or filtered data with an additional 'league' column.

    Examples
    --------
    >>> fetch_data(league='mlv', data_type='pbp', seasons=2024)
    >>> fetch_data(league='au', data_type='rosters', seasons=[2022, 2023])
    >>> fetch_data(league='lovb', data_type='events_log')
    """
    league_config = {
        'mlv': {'start_year': 2024, 'internal_name': 'pvf'},
        'lovb': {'start_year': 2025, 'internal_name': 'lovb'},
        'au': {'start_year': 2022, 'internal_name': 'aupvb'}
    }
    if league in league_config:
        league_start_year = league_config.get(league).get('start_year')
        league_internal_name = league_config.get(league).get('internal_name')
    
        if isinstance(seasons, int):
            seasons = [seasons]
        if isinstance(seasons, list):
            validate_seasons(seasons, league_start_year)
        elif seasons is None:
            seasons = list(range(league_start_year, datetime.now().year + 1))
        else:
            raise TypeError(f'Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}')
        base_url = "https://github.com/awosoga/volleydata/releases/download"
        df = pd.DataFrame()
        if data_type in {'pbp', 'events_log'}:
            for season in seasons:
                file_path = f"{league_internal_name}-{data_type.replace("_", "-")}/{league_internal_name}_{data_type}_{season}.csv"
                df = pd.concat([df, pd.read_csv(f"{base_url}/{file_path}")])
        else:
            file_path = f"{league_internal_name}-{data_type.replace("_", "-")}/{league_internal_name}_{data_type}.csv"
            df = pd.read_csv(f"{base_url}/{file_path}")
            df = df[df['season'].isin(seasons)]
    else:
        raise TypeError("league must be one of 'mlv', 'lovb', or 'au'")
    df['league'] = league
    return df


def validate_seasons(seasons, league_start_year):
    """
    Checks whether all the provided seasons are valid years and raises an error if not.

    Parameters
    ----------
    seasons: list of int
        A list of years representing seasons to validate.

    league_start_year: int
        The starting year to determine if the seasons are within range.

    Returns
    -------
    None

    Examples
    --------
    >>> validate_seasons([2024, 2025], 2024)
    >>> validate_seasons(['2020'], 2024)  # Raises TypeError
    >>> validate_seasons([2022, 2023, 2030], 2024)  # Raises ValueError
    """
    if not isinstance(seasons, list):
        raise TypeError('Expected a list of years')
    for year in seasons:
        if not isinstance(year, int):
            raise TypeError(f'Expected an integer for year, got {type(year).__name__}')
        if year < league_start_year or year > datetime.now().year:
            raise ValueError(f'Year {year} out of valid range for this league ({league_start_year}-{datetime.now().year})')