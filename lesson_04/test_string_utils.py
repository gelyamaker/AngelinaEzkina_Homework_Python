import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("victor", "Victor"),
    ("Apple", "Apple"),
    ("я", "Я"),
    ("Ночь. Улица. Фонарь. Аптека.", "Ночь. Улица. Фонарь. Аптека."),
    ("fINISH", "FINISH"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("$abc", "$abc"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_capitalize_negative_no_string(input_str):
    # Ожидается ошибка: Неверный тип данных
    with pytest.raises(TypeError):
        string_utils.capitalize(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Victor", "Victor"),
    ("    student", "student"),
    (" Apple ", "Apple "),
    ("Россия", "Россия"),
    ("end   ", "end   "),
    ("   ", ""),
    ("Два слова", "Два слова"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_trim_negative_no_string(input_str):
    # Ожидается ошибка: Неверный тип данных
    with pytest.raises(TypeError):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Victor", "V", True),
    ("Victor", "v", False),
    ("Victor", " ", False),
    ("Apple", "p", True),
    ("", "Я", False),
    ([], "Я", False),
    ((), "Я", False),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Я", ""),
    ("", ""),
    ("   ", ""),
    ("Два слова", "Два"),
    ("Два слова", "слово"),
])
def test_contains_negative(input_str, input_symbol):
    # Ожидается ошибка: длина input_symbol должна быть равна 1
    with pytest.raises(ValueError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    (None, 'a'),
    (123,  'a'),
    (4.56, 'a'),
    (True, 'a'),
    ([],   'a'),
    ((),   'a'),
    ({},   'a'),
    ('a', None),
    ('a', 123),
    ('a', 4.56),
    ('a', True),
    ('a', []),
    ('a', ()),
    ('a', {}),
])
def test_contains_negative_no_string(input_str, input_symbol):
    # Ожидается ошибка: Неверный тип данных
    with pytest.raises(TypeError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Victor", "V", "ictor"),
    (" Apple ", " ", "Apple"),
    ("Apple", "p", "Ale"),
    ("Два слова", "Два", " слова"),
    ("Victor", "v", "Victor"),
    ("", "Я", ""),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ("Я", ""),
    ("", ""),
    ("   ", ""),
])
def test_delete_symbol_negative(input_str, input_symbol):
    # Ожидается ошибка: input_symbol не должна быть пустой
    with pytest.raises(ValueError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    (None, 'a'),
    (123, 'a'),
    (4.56, 'a'),
    (True, 'a'),
    ([], 'a'),
    ((), 'a'),
    ({}, 'a'),
    ('a', None),
    ('a', 123),
    ('a', 4.56),
    ('a', True),
    ('a', []),
    ('a', ()),
    ('a', {}),
])
def test_delete_symbol_negative_no_string(input_str, input_symbol):
    # Ожидается ошибка: Неверный тип данных
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, input_symbol)
