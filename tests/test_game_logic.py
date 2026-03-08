import pytest

from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)

# --- check_guess ----------------------------------------------------------------

def test_winning_guess():
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in msg


def test_guess_too_high():
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    assert "HIGHER" in msg


def test_guess_too_low():
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "LOWER" in msg

# string-secret case (glitch)

def test_check_guess_string_secret():
    outcome, _ = check_guess(5, "5")
    assert outcome == "Win"

# --- parse_guess ----------------------------------------------------------------

def test_parse_guess_valid_integer():
    ok, val, err = parse_guess("42")
    assert ok
    assert val == 42
    assert err is None


def test_parse_guess_float_string():
    ok, val, err = parse_guess("3.0")
    assert ok
    assert val == 3


def test_parse_guess_empty_and_none():
    for raw in (None, ""):
        ok, val, err = parse_guess(raw)
        assert not ok
        assert val is None
        assert "Enter a guess" in err


def test_parse_guess_invalid():
    ok, val, err = parse_guess("abc")
    assert not ok
    assert val is None
    assert "not a number" in err

# --- get_range_for_difficulty ----------------------------------------------------

def test_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)
    # unknown difficulty should fall back to normal range
    assert get_range_for_difficulty("Whatever") == (1, 100)

# --- update_score ---------------------------------------------------------------

def test_update_score_win_first_attempt():
    # first attempt should give 100 points (100 - 10 * 0)
    assert update_score(0, "Win", 1) == 100


def test_update_score_win_late_minimum():
    # even if many attempts, floor of 10 points applies
    assert update_score(0, "Win", 20) == 10


def test_update_score_too_high_parity():
    # attempt 1 (odd) should subtract 5
    assert update_score(10, "Too High", 1) == 5
    # attempt 2 (even) should add 5
    assert update_score(10, "Too High", 2) == 15


def test_update_score_too_low_always_subtracts():
    assert update_score(10, "Too Low", 1) == 5
    assert update_score(10, "Too Low", 5) == 5


def test_update_score_other_outcome_no_change():
    assert update_score(42, "???", 3) == 42
