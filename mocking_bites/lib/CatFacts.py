import requests


class CatFacts:

    def __init__(self, requests=requests) -> None:
        self.requests = requests

    def provide(self):
        return f"Cat fact: {self._get_cat_fact()['fact']}"

    # Again, don't stub this method.
    def _get_cat_fact(self):
        response = self.requests.get("https://catfact.ninja/fact")
        print(response.json())
        return response.json()
