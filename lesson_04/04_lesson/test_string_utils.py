import pytest
from string_utils import StringUtils

class TestStringUtils:
    
    @pytest.mark.parametrize('input_str, expected', [
        ("skypro", "Skypro"),
        ("hello world", "Hello world"),
        ("", ""),
        ("123", "123"),
        (" skypro", " skypro")
    ])
    def test_capitalize(self, input_str, expected):
        assert StringUtils.capitalize(input_str) == expected

  
    @pytest.mark.parametrize('input_str, expected', [
        ("   skypro", "skypro"),
        ("  hello  ", "hello  "),
        ("", ""),
        ("skypro", "skypro"),
        ("\t\nskypro", "skypro")
    ])
    def test_trim(self, input_str, expected):
        assert StringUtils.trim(input_str) == expected

    
    @pytest.mark.parametrize('input_str, delimiter, expected', [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3", ":", ["1", "2", "3"]),
        ("", ",", []),
        ("a b c", " ", ["a", "b", "c"]),
        ("single", ",", ["single"])
    ])
    def test_to_list(self, input_str, delimiter, expected):
        assert StringUtils.to_list(input_str, delimiter) == expected

    
    @pytest.mark.parametrize('string, symbol, expected', [
        ("Skypro", "S", True),
        ("Skypro", "k", True),
        ("Skypro", "U", False),
        ("", "a", False),
        ("123", "2", True)
    ])
    def test_contains(self, string, symbol, expected):
        assert StringUtils.contains(string, symbol) == expected

    
    @pytest.mark.parametrize('string, symbol, expected', [
        ("Skypro", "k", "Sypro"),
        ("Skypro", "pro", "Sky"),
        ("Hello hello", "ell", "Ho ho"),
        ("No changes", "z", "No changes"),
        ("", "a", "")
    ])
    def test_delete_symbol(self, string, symbol, expected):
        assert StringUtils.delete_symbol(string, symbol) == expected

    
    @pytest.mark.parametrize('string, symbol, expected', [
        ("Skypro", "S", True),
        ("Skypro", "Sky", True),
        ("Skypro", "P", False),
        ("", "a", False),
        ("123", "1", True)
    ])
    def test_starts_with(self, string, symbol, expected):
        assert StringUtils.starts_with(string, symbol) == expected

   
    @pytest.mark.parametrize('string, symbol, expected', [
        ("Skypro", "o", True),
        ("Skypro", "pro", True),
        ("Skypro", "y", False),
        ("", "a", False),
        ("123", "3", True)
    ])
    def test_end_with(self, string, symbol, expected):
        assert StringUtils.end_with(string, symbol) == expected

    
    @pytest.mark.parametrize('string, expected', [
        ("", True),
        (" ", True),
        ("\t\n", True),
        ("Skypro", False),
        ("  a  ", False)
    ])
    def test_is_empty(self, string, expected):
        assert StringUtils.is_empty(string) == expected

    
    @pytest.mark.parametrize('lst, delimiter, expected', [
        (["a", "b", "c"], ", ", "a, b, c"),
        (["1", "2", "3"], "-", "1-2-3"),
        ([], ", ", ""),
        (["single"], ", ", "single"),
        ([1, 2, 3], ":", "1:2:3")
    ])
    def test_list_to_string(self, lst, delimiter, expected):
        assert StringUtils.list_to_string(lst, delimiter) == expected