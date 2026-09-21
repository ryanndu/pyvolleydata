# pyvolleydata <img src="https://github.com/ryanndu/pyvolleydata/raw/main/assets/images/pyvolleydata-logo.svg" align="right" width="100" height="100"/>

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/pyvolleydata?period=total&units=NONE&left_color=BLACK&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/pyvolleydata)

The goal of this package is to help people access clean and tidy data from
professional volleyball. It provides a set of loaders that return schedules,
box scores, play-by-play, rosters and match events as pandas DataFrames, ready
to analyze.

Three leagues are covered:

| League | Code | Seasons |
| --- | --- | --- |
| Major League Volleyball | `mlv` | 2024 onwards |
| League One Volleyball | `lovb` | 2025 onwards |
| Athletes Unlimited Pro Volleyball | `aupvb` | 2021 to 2025 |

## Installation

```bash
pip install pyvolleydata
```

## Usage

Every loader takes a league, plus a season, a list of seasons, or nothing at
all for every season available.

```python exec="true" source="above"
import pyvolleydata

schedule = pyvolleydata.load_schedule("mlv", 2026)

print(
    schedule[
        [
            "start_time_utc",
            "home_team_name",
            "home_team_set_wins",
            "away_team_name",
            "away_team_set_wins",
        ]
    ]
    .head()
    .to_markdown(index=False)
)
```

Every loader takes a league, and a season, list of seasons, or nothing for 
every season available.

```python
pyvolleydata.load_player_boxscore("lovb", 2026)
pyvolleydata.load_pbp("mlv", [2025, 2026])
pyvolleydata.load_team_boxscore("aupvb")
```

Data is sourced from [volleydata](https://github.com/awosoga/volleydata),
which updates daily during the season.

For those who prefer to program in R,
[rvolleydata](https://awosoga.github.io/rvolleydata/) has complete function
parity with this package.