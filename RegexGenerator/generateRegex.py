import random
import re
from typing import List, Set, Tuple
import sys
import argparse


class RegexGenerator:

    removed = ["."]
    metacharacters = ["^", "$", "*", "+", "?", "{", "}", "[", "]", "\\", "|" "(", ")"]
    patterns = ["\d", "\D", "\s", "\S", "\w", "\W"]
    characters = "abcdefghijklmnopqrstuvwxyz ,'!@#$%^&*()_+}{"
    numbers = "0123456789"
    all_symbols = characters + numbers
    prob = [0.1, 0.2, 0.35, 0.35]

    def __init__(self, string, negative_string=None):
        self.string: str = string
        self.negative_string: str = negative_string
        self.max_patterns = 5
        self.max_tries = 1000
        self.found_patterns = set()
        self.pattern_size: int = 3
        self.unique_patterns: int = 1

    def generateRegExPattern(self) -> List[str]:
        all_patterns: List = []
        while len(all_patterns) < self.unique_patterns:
            pattern = r""
            while len(pattern) < self.pattern_size:
                choice = random.choices(
                    [self.metacharacters, self.patterns, self.characters, self.numbers],
                    self.prob,
                    k=1,
                )
                random_symbol = random.choice(choice[0])
                pattern += random_symbol
            all_patterns.append([self.pattern_size, pattern])
        return all_patterns

    def generateFromRegex(
        self, pattern: str, max_symbols: int = 10, max_tries: int = 100000
    ) -> List:
        matching_string: Set[str] = set()
        failed_matches = 0
        tries = 0
        while not matching_string and tries < max_tries:
            symbols_count = random.choice(range(1, max_symbols))
            string = ""
            while len(string) < symbols_count:
                string_choice = random.choice(self.all_symbols)
                string += string_choice
            if re.match(pattern, string):
                matching_string.add(string)
            else:
                failed_matches += 1
                print(f"Searching for: {pattern} {failed_matches}", end="\r")
            tries += 1
        return [matching_string, pattern, failed_matches]

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

    def generateRegExFromString(self) -> Tuple[str, str]:
        tries = 0
        while len(self.found_patterns) < self.max_patterns and tries < self.max_tries:
            try:
                new_pattern = self.generateRegExPattern(unique_patterns=1000)
                for pattern in new_pattern:
                    pattern = pattern[1]
                    if re.fullmatch(pattern, self.string):
                        self.found_patterns.add(pattern)
                        print(
                            f"Pattern found! {pattern} found:{len(self.found_patterns)}",
                            end="\r",
                        )
            except Exception as ee:
                continue
            finally:
                tries += 1
        else:
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
    generate = RegexGenerator(args.string, args.negative)
    generate.generateRegExFromString()
    print(generate.found_patterns)
