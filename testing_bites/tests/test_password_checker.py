import pytest
from lib.password_checker import PasswordChecker


class TestPresent:
    def test_check_method_with_short_pwd(self):
        pwc = PasswordChecker()
        with pytest.raises(Exception) as error:
            pwc.check("passwor")
        assert str(error.value) == "Invalid password, must be 8+ characters."

    def test_check_method_with_correct_length_pwd(self):
        pwc = PasswordChecker()
        assert pwc.check("password") == True
        assert pwc.check("thisisalongpassword123!") == True
