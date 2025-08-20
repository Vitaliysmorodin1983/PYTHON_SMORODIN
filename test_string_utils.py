import pytest
from string_utils import StringUtils

class TestStringUtils:
    def test_capitalize_positive(self):
        assert StringUtils.capitalize("skypro") == "Skypro"
        assert StringUtils.capitalize("hello") == "Hello"
        
    def test_capitalize_negative(self):
        assert StringUtils.capitalize("") == ""
        assert StringUtils.capitalize("123") == "123"
        
    def test_trim_positive(self):
        assert StringUtils.trim("   skypro") == "skypro"
        assert StringUtils.trim("  hello") == "hello"
        
    def test_trim_negative(self):
        assert StringUtils.trim("") == ""
        assert StringUtils.trim("skypro   ") == "skypro   "
        
    