def parse_file(file) -> list[str]:
    """
    opens text file and returns list of rucksack items as strings
    """
    with open(file) as f:
        rucksacks = [
            rucksack.rstrip("\n").split("\n\n")[0] for rucksack in f.readlines()
        ]

        return rucksacks


def get_rucksack_compartments(rucksacks: list[str]) -> list[dict[int:str]]:
    """
    splits each rucksack into a dictionary in the form:
    {1: first compartment, 2: second compartment}
    returns a list of rucksack dictionaries
    """
    compartments = []
    for rucksack in rucksacks:
        l = int(len(rucksack) / 2)
        compartments.append({1: rucksack[:l], 2: rucksack[l:]})

    return compartments


def get_common_letters(rucksacks_compartments: list[dict[int:str]]) -> list[str]:
    """
    converts each compartment to a set and checks the intersection
    to find the common letter between each
    returns a list of the common letters for all rucksacks
    """
    common = []
    for rucksack in rucksacks_compartments:
        common.append(("".join(set(rucksack[1]).intersection(set(rucksack[2])))))

    return common


def get_sum_priorities(common_letters: list[str]):
    """
    uses the ord function to convert each letter to a unicode value
    then maps this value to its priority (1-52 for a-zA-Z respectively)
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
    rucksacks_compartments = get_rucksack_compartments(rucksacks)
    common_letters = get_common_letters(rucksacks_compartments)
    total = get_sum_priorities(common_letters)

    return total


if __name__ == "__main__":
    print(main())
