import re
import typing


class EngineSemantics:
    lines = None
    LOOKUP_DICT_IS_A_SYMBOL = {}
    LOOKUP_DICT_IS_A_NUMBER = {}
    SHOULD_GET_MULTIPLIED_WITH_TRACKER = {}
    SUM_OF_PRODUCTS = 0

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

    def is_field_a_symbol_and_matched_by_star(
        self, x: int, y: int
    ) -> typing.Tuple[bool, bool]:
        try:
            return self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)]
        except KeyError:
            try:
                if self.lines[x][y] == ".":
                    self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)] = (False, False)
                else:
                    self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)] = (
                        True,
                        self.lines[x][y] == "*",
                    )

                return self.LOOKUP_DICT_IS_A_SYMBOL[(x, y)]
            except IndexError:
                # Handle this better maybe?
                return False, False

    def is_field_a_number(self, x: int, y: int) -> bool:
        try:
            return self.LOOKUP_DICT_IS_A_NUMBER[(x, y)]
        except KeyError:
            try:
                self.LOOKUP_DICT_IS_A_NUMBER[(x, y)] = self.lines[x][y].isdecimal()
                return self.LOOKUP_DICT_IS_A_NUMBER[(x, y)]
            except IndexError:
                # Handle this better maybe?
                return False

    def process_data_part_1(self):
        REGEX_PATTERN_FOR_NUMBERS = r"\d+"
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

    def is_and_loc_of_another_part_number_nearby(
        self,
        x: int,
        y: int,
        matched_group_x,
        matched_group_y_start,
        matched_group_y_end,
    ):
        # So there is a star at x, y. We need to see if there is an another number nearby.
        for coo_ords in [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x - 1, y - 1),
        ]:
            # Some of them we have to skip, as this would be the matched group.
            if (
                coo_ords[0] == matched_group_x
                and matched_group_y_start <= coo_ords[1] <= matched_group_y_end
            ):
                continue

            if any(i < 0 for i in coo_ords):
                continue

            if self.is_field_a_number(*coo_ords):
                # okey, then we have to add this number to the sum.
                # We better get the number as well.
                return True, coo_ords

        return False, None

    def process_data_part_2(self):
        REGEX_PATTERN_FOR_NUMBERS = r"\d+"
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

                        (
                            is_a_symbol,
                            is_matched_by_star,
                        ) = self.is_field_a_symbol_and_matched_by_star(*coo_ords)
                        # okey, then we have to add this number to the sum.
                        if is_a_symbol:
                            # We need to check if there are some part numbers nearby.
                            if not is_matched_by_star:
                                continue

                            (
                                is_there_a_number_nearby,
                                number_cords,
                            ) = self.is_and_loc_of_another_part_number_nearby(
                                *coo_ords,
                                matched_group_x=line_idx,
                                matched_group_y_start=match_y_start,
                                matched_group_y_end=match_y_end,
                            )
                            if not is_there_a_number_nearby:
                                continue

                            self._check_and_add_to_multiply_list(
                                line_idx=line_idx,
                                match=match,
                                number_cords=number_cords,
                            )
                            # Now can skip this one.
                            skip_this_match_group = True
                            break

        # Now we have to go through the values and try to get them.
        return self.SUM_OF_PRODUCTS

    def _check_and_add_to_multiply_list(self, line_idx, match, number_cords):
        # Sometimes the number coords can be already here somewhere
        for key, value in self.SHOULD_GET_MULTIPLIED_WITH_TRACKER.items():
            current_check_cords_x = value["part_number_two_coo_ords_include"][0]
            if current_check_cords_x == line_idx:
                current_check_cords_y = value["part_number_two_coo_ords_include"][1]
                if match.start() <= current_check_cords_y <= match.end() - 1:
                    # This is already here
                    self.SHOULD_GET_MULTIPLIED_WITH_TRACKER[key].update(
                        {
                            "part_number_two": int(match.group()),
                        }
                    )
                    self.SUM_OF_PRODUCTS += (
                        int(match.group()) * value["part_number_one"]
                    )
                    return

        self.SHOULD_GET_MULTIPLIED_WITH_TRACKER[
            f"{number_cords[0]}_{number_cords[1]}"
        ] = {
            "part_number_one": int(match.group()),
            "part_number_two": None,
            "part_number_two_coo_ords_include": number_cords,
        }


engine_semantics = EngineSemantics()
engine_semantics.load_data()
# print(engine_semantics.process_data_part_1())
print(engine_semantics.process_data_part_2())
