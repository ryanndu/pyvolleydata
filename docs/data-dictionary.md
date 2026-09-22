# Data dictionary

Every column in every dataset. The tables below are generated from the
published data at build time, so the column names and dtypes are always what
a loader actually returns.

Eight of the nine datasets have identical columns for all three leagues.
Only `schedule` differs: `parent_match_id` exists for LOVB and AU, which
settle a drawn series with a golden set, and not for MLV, which doesn't.

## `schedule`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_schedule("lovb")
descriptions = json.loads(Path("docs/columns.json").read_text())["schedule"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `sets`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_sets("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["sets"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `officials`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_officials("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["officials"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `player_info`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_player_info("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["player_info"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `team_staff`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_team_staff("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["team_staff"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `pbp`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_pbp("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["pbp"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `events_log`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_events_log("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["events_log"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `player_boxscore`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_player_boxscore("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["player_boxscore"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```

## `team_boxscore`

```python exec="true"
import json
from pathlib import Path

import pyvolleydata

frame = pyvolleydata.load_team_boxscore("mlv")
descriptions = json.loads(Path("docs/columns.json").read_text())["team_boxscore"]

print(f"{len(frame):,} rows, {len(frame.columns)} columns.\n")
print("| Column | Type | Description |")
print("| --- | --- | --- |")
for column in frame.columns:
    print(f"| `{column}` | `{frame[column].dtype}` | {descriptions.get(column, '')} |")
```