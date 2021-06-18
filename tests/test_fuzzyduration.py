from fuzzyduration import __version__
from fuzzyduration import fuzzyDuration


def test_version():
    assert __version__ == "0.2.0"


def test_seconds():
    val = 32
    res = fuzzyDuration(val)
    assert res == "32 seconds"


def test_minutes():
    val = 143
    res = fuzzyDuration(val)
    assert res == "2 minutes"


def test_hours():
    val = 3601
    res = fuzzyDuration(val)
    assert res == "1 hour"


def test_days():
    val = 3600 * 24 * 3 + 3
    res = fuzzyDuration(val)
    assert res == "3 days"


def test_weeks():
    val = 3600 * 24 * 7 * 2 + 3
    res = fuzzyDuration(val)
    assert res == "2 weeks"


def test_year():
    val = 3600 * 24 * 7 * 102 + 3
    res = fuzzyDuration(val)
    assert res == "1 year"


def test_years():
    val = 3600 * 24 * 7 * 105 + 3
    res = fuzzyDuration(val)
    assert res == "2 years"


def test_exact_hours():
    val = 3600
    res = fuzzyDuration(val)
    assert res == "1 hour"


def test_exact_mins():
    val = 120
    res = fuzzyDuration(val)
    assert res == "2 minutes"
