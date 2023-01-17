import main
from datetime import date, time


def test_generate_calendar_for_day():
    start_date = date(2020, 1, 1)
    end_date = date(2020, 1, 2)

    result = main.generate_calendar(start_date, end_date)

    assert len(result) == 48

    # First record
    assert result["Date"].iloc[0] == date(2020, 1, 1)
    assert result["Time"].iloc[0] == time(00, 00)
    assert result["Period"].iloc[0] == 1

    # Last record
    assert result["Date"].iloc[-1] == date(2020, 1, 1)
    assert result["Time"].iloc[-1] == time(23, 30)
    assert result["Period"].iloc[-1] == 48


def test_generate_calendar_for_month():
    start_date = date(2020, 1, 1)
    end_date = date(2020, 2, 1)

    result = main.generate_calendar(start_date, end_date)

    assert len(result) == 48 * 31

    # First record
    assert result["Date"].iloc[0] == date(2020, 1, 1)
    assert result["Time"].iloc[0] == time(00, 00)
    assert result["Period"].iloc[0] == 1

    # Some other record
    assert result["Date"].iloc[120] == date(2020, 1, 3)
    assert result["Time"].iloc[120] == time(12, 00)
    assert result["Period"].iloc[120] == 25

    # Last record
    assert result["Date"].iloc[-1] == date(2020, 1, 31)
    assert result["Time"].iloc[-1] == time(23, 30)
    assert result["Period"].iloc[-1] == 48


def test_generate_calendar_for_instant():
    start_date = date(2020, 1, 1)
    end_date = start_date

    result = main.generate_calendar(start_date, end_date)

    assert len(result) == 0


def test_generate_calendar_for_start_after_end():
    start_date = date(2020, 1, 2)
    end_date = date(2020, 1, 1)

    result = main.generate_calendar(start_date, end_date)

    assert len(result) == 0
