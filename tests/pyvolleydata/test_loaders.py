from datetime import UTC, datetime

import pytest

from pyvolleydata.loaders import LEAGUES, _validate_league, _validate_seasons


class TestValidateLeague:
    def test_every_published_league_passes(self):
        for league in LEAGUES:
            assert _validate_league(league) == league

    def test_case_is_ignored(self):
        assert _validate_league("MLV") == "mlv"
        assert _validate_league("Lovb") == "lovb"

    def test_unknown_league_raises(self):
        with pytest.raises(ValueError):
            _validate_league("nba")

    def test_retired_league_name_raises(self):
        with pytest.raises(ValueError):
            _validate_league("pvf")

    def test_non_string_league_raises(self):
        with pytest.raises(TypeError):
            _validate_league(None)

        with pytest.raises(TypeError):
            _validate_league(2025)


class TestValidateSeasons:
    def test_none_returns_every_season(self):
        assert _validate_seasons("mlv", None) == list(range(2024, datetime.now(UTC).year + 1))
        assert _validate_seasons("lovb", None) == list(range(2025, datetime.now(UTC).year + 1))
        assert _validate_seasons("aupvb", None) == list(range(2022, datetime.now(UTC).year + 1))

    def test_int_becomes_a_list(self):
        assert _validate_seasons("mlv", 2025) == [2025]

    def test_list_passes_through(self):
        assert _validate_seasons("lovb", [2025, 2026]) == [2025, 2026]

    def test_range_is_per_league(self):
        assert _validate_seasons("aupvb", 2022) == [2022]

        with pytest.raises(ValueError):
            _validate_seasons("mlv", 2022)

    def test_season_out_of_range_raises(self):
        with pytest.raises(ValueError):
            _validate_seasons("lovb", 2024)

        with pytest.raises(ValueError):
            _validate_seasons("mlv", datetime.now(UTC).year + 1)

    def test_non_int_season_raises(self):
        with pytest.raises(TypeError):
            _validate_seasons("mlv", "2025")

        with pytest.raises(TypeError):
            _validate_seasons("mlv", [2024, "2025"])

    def test_bool_is_not_a_season(self):
        with pytest.raises(TypeError):
            _validate_seasons("mlv", True)

        with pytest.raises(TypeError):
            _validate_seasons("mlv", [True])
