"""Verify that the prefix and suffix functions work correctly."""

from words import prefix, suffix
import pytest


def test_prefix():
    """Verify that the prefix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the prefix function and verify that it returns a string.
    pre = prefix("upbeat", "upgrade")
    assert isinstance(pre, str), "prefix function must return a string"

    # Call the prefix function ten times and use an assert
    # statement to verify that the string returned by the
    # prefix function is correct each time.
    assert prefix("cat", "catalog") == "cat"
    assert prefix("", "") == ""
    assert prefix("", "correct") == ""
    assert prefix("clear", "") == ""
    assert prefix("happy", "funny") == ""
    assert prefix("cat", "catalog") == "cat"
    assert prefix("dogmatic", "dog") == "dog"
    assert prefix("jump", "joyous") == "j"
    assert prefix("upbeat", "upgrade") == "up"
    assert prefix("Disable", "dIstasteful") == "dis"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.

def test_suffix():
    """Verify that the suffix function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the suffix function and verify that it returns a string.
    suf = suffix("upbeat", "upgrade")
    assert isinstance(suf, str), "suffix function must return a string"

    # Call the suffix function ten times and use an assert
    # statement to verify that the string returned by the
    # suffix function is correct each time.
    assert suffix("", "") == ""
    assert suffix("", "correct") == ""
    assert suffix("clear", "") == ""
    assert suffix("happy", "funny") == "y"
    assert suffix("angelic", "awesome") == ""
    assert suffix("found", "profound") == "found"
    assert suffix("ditch", "itch") == "itch"
    assert suffix("tired", "fatigued") == "ed"
    assert suffix("swimming", "FLYING") == "ing"

pytest.main(["-v", "--tb=line", "-rN", __file__])
