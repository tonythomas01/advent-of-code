import csv
import re

STRING_TO_NUMBER = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

REGEX_PATTERN_FOR_NUMBERS = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"


def process_data():
    with open("input/test.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        total_sum = 0
        _regex = re.compile(REGEX_PATTERN_FOR_NUMBERS)
        for row in reader:
            first_int = None
            last_int = None
            input_line = row["input_lines"]

            matches = _regex.findall(input_line)

            for match in matches:
                if match.isdecimal():
                    if not first_int:
                        first_int = match
                    else:
                        last_int = match
                else:
                    if not first_int:
                        first_int = STRING_TO_NUMBER[match]
                    else:
                        last_int = STRING_TO_NUMBER[match]

            if not last_int:
                last_int = first_int

            print(f"Row: {input_line} int is: {first_int}{last_int}")
            total_sum += int(f"{first_int}{last_int}")

        return total_sum


total_sum = process_data()

print(total_sum)
