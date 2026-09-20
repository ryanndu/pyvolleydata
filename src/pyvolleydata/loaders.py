import io
from datetime import UTC, datetime

import pandas as pd
import requests

LEAGUES = {
    "mlv": 2024,
    "lovb": 2025,
    "aupvb": 2022,
}


def _load(league: str, dataset: str, seasons: int | list[int] | None) -> pd.DataFrame:
    """Loads one league's published dataset, filtered to the given seasons.

    Args:
        league: The league to load.
        dataset: A dataset name, which is also its release tag.
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        The dataset as published, filtered to the requested seasons.

    Raises:
        TypeError: If seasons isn't an int, a list of ints, or None.
        ValueError: If the league is unknown, or a season is outside
            the range of available data.
        ConnectionError: If the data couldn't be downloaded.
    """
    league = _validate_league(league)
    seasons = _validate_seasons(league, seasons)

    asset = f"{league}_{dataset.replace('-', '_')}.parquet"
    url = f"https://github.com/awosoga/volleydata/releases/download/{dataset}/{asset}"

    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
    except requests.RequestException as error:
        raise ConnectionError(f"Could not download {league} {dataset} data from {url}") from error

    frame = pd.read_parquet(io.BytesIO(response.content))
    return frame[frame["season"].isin(seasons)].reset_index(drop=True)


def _validate_league(league: str) -> str:
    """Checks that a league is one the data covers.

    Args:
        league: The league to load, case insensitive.

    Raises:
        TypeError: If league isn't a string.
        ValueError: If the league isn't one of the published leagues.

    Returns:
        The league, lowercased.
    """
    if not isinstance(league, str):
        raise TypeError(f"Expected league to be a str, got {type(league).__name__}")

    if league.lower() not in LEAGUES:
        raise ValueError(f"Unknown league {league!r}, expected one of {sorted(LEAGUES)}")

    return league.lower()


def _validate_seasons(league: str, seasons: int | list[int] | None) -> list[int]:
    """Checks that seasons is a usable season collection for one league.

    Args:
        league: The league being loaded, already validated.
        seasons (int | list[int] | None): A season, a list of seasons, or None for all of them.

    Raises:
        TypeError: If seasons isn't an int, a list of ints, or None.
        TypeError: If a season in seasons isn't an int.
        ValueError: If the season is out of range.

    Returns:
        The requested seasons as a list. If None was given, every season
            from the league's first through the current year.

    """
    first_season = LEAGUES[league]
    latest = datetime.now(UTC).year

    if seasons is None:
        return list(range(first_season, latest + 1))
    if isinstance(seasons, bool):
        raise TypeError("Expected an integer season, got bool")
    if isinstance(seasons, int):
        seasons = [seasons]
    if not isinstance(seasons, list):
        raise TypeError(
            f"Expected seasons to be an int, list of ints, or None, got {type(seasons).__name__}"
        )

    for season in seasons:
        if isinstance(season, bool) or not isinstance(season, int):
            raise TypeError(f"Expected an integer season, got {type(season).__name__}")
        if not first_season <= season <= latest:
            raise ValueError(f"Season {season} out of range ({first_season}-{latest})")

    return seasons


def load_schedule(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's schedule.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per match.

    Examples:
        >>> load_schedule("mlv", 2025)
        >>> load_schedule("lovb", [2025, 2026])
        >>> load_schedule("aupvb")
    """
    return _load(league, "schedule", seasons)


def load_sets(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's sets.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per team per set.

    Examples:
        >>> load_sets("mlv", 2025)
        >>> load_sets("lovb", [2025, 2026])
        >>> load_sets("aupvb")
    """
    return _load(league, "sets", seasons)


def load_officials(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's match officials.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per official per match. A match with no officials recorded
            produces no rows.

    Examples:
        >>> load_officials("mlv", 2025)
        >>> load_officials("lovb", [2025, 2026])
        >>> load_officials("aupvb")
    """
    return _load(league, "officials", seasons)


def load_player_info(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's match rosters.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per player per match, for the active roster and the reserves.

    Examples:
        >>> load_player_info("mlv", 2025)
        >>> load_player_info("lovb", [2025, 2026])
        >>> load_player_info("aupvb")
    """
    return _load(league, "player-info", seasons)


def load_team_staff(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's team staff.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per staff member per team per match. A match with no staff
            recorded produces no rows.

    Examples:
        >>> load_team_staff("mlv", 2025)
        >>> load_team_staff("lovb", [2025, 2026])
        >>> load_team_staff("aupvb")
    """
    return _load(league, "team-staff", seasons)


def load_pbp(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's play-by-play.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per touch.

    Examples:
        >>> load_pbp("mlv", 2025)
        >>> load_pbp("lovb", [2025, 2026])
        >>> load_pbp("aupvb")
    """
    return _load(league, "pbp", seasons)


def load_events_log(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's match events.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per event.

    Examples:
        >>> load_events_log("mlv", 2025)
        >>> load_events_log("lovb", [2025, 2026])
        >>> load_events_log("aupvb")
    """
    return _load(league, "events-log", seasons)


def load_player_boxscore(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's player box scores.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per player per set.

    Examples:
        >>> load_player_boxscore("mlv", 2025)
        >>> load_player_boxscore("lovb", [2025, 2026])
        >>> load_player_boxscore("aupvb")
    """
    return _load(league, "player-boxscore", seasons)


def load_team_boxscore(league: str, seasons: int | list[int] | None = None) -> pd.DataFrame:
    """Loads a league's team box scores.

    Args:
        league: One of "mlv", "lovb", or "aupvb".
        seasons: A season, a list of seasons, or None for all of them.

    Returns:
        One row per team per set.

    Examples:
        >>> load_team_boxscore("mlv", 2025)
        >>> load_team_boxscore("lovb", [2025, 2026])
        >>> load_team_boxscore("aupvb")
    """
    return _load(league, "team-boxscore", seasons)
