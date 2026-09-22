# Changelog

## v2.0.0 (2026-09-21)

A rebuild against the new volleydata release, which republished every dataset
with new columns, explicit nullable dtypes, and parquet in place of CSV. Code
written against v1 will need updating, the notes below cover what changed.

### Changes

- League codes are `mlv`, `lovb` and `aupvb`.
- Import the loaders from the package itself, as
  `from pyvolleydata import load_schedule`. The `pyvolleydata.get_data` module
  has been removed.
- Every dataset's columns have been renamed or restructured to match the new
  release. The [data dictionary](https://ryanndu.github.io/pyvolleydata/data-dictionary/)
  lists every column in every dataset.
- `load_sets`, for the ninth dataset: one row per team per set, with the six
  starting court positions, points scored, who served first, and the set's
  start and end times.
- The documentation has moved to
  [ryanndu.github.io/pyvolleydata](https://ryanndu.github.io/pyvolleydata/).
- Data is read as parquet, so `pyarrow` is now a dependency.

## v1.0.1 (2026-02-01)

- Fixed a bug in `load_team_boxscore`.

## v1.0.0 (2026-01-31)

- Every loader now covers all supported leagues, selected with a `league`
  argument.

## v0.1.3 (2025-10-22)

- `load_player_boxscore` now shows substitutions correctly in the
  `set_starting_position` column.

## v0.1.2 (2025-10-20)

- Renamed the old `player_boxscore` dataset to `player_info`.
- Added new `load_player_boxscore` and `load_team_boxscore` functions.

## v0.1.1 (2025-08-12)

- Fixed typos across the documentation.
- Expanded the documentation.

## v0.1.0 (2025-07-15)

- Initial release.