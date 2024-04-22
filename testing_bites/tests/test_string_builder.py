from lib.string_builder import StringBuilder


class TestStringBuilder:
    def test_instance_initialises_to_empty_str(self):
        sb = StringBuilder()
        assert sb.str == ""

    def test_add_method_changes_str(self):
        sb = StringBuilder()
        sb.add("Hello")
        assert sb.str == "Hello"

    def test_add_method_with_multiple_calls(self):
        sb = StringBuilder()
        sb.add("Hello")
        sb.add("World")
        assert sb.str == "HelloWorld"

    def test_size_method_returns_correct_length(self):
        sb = StringBuilder()
        sb.add("Hello")
        assert sb.size() == 5
        sb.add("World")
        assert sb.size() == 10

    def test_output_returns_correct_string(self):
        sb = StringBuilder()
        sb.add("Hello")
        assert sb.output() == "Hello"
        sb.add("World")
        assert sb.output() == "HelloWorld"
