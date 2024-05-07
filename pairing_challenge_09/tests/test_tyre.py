from ..lib.tyre import Tyre
from unittest.mock import MagicMock
import datetime


def test_instance_initialises_correctly(monkeypatch):

    FAKE_NOW = datetime.datetime(2024, 1, 1)
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = FAKE_NOW
    monkeypatch.setattr(datetime, "datetime", datetime_mock)

    front_left_tyre = Tyre("front left", 30, 1.8)
    assert front_left_tyre.position == "front left"
    assert front_left_tyre.pressure == 30
    assert front_left_tyre.tread_depth == 1.8
    assert front_left_tyre.readings == [
        {"pressure": 30, "tread_depth": 1.8, "date_taken": "01/01/2024"}
    ]


def test_make_reading(monkeypatch):

    FAKE_NOW = datetime.datetime(2024, 4, 1)
    datetime_mock = MagicMock(wraps=datetime.datetime)
    datetime_mock.now.return_value = FAKE_NOW
    monkeypatch.setattr(datetime, "datetime", datetime_mock)

    front_left_tyre = Tyre("front left", 30, 1.8)
    front_left_tyre.make_reading(40, 3.5)
    assert front_left_tyre.readings == [
        {"pressure": 30, "tread_depth": 1.8, "date_taken": "01/04/2024"},
        {"pressure": 40, "tread_depth": 3.5, "date_taken": "01/04/2024"},
    ]
