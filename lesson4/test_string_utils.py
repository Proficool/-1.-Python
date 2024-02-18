
from string_utils import StringUtils
import pytest

@pytest.fixture
def utils():
    return StringUtils()

# Позитивные тесты
def test_capitalize_positive(utils):
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("скайпро") == "Скайпро"

def test_trim_positive(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("  скайпро") == "скайпро"
    assert utils.trim("  skypro plus") == "skypro plus"

def test_to_list_positive(utils):
    assert utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    assert utils.to_list("к,л,м,н") == ["к", "л", "м", "н"]
    assert utils.to_list("k:l:m:n", ":") == ["k", "l", "m","n"]

def test_contains_positive(utils):
    assert utils.contains("SkyPro", "y") is True
    assert utils.contains("Скайпро", "й") is True
    
def test_delete_symbol_positive(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    assert utils.delete_symbol("Скайпро", "й") == "Скапро"
    assert utils.delete_symbol("Скайпро", "про") == "Скай"

def test_starts_with_positive(utils):
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with("Скайпро", "С") is True

def test_end_with_positive(utils):
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("Скайпро", "о") is True

def test_is_empty_positive(utils):
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("SkyPro") is False

def test_list_to_string_positive(utils):
    assert utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"

# Негативные тесты
def test_contains_negative(utils):
    assert utils.contains("SkyPro", "U") is False
    assert utils.contains("Как дела?", "!") is False

def test_delete_symbol_symbol_not_found(utils):
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
    assert utils.delete_symbol("Скайпро", "м") == "Скайпро"

def test_starts_with_negative(utils):
    assert utils.starts_with("SkyPro", "P") is False
    assert utils.starts_with("Скайпро", "й") is False

def test_end_with_negative(utils):
    assert utils.end_with("SkyPro", "y") is False
    assert utils.end_with("Скайпро", "й") is False

def test_is_empty_negative(utils):
    assert utils.is_empty("SkyPro") is False
    assert utils.is_empty("   Скайпро") is False

