from RegexGenerator.generateRegex import generateRegex
from RegexGenerator.generateRegex import generateRegex


def test_generate_regex_pattern():
    g = generateRegex("abc", "100")
    assert g.string == "abc"


def test_generate_regex_pattern():
    g = generateRegex("abc", "100")
    assert g.negative_string == "100"


def test_generate_regex_pattern():
    g = generateRegex("abc", "100")
    assert g.symbol_map["#"] == 0.015819750719079578


def test_generate_regex_pattern():
    g = generateRegex("abc", "100")
    assert g.generate_regex_pattern() == [[3, "\\[q"]]


def test_generate_regex_pattern():
    g = generateRegex("abc", "100")
    g.generate_regex_from_string()
    g.found_patterns = []


# self.max_patterns = 5
# self.max_tries = 1000
# self.found_patterns = set()
# self.pattern_size: int = 3
# self.unique_patterns: int = 1
# self.symbol_map = uf.create_probability_object(uf)
