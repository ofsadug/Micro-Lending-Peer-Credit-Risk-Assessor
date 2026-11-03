"""Tests designed to execute every executable line in parking_fee.py."""

import pytest

from parking_fee import find_slot, monthly_pass, parking_fee


def test_parking_fee_rejects_unknown_vehicle():
    with pytest.raises(ValueError, match="unknown vehicle"):
        parking_fee("bus", 60, False, False)


def test_parking_fee_rejects_negative_duration():
    with pytest.raises(ValueError, match="invalid duration"):
        parking_fee("car", -1, False, False)


@pytest.mark.parametrize(
    ("vehicle", "minutes", "expected"),
    [
        ("bike", 0, 0),
        ("car", 30, 0),
        ("truck", 31, 60),
        ("bike", 60, 10),
        ("car", 61, 60),
        ("truck", 120, 120),
    ],
)
def test_parking_fee_duration_paths(vehicle, minutes, expected):
    assert parking_fee(vehicle, minutes, False, False) == expected


def test_parking_fee_ev_discount_for_bike_and_car():
    assert parking_fee("bike", 60, True, False) == 5
    assert parking_fee("car", 61, True, False) == 30


def test_parking_fee_ev_does_not_discount_truck():
    assert parking_fee("truck", 61, True, False) == 120


def test_parking_fee_lost_ticket_surcharge():
    assert parking_fee("car", 60, False, True) == 230


def test_parking_fee_ev_and_lost_ticket_combined():
    assert parking_fee("bike", 60, True, True) == 205


def test_find_slot_all_return_paths():
    assert find_slot("car", 0, False) == "full"
    assert find_slot("car", 1, True) == "ground floor"
    assert find_slot("truck", 1, False) == "basement"
    assert find_slot("bike", 1, False) == "any floor"


def test_monthly_pass_bike_and_car_with_resident_discount():
    assert monthly_pass("bike", True) == 400
    assert monthly_pass("car", True) == 1200


def test_monthly_pass_bike_and_car_without_discount():
    assert monthly_pass("bike", False) == 500
    assert monthly_pass("car", False) == 1500


def test_monthly_pass_rejects_unsupported_vehicle():
    with pytest.raises(ValueError, match="no pass for this vehicle"):
        monthly_pass("truck", False)
