patterns = set()

with open("scratchpad.txt", "r", encoding="utf-8") as infile:
    for line in infile.readlines():
        if "re.compile" in line:
            line = line.split("re.compile")[-1]
            patterns.add(line)

with open("scratchpad.txt", "w", encoding="utf-8") as outfile:
    for pattern in patterns:
        outfile.write(pattern + "\n")
