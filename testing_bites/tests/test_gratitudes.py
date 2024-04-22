from lib.gratitudes import Gratitudes


class TestGratitudes:
    def test_instance_initialises_to_empty_list(self):
        gratitudes = Gratitudes()
        assert gratitudes.gratitudes == []

    def test_add_method_adds_new_items_to_list(self):
        gratitudes = Gratitudes()
        gratitudes.add("Family")
        assert len(gratitudes.gratitudes) == 1
        assert "Family" in gratitudes.gratitudes
        gratitudes.add("Health")
        assert len(gratitudes.gratitudes) == 2
        assert gratitudes.gratitudes[-1] == "Health"

    def test_format_method(self):
        gratitudes = Gratitudes()
        gratitudes.add("Family")
        assert gratitudes.format() == "Be grateful for: Family"
        gratitudes.add("Health")
        assert gratitudes.format() == "Be grateful for: Family, Health"
        gratitudes.add("Friends")
        assert gratitudes.format() == "Be grateful for: Family, Health, Friends"
