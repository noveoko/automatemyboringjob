import random
import re
from typing import List,Set,Tuple

metacharacters = [".","^","$","*","+","?","{","}","[","]","\\","|" "(", ")"]

patterns = ["\d","\D","\s","\S","\w","\W"]

characters = "abcdefghijklmnopqrstuvwxyz ,'!@#$%^&*()_+}{"

numbers = "0123456789"

all_symbols = characters+numbers

prob = [0.1, 0.2, 0.35, 0.35]

def generateRegExPattern(pattern_size:int=3, unique_patterns:int=1)->List[str]:
    all_patterns:List = []
    while len(all_patterns) < unique_patterns:
        pattern = r""
        while len(pattern) < pattern_size:
            choice = random.choices([metacharacters, patterns, characters, numbers], prob, k=1)
            random_symbol = random.choice(choice[0])
            pattern += random_symbol
        all_patterns.append([pattern_size, pattern])
    return all_patterns

def generateFromRegex(pattern:str, max_symbols:int=10, max_tries:int=100000)->List:
    matching_string:Set[str] = set()
    failed_matches = 0
    tries = 0
    while not matching_string and tries < max_tries:
        symbols_count = random.choice(range(1, max_symbols))
        string = ""
        while len(string) < symbols_count:
            string_choice = random.choice(all_symbols)
            string += string_choice
        if re.match(pattern, string):
            matching_string.add(string)
        else:
            failed_matches+=1
            print(f"Searching for: {pattern} {failed_matches}", end="\r")
        tries +=1
    return [matching_string, pattern, failed_matches]

def generateRegExFromString(string)->Tuple[str, str]:
    good_pattern = None
    while not good_pattern:
        try:
            new_pattern = generateRegExPattern(unique_patterns=100)
            for pattern in new_pattern:
                pattern = pattern[1]
                if re.match(pattern, string):
                    good_pattern = pattern
                    break
        except Exception as ee:
            print(ee)
    return (good_pattern, string)



myregex = generateRegExFromString("9999")

print(myregex)