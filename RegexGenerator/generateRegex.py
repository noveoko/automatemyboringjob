import random
import re
from typing import List, Set
import click

from utilities.create_symbol_frequency import UpdateFrequencies as uf


class generateRegex:

    """Generate a regex give a string"""

    seed = 0.2323

    def __init__(self, string: str = "abc", negative_string: str = "10"):
        self.string = string
        self.negative_string = negative_string
        self.max_patterns = 2
        self.max_tries = 10
        self.found_patterns = set()
        self.tried_patterns = []
        self.pattern_size: int = 10
        self.unique_patterns: int = 10000
        self.symbol_map = uf.create_probability_object(uf)

    def get_random_size(self):
        return random.choice(range(1, 10))

    def symbol_choices(self):
        return random.choices(
            [a for a in self.symbol_map.keys()],
            [a for a in self.symbol_map.values()],
            k=200,
        )

    def generate_regex_pattern(self):
        all_patterns = []
        random.seed(self.seed)
        while len(all_patterns) < self.unique_patterns:
            try:
                pattern = r""
                while len(pattern) < self.get_random_size():
                    choice = self.symbol_choices()
                    random_symbol = choice[0]
                    pattern += random_symbol
                self.tried_patterns.append(pattern)
                all_patterns.append(pattern)
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
                print(symbols_count)
                string = ""
                while len(string) < symbols_count:
                    print(string)
                    if self.symbol_map:
                        string_choice = random.choice(
                            [a for a in self.symbol_map.keys()]
                        )
                        string += string_choice
                    if re.fullmatch(pattern, string):
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
                if tries % 100 == 0:
                    print(f"Tries: {tries}", end="\r")
                patterns_to_try = self.generate_regex_pattern()
                for _, pattern in patterns_to_try:
                    if re.fullmatch(pattern, self.string):
                        self.found_patterns.add(pattern)
                    else:
                        print(f"Doesn't Match! {pattern} -> {self.string}")
            except Exception as e:
                pass
        if self.negative_string:
            self.found_patterns = self.best_pattern()


@click.command()
@click.option("--string", prompt="Input string?", help="Input symbols")
@click.option(
    "--negative",
    prompt="Which string must not match?",
    help="Symbol pattern that shouldn't match",
)
@click.option(
    "--mode",
    prompt="regex (generate pattern) OR string (generate string from pattern)?",
    help="The function to run on your input string",
)
def main(string, negative, mode):
    """Generate regex/string based on input"""

    gen = generateRegex(string, negative)
    result = None
    if mode == "regex":
        # generate regex from string
        gen.generate_regex_from_string()
        result = gen.found_patterns
    elif mode == "string":
        # generate string from regex
        result = gen.generate_from_regex(string)
    if result:
        print(f"OUTPUT:\n\n", result)
    else:
        print("No matches found!")


if __name__ == "__main__":
    main()
