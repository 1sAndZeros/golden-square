from testing_bites.lib.greet import greet


def test_greet_returns_hello_and_name():
    assert greet("Rikie") == "Hello, Rikie!"
