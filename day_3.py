import re

REGEX_PATTERN_FOR_NUMBERS = r"\d+"


class EngineSemantics:
    lines = None
    LOOKUP_DICT_IS_A_SYMBOL = {}

    def load_data(self):
        with open("input/day_3.txt", "r") as txt_file:
            self.lines = [line.strip() for line in txt_file.readlines()]

    def is_field_a_symbol(self, x: int, y: int) -> bool:
        try:
            return self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)]
        except KeyError:
            try:
                self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)] = (
                    False if self.lines[x][y] == "." else True
                )
                return self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)]
            except IndexError:
                # Handle this better maybe?
                return False

    def process_data(self):
        _regex = re.compile(REGEX_PATTERN_FOR_NUMBERS)

        TOTAL_SUM = 0
        for line_idx, line in enumerate(self.lines):
            # Try to use regex to find the numbers.
            # We can use the regex to find the numbers and then we can use the index to find the numbers.
            matches_iterable = _regex.finditer(line)
            for match in matches_iterable:
                # Now we have the y for the match.
                match_y_start, match_y_end = match.start(), match.end() - 1
                # We have to check the following:
                print("Match: ", match.group(), match_y_start, match_y_end)
                skip_this_match_group = False
                # For the start one and the end one, you have to look at left
                for _y in range(match_y_start, match_y_end + 1):
                    if skip_this_match_group:
                        break

                    # This can be made better by using a set or some sort.
                    for coo_ords in [
                        (line_idx, _y + 1),
                        (line_idx, _y - 1),
                        (line_idx + 1, _y),
                        (line_idx + 1, _y + 1),
                        (line_idx + 1, _y - 1),
                        (line_idx - 1, _y),
                        (line_idx - 1, _y + 1),
                        (line_idx - 1, _y - 1),
                    ]:
                        if any(i < 0 for i in coo_ords):
                            continue

                        if (
                            coo_ords[0] == line_idx
                            and match_y_start <= coo_ords[1] <= match_y_end
                        ):
                            continue

                        if self.is_field_a_symbol(*coo_ords):
                            # okey, then we have to add this number to the sum.
                            TOTAL_SUM += int(match.group())
                            # Now can skip this one.
                            skip_this_match_group = True
                            break

        return TOTAL_SUM


engine_semantics = EngineSemantics()
engine_semantics.load_data()
print(engine_semantics.process_data())
