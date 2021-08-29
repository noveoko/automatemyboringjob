import re


class UpdateFrequencies:

    all_symbols = {
        ".": 0,
        "^": 0,
        "$": 0,
        "*": 0,
        "+": 0,
        "?": 0,
        "{": 0,
        "}": 0,
        "[": 0,
        "]": 0,
        "\\": 0,
        "|": 0,
        "(": 0,
        ")": 0,
        "\d": 0,
        "\D": 0,
        "\s": 0,
        "\S": 0,
        "\w": 0,
        "\W": 0,
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
        " ": 0,
        ":0,": 0,
        "'": 0,
        "!": 0,
        "@": 0,
        "#": 0,
        "$": 0,
        "%": 0,
        "^": 0,
        "&": 0,
        "*": 0,
        "(": 0,
        ")": 0,
        "_": 0,
        "+": 0,
        "}": 0,
        "{": 0,
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
    }

    total_symbols = 0

    prob_dict = {}

    def update_frequencies(self):

        errors = set()
        with open("patterns_in_the_wild.txt", "r", encoding="utf-8") as infile:
            for line in infile.readlines():
                line_x = line
                for symbol in self.all_symbols.keys():
                    if symbol.isalpha():
                        symbol = symbol.lower()
                    try:
                        if symbol in line_x:
                            # count occurances
                            self.all_symbols[symbol] += line_x.count(symbol)
                            # remvoe occurances
                            line_x = re.sub(symbol, "", line_x)
                            self.total_symbols += 1
                    except Exception as ee:
                        errors.add(ee)

    def create_probability_object(self):
        self.update_frequencies()
        prob_dict = {}
        for symbol in self.all_symbols.keys():
            prob_dict[symbol] = self.all_symbols[symbol] / self.total_symbols
        print(prob_dict)
        self.prob_dict = prob_dict


if __name__ == "__main__":
    pass
