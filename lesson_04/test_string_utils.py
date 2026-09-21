import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("victor", "Victor"),
    ("Apple", "Apple"),
    ("я", "Я"),
    pytest.param("Ночь. Улица. Фонарь. Аптека", "Ночь. Улица. Фонарь. Аптека",
                 marks=pytest.mark.xfail(strict=True, reason="BR-1")),
    pytest.param("fINISH", "FINISH",
                 marks=pytest.mark.xfail(strict=True, reason="BR-1")),
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("$abc", "$abc"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.xfail(strict=True,
                   reason="BR-2: Вместо TypeError летит AttributeError")
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_capitalize_raises_type_error(input_str):
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
    ("", ""),
    pytest.param("\tPython", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
    pytest.param("\nPython", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
    pytest.param("\rPython", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
    pytest.param("\vPython", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
    pytest.param("\fPython", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
    pytest.param("\u2005Python", "Python",
                 marks=pytest.mark.xfail(strict=True, reason="BR-3")),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.xfail(strict=True,
                   reason="BR-4: Вместо TypeError летит AttributeError")
@pytest.mark.negative
@pytest.mark.parametrize("input_str", [None, 123, 4.56, True, [], (), {}])
def test_trim_raises_type_error(input_str):
    with pytest.raises(TypeError):
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


@pytest.mark.xfail(strict=True,
                   reason="BR-5: Вместо TypeError летит AttributeError")
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    (None, 'a'),
    (123,  'a'),
    (4.56, 'a'),
    (True, 'a'),
    ({},   'a'),
])
def test_contains_type_error(input_str, input_symbol):
    with pytest.raises(TypeError):
        string_utils.contains(input_str, input_symbol)


@pytest.mark.xfail(strict=True,
                   reason="BR-6: вместо TypeError функция отрабатывает")
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ([], 'a'),
    (['a'], 'a'),
    ((), 'a'),
    (('a', 'b'), 'a'),
])
def test_contains_raises_type_error(input_str, input_symbol):
    with pytest.raises(TypeError):
        string_utils.contains(input_str, input_symbol)


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


@pytest.mark.xfail(strict=True,
                   reason="BR-7: Вместо TypeError летит AttributeError")
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
def test_delete_symbol_type_error(input_str, input_symbol):
    with pytest.raises(TypeError):
        string_utils.delete_symbol(input_str, input_symbol)


@pytest.mark.xfail(strict=True, reason="BR-8: возвращается не str")
@pytest.mark.negative
@pytest.mark.parametrize("input_str, input_symbol", [
    ([], 'a'),
    ((), 'a')
])
def test_delete_symbol_returns_str(input_str, input_symbol):
    assert isinstance(string_utils.delete_symbol(input_str, input_symbol), str)


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
