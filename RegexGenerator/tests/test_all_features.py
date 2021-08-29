from RegexGenerator.generateRegex import generateRegex

# import generateRegex class from RegexGenerator.generateRegex
from RegexGenerator.generateRegex import generateRegex


def test_generate_regex_pattern():
    g = generateRegex("abc")
    assert g.generate_regex_pattern() == [[3, "4\\w"]]


def test_generate_from_regex():
    g = generateRegex("abc")
    assert g.generate_from_regex("\d{2}") == [{"71*ze"}, "\\d{2}", 0]


def test_generate_regex_from_string():
    g = generateRegex("abc")
    g.generate_regex_pattern()
    g.found_patterns = []
