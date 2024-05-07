class Car:
    def __init__(self) -> None:
        self.tyres = []

    def add_tyres(self, tyres):
        self.tyres = [*self.tyres, *tyres]

    def get_latest_readings(self):
        results = []
        for tyre in self.tyres:
            date = tyre.readings[0]["date_taken"]
            results.append(
                f"{tyre.position} - pressure {tyre.pressure}psi / tread depth {tyre.tread_depth}mm taken on {date}"
            )
        return "\n".join(results)
