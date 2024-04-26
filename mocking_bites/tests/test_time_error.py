from ..lib.TimeError import TimeError
from unittest.mock import Mock


class TestTimeError:
    def test_error_method(self):
        time_mock = Mock(name="time")
        time_mock.time.return_value = 1714128477.5

        requests_mock = Mock(name="requests")
        response_mock = Mock(name="response")

        response_mock.json.return_value = {
            "abbreviation": "BST",
            "client_ip": "62.49.20.41",
            "datetime": "2024-04-26T11:50:41.325333+01:00",
            "day_of_week": 5,
            "day_of_year": 117,
            "dst": True,
            "dst_from": "2024-03-31T01:00:00+00:00",
            "dst_offset": 3600,
            "dst_until": "2024-10-27T01:00:00+00:00",
            "raw_offset": 0,
            "timezone": "Europe/London",
            "unixtime": 1714128477,
            "utc_datetime": "2024-04-26T10:50:41.325333+00:00",
            "utc_offset": "+01:00",
            "week_number": 17,
        }

        requests_mock.get.return_value = response_mock
        print(response_mock.json())
        te = TimeError(time=time_mock, requests=requests_mock)
        assert te.error() == -0.5
