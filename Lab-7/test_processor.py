
import string

import pytest
from hypothesis import given, strategies as st

from processor import minutes_parked, hourly_rate, format_plate


# -------------------------------------------------
# 1. MINUTES_PARKED TESTS
# -------------------------------------------------

@st.composite
def valid_intervals(draw):
    start = draw(st.integers(min_value=0, max_value=1439))
    duration = draw(st.integers(min_value=0, max_value=1439 - start))
    return start, duration


@given(valid_intervals())
def test_minutes_parked_valid_inputs(interval):
    start, duration = interval

    entry = f"{start // 60:02d}:{start % 60:02d}"
    end = start + duration
    exit_time = f"{end // 60:02d}:{end % 60:02d}"

    assert minutes_parked(f"{entry}-{exit_time}") == duration


@given(
    bad_hour=st.integers(min_value=24, max_value=999),
    minute=st.integers(min_value=0, max_value=59),
    end_hour=st.integers(min_value=0, max_value=23),
    end_minute=st.integers(min_value=0, max_value=59),
)
def test_minutes_parked_rejects_invalid_hours(
    bad_hour, minute, end_hour, end_minute
):
    value = (
        f"{bad_hour:02d}:{minute:02d}-"
        f"{end_hour:02d}:{end_minute:02d}"
    )

    with pytest.raises(ValueError):
        minutes_parked(value)


@given(
    bad_minute=st.integers(min_value=60, max_value=999),
    end_hour=st.integers(min_value=0, max_value=23),
    end_minute=st.integers(min_value=0, max_value=59),
)
def test_minutes_parked_rejects_invalid_minutes(
    bad_minute, end_hour, end_minute
):
    value = f"09:{bad_minute:02d}-{end_hour:02d}:{end_minute:02d}"

    with pytest.raises(ValueError):
        minutes_parked(value)


@given(start=st.integers(min_value=1, max_value=1439), data=st.data())
def test_minutes_parked_rejects_exit_before_entry(start, data):
    end = data.draw(st.integers(min_value=0, max_value=start - 1))

    entry = f"{start // 60:02d}:{start % 60:02d}"
    exit_time = f"{end // 60:02d}:{end % 60:02d}"

    with pytest.raises(ValueError):
        minutes_parked(f"{entry}-{exit_time}")


@given(
    value=st.one_of(
        st.none(),
        st.integers(),
        st.booleans(),
        st.lists(st.text()),
    )
)
def test_minutes_parked_rejects_non_string_inputs(value):
    with pytest.raises(TypeError):
        minutes_parked(value)


# -------------------------------------------------
# 2. HOURLY_RATE TESTS
# -------------------------------------------------

@given(
    vehicle=st.sampled_from(["bike", "car", "truck"]),
    before=st.text(alphabet=" \t", max_size=5),
    after=st.text(alphabet=" \t", max_size=5),
)
def test_hourly_rate_valid_inputs(vehicle, before, after):
    expected = {"bike": 10, "car": 30, "truck": 60}

    value = before + vehicle.upper() + after

    assert hourly_rate(value) == expected[vehicle]


@given(
    vehicle=st.text().filter(
        lambda v: v.strip().lower() not in {"bike", "car", "truck"}
    )
)
def test_hourly_rate_rejects_unknown_vehicles(vehicle):
    with pytest.raises(ValueError):
        hourly_rate(vehicle)


@given(
    value=st.one_of(
        st.none(),
        st.integers(),
        st.booleans(),
        st.lists(st.text()),
    )
)
def test_hourly_rate_rejects_non_string_inputs(value):
    with pytest.raises(TypeError):
        hourly_rate(value)


# -------------------------------------------------
# 3. FORMAT_PLATE TESTS
# -------------------------------------------------

@given(
    plate=st.text(
        alphabet=string.ascii_letters + string.digits,
        min_size=10,
        max_size=10,
    )
)
def test_format_plate_valid_inputs(plate):
    expected = (
        plate[:2].upper() + " " +
        plate[2:4].upper() + " " +
        plate[4:6].upper() + " " +
        plate[6:10].upper()
    )

    assert format_plate(plate) == expected


@given(
    plate=st.text().filter(
        lambda p: len(p) != 10 or not p.isascii() or not p.isalnum()
    )
)
def test_format_plate_rejects_malformed_plates(plate):
    with pytest.raises(ValueError):
        format_plate(plate)


@given(
    value=st.one_of(
        st.none(),
        st.integers(),
        st.booleans(),
        st.lists(st.text()),
    )
)
def test_format_plate_rejects_non_string_inputs(value):
    with pytest.raises(TypeError):
        format_plate(value)
