from lib.counter import Counter


class TestCounter:
    def test_counter_initialises_to_zero(self):
        counter = Counter()
        assert counter.count == 0

    def test_add_method_increases_counter_when_called_once(self):
        counter = Counter()
        counter.add(1)
        assert counter.count == 1

    def test_add_method_increases_counter_when_called_multiple_times(self):
        counter = Counter()
        counter.add(1)
        assert counter.count == 1
        counter.add(3)
        assert counter.count == 4
        counter.add(2)
        counter.add(10)
        assert counter.count == 16

    def test_report_method_returns_correct_count(self):
        counter = Counter()
        counter.add(3)
        output = counter.report()
        assert output == "Counted to 3 so far."
