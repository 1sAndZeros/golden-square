from ..lib.car import Car
from ..lib.tyre import Tyre
from unittest.mock import MagicMock
import datetime


def test_instance_initialises_correctly():
    car = Car()
    assert car.tyres == []


def test_add_tyres():
    car = Car()

    front_left = Tyre("front left", 30, 1.8)
    front_right = Tyre("front right", 30, 1.8)
    rear_left = Tyre("rear left", 30, 1.8)
    rear_right = Tyre("rear right", 30, 1.8)
    car.add_tyres([front_left, front_right, rear_left, rear_right])

    assert car.tyres == [front_left, front_right, rear_left, rear_right]


def test_get_latest_readings(monkeypatch):
    FAKE_NOW = datetime.datetime(2024, 1, 1)
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = FAKE_NOW
    monkeypatch.setattr(datetime, "datetime", datetime_mock)

    car = Car()
    front_left = Tyre("front left", 30, 1.8)
    front_right = Tyre("front right", 31, 1.9)
    rear_left = Tyre("rear left", 32, 2.0)
    rear_right = Tyre("rear right", 33, 2.1)
    car.add_tyres([front_left, front_right, rear_left, rear_right])
    result = car.get_latest_readings()
    assert (
        result
        == """front left - pressure 30psi / tread depth 1.8mm taken on 01/01/2024
front right - pressure 31psi / tread depth 1.9mm taken on 01/01/2024
rear left - pressure 32psi / tread depth 2.0mm taken on 01/01/2024
rear right - pressure 33psi / tread depth 2.1mm taken on 01/01/2024"""
    )
