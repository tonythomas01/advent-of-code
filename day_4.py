def find_total_winning_points() -> int:
    total_sum = 0
    with open("input/day_4.txt", "r") as file:
        for line in file:
            line_total = 0
            line = line.split(": ")[1].strip()
            # Now, we want to split by ("|")
            winning_numbers_part, cards_owned_part = line.split(" | ")
            # Remove '' from both lists
            winning_numbers = list(map(int, winning_numbers_part.split()))
            cards_owned = list(map(int, cards_owned_part.split()))

            # print(f"Winning numbers: {winning_numbers}")
            # print(f"Cards owned: {cards_owned}")

            common_elements = len(set(winning_numbers) & set(cards_owned))
            if common_elements == 0:
                continue

            line_total = 2 ** (common_elements - 1) if common_elements > 0 else 0
            total_sum += line_total

    return total_sum


if __name__ == "__main__":
    print(find_total_winning_points())
