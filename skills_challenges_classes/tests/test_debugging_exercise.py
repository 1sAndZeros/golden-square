from ..lib.debugging_exercise import *


def test_say_hello_with_kay():
    assert say_hello("kay") == "hello kay"


def test_encode():
    assert (
        encode("theswiftfoxjumpedoverthelazydog", "secretkey")
        == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"
    )


def test_decode():
    assert (
        decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
        == "theswiftfoxjumpedoverthelazydog"
    )
