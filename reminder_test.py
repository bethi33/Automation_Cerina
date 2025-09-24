import pytest
from datetime import datetime

def format_reminder_time(time_str: str, locale: str) -> str:
    dt = datetime.strptime(time_str, "%H:%M")
    if locale == "en-GB":
        return dt.strftime("%H:%M")   # 24h format
    elif locale == "en-US":
        return dt.strftime("%I:%M %p").lstrip("0")  # 12h format
    else:
        return time_str

@pytest.mark.parametrize("time_str, locale, expected", [
    ("20:00", "en-GB", "20:00"),
    ("20:00", "en-US", "8:00 PM"),
    ("08:05", "en-GB", "08:05"),
    ("08:05", "en-US", "8:05 AM"),
])
def test_reminder_time_formatting(time_str, locale, expected):
    assert format_reminder_time(time_str, locale) == expected
@pytest.mark.parametrize("time_str, locale, expected", [
    ("00:00", "en-GB", "00:00"),
    ("00:00", "en-US", "12:00 AM"),
    ("12:00", "en-GB", "12:00"),
    ("12:00", "en-US", "12:00 PM"),
])
def test_reminder_time_formatting_midnight_noon(time_str, locale, expected):
    assert format_reminder_time(time_str, locale) == expected