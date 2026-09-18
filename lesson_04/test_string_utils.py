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
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("$abc", "$abc"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.xfail(reason="BR-2", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_capitalize_negative_attribute_error(input_str):
    with pytest.raises(AttributeError):
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
    ("", ""),
    ("\tPython", "Python"),
    ("\nPython", "Python"),
    ("\rPython", "Python"),
    ("\vPython", "Python"),
    ("\fPython", "Python"),
    ("\u2005Python", "Python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.xfail(reason="BR-4", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_trim_negative_attribute_error(input_str):
    with pytest.raises(AttributeError):
        string_utils.trim(input_str)


@pytest.mark.positive
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("Victor", "V", True),
    ("Victor", "v", False),
    ("Victor", " ", False),
    ("Apple", "p", True),
    ("", "Я", False),
    ("Я", "", True),
    ("", "", True),
    ("   ", "", True),
    ("Два слова", "Два", True),
    ("Два слова", "слово", False),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.xfail(reason="BR-5", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    (None, 'a'),
    (123,  'a'),
    (4.56, 'a'),
    (True, 'a'),
    ({},   'a'),
])
def test_contains_negative_attribute_error(input_str, input_symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.xfail(reason="BR-6", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ([], 'a', False),
    (['a'], 'a', True),
    ((), 'a', False),
    (('a', 'b'), 'a', True),
])
def test_contains_negative(input_str, input_symbol, expected):
    print(f"input_str = {input_str}, input_symbol = {input_symbol}")
    print(f"result = {string_utils.contains(input_str, input_symbol)}")
    assert string_utils.contains(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ('a', None),
    ('a', 123),
    ('a', 4.56),
    ('a', True),
    ('a', []),
    ('a', ()),
    ('a', {}),
])
def test_contains_negative_type_error(input_str, input_symbol):
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
    ("Я", "", "Я"),
    ("", "", ""),
    ("   ", "", "   "),
])
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.xfail(reason="BR-7", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    (None, 'a'),
    (123,  'a'),
    (4.56, 'a'),
    (True, 'a'),
    ({},   'a'),
    (['a'], 'a'),
    (('a', 'b'), 'a'),
])
def test_delete_symbol_negative_attribute_error(input_str, input_symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(input_str, input_symbol)


@pytest.mark.xfail(reason="BR-8", strict=True)
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ([], 'a', []),
    ((), 'a', ()),
])
def test_delete_symbol_negative(input_str, input_symbol, expected):
    print(f"input_str = {input_str}, input_symbol = {input_symbol}")
    print(f"result = {string_utils.delete_symbol(input_str, input_symbol)}")
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ('a', None),
    ('a', 123),
    ('a', 4.56),
    ('a', True),
    ('a', []),
    ('a', ()),
    ('a', {}),
])
def test_delete_symbol_negative_type_error(input_str, input_symbol):
    # Ожидается ошибка: Неверный тип данных
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, input_symbol)
