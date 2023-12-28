import csv
import math

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

COLOR_TO_MAX_MAP = {"red": MAX_RED, "green": MAX_GREEN, "blue": MAX_BLUE}


def process_data():
    with open("input/day2.csv", "r") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=";", quotechar="|")
        total_sum = 0
        for row in spamreader:
            game_number_side, rest_of_row_data = row[0].split(":")
            game_number = int(game_number_side.split("Game")[1].strip())
            row[0] = rest_of_row_data
            row_valid = True
            for game_data in row:
                for item in game_data.split(","):
                    color_count, color = item.strip().split(" ")
                    if int(color_count) > COLOR_TO_MAX_MAP[color]:
                        row_valid = False
                        break
                if not row_valid:
                    break

            if row_valid:
                total_sum += game_number

        return total_sum


def process_data_part_two():
    with open("input/day2.csv", "r") as csv_file:
        spamreader = csv.reader(csv_file, delimiter=";", quotechar="|")
        total_sum = 0
        for row in spamreader:
            game_number_side, rest_of_row_data = row[0].split(":")
            row[0] = rest_of_row_data
            row_max_dict = {}
            for game_data in row:
                for item in game_data.split(","):
                    color_count, color = item.strip().split(" ")
                    if color in row_max_dict:
                        if int(color_count) > row_max_dict[color]:
                            row_max_dict[color] = int(color_count)
                    else:
                        row_max_dict[color] = int(color_count)

            total_sum += math.prod(row_max_dict.values())
        return total_sum


total_sum = process_data_part_two()

print(total_sum)
