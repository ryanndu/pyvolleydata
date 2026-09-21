# Analyzing a match

Let's look at one match: the 2026 MLV final, where the Dallas Pulse beat the
Omaha Supernovas 3–2 to win the championship.

## Find the match

Every dataset is keyed on `match_id`, so the schedule is where you start.

```python exec="true" source="above"
import pyvolleydata

schedule = pyvolleydata.load_schedule("mlv", 2026)
final = schedule[schedule["match_id"] == "2464512"]

print(
    final[
        [
            "start_time_utc",
            "venue_name",
            "home_team_name",
            "home_team_set_wins",
            "away_team_name",
            "away_team_set_wins",
            "game_type",
        ]
    ].to_markdown(index=False)
)
```

## Set by set

`load_sets` has one row per team per set, so pivoting on `set_number` gives
the scoreline.

```python exec="true" source="above"
import pyvolleydata

sets = pyvolleydata.load_sets("mlv", 2026)
final = sets[sets["match_id"] == "2464512"]

print(
    final.pivot_table(index="set_number", columns="team_name", values="points_scored").to_markdown()
)
```

## Team totals

The team box score is also per set, so a match total means summing over
`set_number`. Every stat here equals the sum of that team's players for the
same set, which makes it a useful cross-check.

```python exec="true" source="above"
import pyvolleydata

boxscore = pyvolleydata.load_team_boxscore("mlv", 2026)
final = boxscore[boxscore["match_id"] == "2464512"]

print(
    final.groupby("team_name")[
        ["attack_kills", "attack_attempts", "serve_aces", "block_points", "digs"]
    ]
    .sum()
    .to_markdown()
)
```

## Individual lines

The player box score is one row per player per set, including sets a player
didn't appear in, so summing gives match totals.

```python exec="true" source="above"
import pyvolleydata

players = pyvolleydata.load_player_boxscore("mlv", 2026)
final = players[players["match_id"] == "2464512"]

totals = (
    final.groupby(["first_name", "last_name", "team_name"], as_index=False)[
        ["attack_kills", "attack_errors", "block_points", "digs"]
    ]
    .sum()
    .sort_values("attack_kills", ascending=False)
)

print(totals.head(6).to_markdown(index=False))
```

## Every touch

Play-by-play is one row per touch, in order. `skill` names what the player
did and `effect_code` says how it came off.

```python exec="true" source="above"
import pyvolleydata

pbp = pyvolleydata.load_pbp("mlv", 2026)
final = pbp[pbp["match_id"] == "2464512"]

print(
    final[["set_number", "rally_number", "play_number", "team_side", "skill", "effect_code"]]
    .head(8)
    .to_markdown(index=False)
)
```

The effect codes run from `#` for a terminal winner through `+`, `!`, `-` and
`/` down to `=` for an error.

```python exec="true" source="above"
import pyvolleydata

pbp = pyvolleydata.load_pbp("mlv", 2026)
final = pbp[pbp["match_id"] == "2464512"]

attacks = final[final["skill"] == "attack"]

print(attacks.groupby("team_side")["effect_code"].value_counts().unstack(fill_value=0).to_markdown())
```

## How the fifth set went

Because `home_score` and `away_score` are carried on every touch, the swing
of a set plots straight from the play-by-play.

```python exec="true" source="above"
import pyvolleydata

pbp = pyvolleydata.load_pbp("mlv", 2026)
fifth = pbp[(pbp["match_id"] == "2464512") & (pbp["set_number"] == 5)]

rallies = fifth.groupby("rally_number")[["home_score", "away_score"]].max()
rallies["home_lead"] = rallies["home_score"] - rallies["away_score"]

print(rallies.tail(8).to_markdown())
```

## Comparing player contributions
 
Sofia Maldonado Diaz and Brooke Nuneviller both played all five sets and led their 
respective teams' attacks, but their statistical profiles differ significantly. 
Scaling each skill to the highest figure recorded in the match puts all five axes 
on the same footing, allowing for a direct visual comparison of their distinct roles.
 
```python exec="true" html="true" source="above"
from io import StringIO
 
import matplotlib
 
matplotlib.use("Agg")
 
import matplotlib.pyplot as plt
import numpy as np
 
import pyvolleydata
 
players = pyvolleydata.load_player_boxscore("mlv", 2026)
final = players[players["match_id"] == "2464512"]
 
skills = {
    "attack_kills": "Kills",
    "attack_attempts": "Attacks",
    "block_points": "Blocks",
    "digs": "Digs",
    "receptions": "Receptions",
}
 
totals = final.groupby(["first_name", "last_name"])[list(skills)].sum()
shares = totals / totals.max()
 
INHERIT = "#ff00ff"
 
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False)
closed = np.concatenate([angles, angles[:1]])
 
figure, axes = plt.subplots(figsize=(5.5, 5.5), subplot_kw={"projection": "polar"})
 
for (first, last), colour in (
    (("Sofia", "Maldonado Diaz"), "#e8452c"),
    (("Brooke", "Nuneviller"), "#4c9be8"),
):
    values = shares.loc[(first, last)].to_numpy()
    values = np.concatenate([values, values[:1]])
    axes.plot(closed, values, color=colour, linewidth=2, label=f"{first} {last}")
    axes.fill(closed, values, color=colour, alpha=0.15)
 
axes.set_xticks(angles)
axes.set_xticklabels(skills.values(), color=INHERIT)
axes.set_yticks([0.25, 0.5, 0.75, 1.0])
axes.set_yticklabels([])
axes.set_ylim(0, 1)
axes.spines["polar"].set_color(INHERIT)
axes.spines["polar"].set_alpha(0.45)
axes.grid(color=INHERIT, alpha=0.25)
axes.set_title("Visualizing Player Impact", pad=25, color=INHERIT)
axes.legend(
    loc="upper center",
    bbox_to_anchor=(0.5, -0.06),
    ncol=2,
    frameon=False,
    labelcolor=INHERIT,
)
 
buffer = StringIO()
plt.savefig(buffer, format="svg", bbox_inches="tight", transparent=True)
print(buffer.getvalue().replace(INHERIT, "currentColor"))
```
 
Maldonado Diaz's shape leans offensive, leading the match in kills and attack attempts, 
while Nuneviller's leans defensive, with far more digs and receptions.

## What else

`load_events_log` gives events such as rallys, substitutions, timeouts, `load_player_info` 
the rosters, `load_team_staff` the team staff, and `load_officials` the crew. Every loader 
takes a list of seasons or nothing at all for the full history. See the
[API reference](reference.md) for the details and the
[data dictionary](data-dictionary.md) for every column.