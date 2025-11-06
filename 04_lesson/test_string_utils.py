from string_utils import StringUtils

utils = StringUtils()


# Тесты для capitalize
def test_capitalize_positive_string():
    result = utils.capitalize("skypro")
    assert result == "Skypro"


def test_capitalize_empty_string():
    result = utils.capitalize("")
    assert result == ""


def test_capitalize_already_capitalized():
    result = utils.capitalize("Skypro")
    assert result == "Skypro"


# Тесты для trim
def test_trim_positive():
    result = utils.trim("  skypro")
    assert result == "skypro"


def test_trim_only_space():
    result = utils.trim("  ")
    assert result == ""


def test_trim_no_space():
    result = utils.trim("skypro")
    assert result == "skypro"


# Тесты для contains
def test_contains_positive():
    result = utils.contains("Skypro", "S")
    assert result is True


def test_contains_negative():
    result = utils.contains("SkyPro", "U")
    assert result is False


def test_contains_empty_symbol():
    result = utils.contains("SkyPro", "")
    assert result is True


def test_contains_empty_string():
    result = utils.contains("", "S")
    assert result is False


# Тесты для delete_symbol
def test_delete_symbol_positive():
    result = utils.delete_symbol("SkyPro", "o")
    assert result == "SkyPr"


def test_delete_symbol_negative():
    result = utils.delete_symbol("SkyPro", "f")
    assert result == "SkyPro"


def test_delete_symbol_word():
    result = utils.delete_symbol("SkyPro", "Sky")
    assert result == "Pro"


def test_delete_symbol_no_match():
    result = utils.delete_symbol("SkyPro", "U")
    assert result == "SkyPro"


def test_delete_symbol_empty_string():
    result = utils.delete_symbol("", "a")
    assert result == ""
