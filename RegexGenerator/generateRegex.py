import random
import re
from typing import List, Set, Tuple
import sys
import argparse

from RegexGenerator.utilities.create_symbol_frequency import UpdateFrequencies as uf


class generateRegex:

    """Generate a regex give a string"""

    seed = 0.2323

    def __init__(self, string: str = "abc", negative_string: str = "10"):
        self.string = string
        self.negative_string = negative_string
        self.max_patterns = 5
        self.max_tries = 1000
        self.found_patterns = set()
        self.pattern_size: int = 3
        self.unique_patterns: int = 100
        self.symbol_map = uf.create_probability_object(uf)

    def generate_regex_pattern(self):
        all_patterns = []
        random.seed(self.seed)
        while len(all_patterns) < self.unique_patterns:
            try:
                pattern = r""
                while len(pattern) < self.pattern_size:
                    choice = random.choices(
                        [a for a in self.symbol_map.keys()],
                        [a for a in self.symbol_map.values()],
                        k=1,
                    )
                    random_symbol = random.choice(choice[0])
                    pattern += random_symbol
                all_patterns.append([self.pattern_size, pattern])
            except IndexError as ie:
                print(ie)
        return all_patterns

    def generate_from_regex(
        self, pattern: str, max_symbols: int = 10, max_tries: int = 100000
    ) -> List:
        matching_string: Set[str] = set()
        failed_matches = 0
        tries = 0
        while not matching_string and tries < max_tries:
            try:
                symbols_count = random.choice(range(1, max_symbols))
                string = ""
                while len(string) < symbols_count:
                    print(string)
                    if self.symbol_map:
                        string_choice = random.choice(
                            [a for a in self.symbol_map.keys()]
                        )
                        string += string_choice
                    if re.match(pattern, string):
                        matching_string.add(string)
                        break
                    else:
                        failed_matches += 1
                        print(f"Searching for: {pattern} {failed_matches}", end="\r")
                tries += 1
            except Exception as e:
                print(e)
        else:
            shortest_matching_string = sorted(matching_string, key=len)[0]
            package = [shortest_matching_string, pattern, failed_matches]
            print(f"Done! {package}")
            return package

    def best_pattern(self):
        return sorted(
            [
                a
                for a in list(self.found_patterns)
                if not re.fullmatch(a, self.negative_string)
            ],
            key=lambda x: len(x),
            reverse=True,
        )

    def repeatMaker(max_repeats=5):
        repeats = random.choice(range(max_repeats))
        return f"{repeats}"

    def generate_regex_from_string(self):
        """Generate any regex pattern from a string"""
        tries = 0
        while tries < self.max_tries:
            try:
                tries += 1
                new_pattern = self.generate_regex_pattern()
                for pattern in new_pattern:
                    try:
                        pattern = pattern[1]
                        assert isinstance(self.string, str)
                        if re.match(pattern, self.string):
                            self.found_patterns.add(pattern)
                            print(
                                f"Pattern match found! {pattern} found:{len(self.found_patterns)}",
                                end="\r",
                            )
                    except Exception as ee:
                        pass
            except AssertionError as ae:
                print("2a:", ae)
            except Exception as ee:
                print("2: ", ee)
        if self.negative_string:
            self.found_patterns = self.best_pattern()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Regex/String")
    parser.add_argument(
        "string",
        type=str,
        help="The <string> used to generate the regex pattern",
    )
    parser.add_argument(
        "--negative",
        type=str,
        help="<string> that should not match generated regex pattern",
    )
    args = parser.parse_args()
    generate = generateRegex(args.string)
    if args.negative:
        generate.generate_regex_from_string()
    else:
        generate.generate_regex_pattern()
