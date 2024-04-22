from lib.high_value import HighValue

def test_instance_initialises_correctly():
    high_value = HighValue(10, 20)
    assert high_value.value_first == 10
    assert high_value.value_second == 20

def test_get_highest_where_first_is_highest():
    high_value = HighValue(20,10)
    assert high_value.get_highest() == "First value is higher"

def test_get_highest_where_second_is_highest():
    high_value = HighValue(10, 20)
    assert high_value.get_highest() == "Second value is higher"

def test_get_highest_where_values_are_equal():
    high_value = HighValue(10, 10)
    assert high_value.get_highest() == "Values are equal"

def test_add_method_adds_amount_to_first():
    high_value = HighValue(10, 20)
    high_value.add(5, "first")
    assert high_value.value_first == 15

def test_add_method_adds_amount_to_second():
    high_value = HighValue(10, 20)
    high_value.add(5, "second")
    assert high_value.value_second == 25