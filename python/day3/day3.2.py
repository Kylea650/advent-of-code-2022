def parse_file(file) -> list[str]:
    """
    opens text file and returns list of rucksack items as strings
    """
    with open(file) as f:
        rucksacks = [
            rucksack.rstrip("\n").split("\n\n")[0] for rucksack in f.readlines()
        ]

        return rucksacks


def get_rucksack_groups(rucksacks: list[str]) -> list[dict[int:str]]:
    """
    splits all rucksacks into groups of three:
    {1: rucksack 1, 2: rucksack 2, 3: rucksack 3}, {1: rucksack 4, ...}
    returns a list of rucksack group dictionaries
    """
    groups = []
    for i in range(0, len(rucksacks) - 2, 3):
        groups.append({1: rucksacks[i], 2: rucksacks[i + 1], 3: rucksacks[i + 2]})

    return groups


def get_common_letters(rucksacks_compartments: list[dict[int:str]]) -> list[str]:
    """
    converts each compartment to a set and checks the intersection
    to find the common letter
    returns a list of the common letters for all rucksacks
    """
    common = []
    for rucksack in rucksacks_compartments:
        common.append(
            (
                "".join(
                    set(rucksack[1]).intersection(
                        set(rucksack[2]).intersection(set(rucksack[3]))
                    )
                )
            )
        )

    return common


def get_sum_priorities(common_letters: list[str]):
    """
    uses the python ord function to convert each letter to a unicode value
    then maps this to its priority (1-52 for a-zA-Z respectively)
    returns total count of priorities
    """
    count = 0

    for common_letter in common_letters:
        if common_letter.islower():
            count += ord(common_letter) - 96

        if common_letter.isupper():
            count += ord(common_letter) - 38

    return count


def main() -> int:

    rucksacks = parse_file("day3.txt")
    rucksack_groups = get_rucksack_groups(rucksacks)
    common_letters = get_common_letters(rucksack_groups)
    total = get_sum_priorities(common_letters)

    return total


if __name__ == "__main__":
    print(main())
