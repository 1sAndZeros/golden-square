from ..lib.CatFacts import CatFacts
from unittest.mock import Mock


class TestCatFacts:
    def test_provide_method(self):
        requests_mock = Mock(name="requests")
        response_mock = Mock(name="response")

        response_mock.json.return_value = {
            "fact": "A cat's appetite is the barometer of its health. Any cat that does not eat or drink for more than two days should be taken to a vet.",
            "length": 132,
        }

        requests_mock.get.return_value = response_mock

        cat_facts = CatFacts(requests=requests_mock)
        assert (
            cat_facts.provide()
            == "Cat fact: A cat's appetite is the barometer of its health. Any cat that does not eat or drink for more than two days should be taken to a vet."
        )
