"""Tests designed to exercise both outcomes of every decision in parking_fee.py."""

import pytest

from parking_fee import find_slot, monthly_pass, parking_fee


@pytest.mark.parametrize(
    ("vehicle", "minutes", "is_ev", "lost_ticket", "expected"),
    [
        # vehicle validation: known and unknown
        ("bus", 60, False, False, None),
        # duration validation: negative and non-negative
        ("car", -1, False, False, None),
        # free-stay decision: <= 30 and > 30
        ("bike", 30, False, False, 0),
        ("truck", 31, False, False, 60),
        # rounding decision: exact hour and remainder
        ("car", 60, False, False, 30),
        ("car", 61, False, False, 60),
        # EV decision: true and false; vehicle exception: truck and non-truck
        ("bike", 60, True, False, 5),
        ("truck", 60, True, False, 60),
        ("car", 60, False, False, 30),
        # lost-ticket decision: true and false
        ("car", 60, False, True, 230),
        ("bike", 60, True, True, 205),
    ],
)
def test_parking_fee_branch_outcomes(vehicle, minutes, is_ev, lost_ticket, expected):
    if vehicle == "bus":
        with pytest.raises(ValueError, match="unknown vehicle"):
            parking_fee(vehicle, minutes, is_ev, lost_ticket)
    elif minutes < 0:
        with pytest.raises(ValueError, match="invalid duration"):
            parking_fee(vehicle, minutes, is_ev, lost_ticket)
    else:
        assert parking_fee(vehicle, minutes, is_ev, lost_ticket) == expected


@pytest.mark.parametrize(
    ("vehicle", "free_slots", "is_disabled", "expected"),
    [
        # free_slots <= 0 true/false; disabled true/false;
        # truck true/false (only evaluated when earlier decisions are false)
        ("car", 0, False, "full"),
        ("car", 1, True, "ground floor"),
        ("truck", 1, False, "basement"),
        ("bike", 1, False, "any floor"),
    ],
)
def test_find_slot_branch_outcomes(vehicle, free_slots, is_disabled, expected):
    assert find_slot(vehicle, free_slots, is_disabled) == expected


@pytest.mark.parametrize(
    ("vehicle", "is_resident", "expected"),
    [
        # bike true, car (bike false then car true), unsupported (both false)
        ("bike", False, 500),
        ("bike", True, 400),
        ("car", False, 1500),
        ("car", True, 1200),
        ("truck", False, None),
    ],
)
def test_monthly_pass_branch_outcomes(vehicle, is_resident, expected):
    if vehicle == "truck":
        with pytest.raises(ValueError, match="no pass for this vehicle"):
            monthly_pass(vehicle, is_resident)
    else:
        assert monthly_pass(vehicle, is_resident) == expected
