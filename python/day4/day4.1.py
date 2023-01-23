def parse_file(file: str) -> list[list[list[str]]]:
    """
    Opens the file, removes newlines and removes the dashes
    
    Returns: a list containing the elf pairs sections as strings
    """
    with open(file) as f:
        pairs_with_dash = [pair.strip("\n").split(",") for pair in f.readlines()]

        pairs_clean = []
        for pairs in pairs_with_dash:
            pairs_clean.append([pair.split("-") for pair in pairs])

        return pairs_clean


def fully_contains(pairs: list[list[list[str]]]) -> int:
    """
    Initiates a list containing False for each elf pair
    Checks the section start and end points for each pair to see if 
    one contains the other and updates the list to True for that index

    Returns: the count of instances of True
    """

    contains_list = [False] * len(pairs)

    for i in range(len(pairs)):
        if (
            int(pairs[i][0][0]) <= int(pairs[i][1][0])
            and int(pairs[i][0][1]) >= int(pairs[i][1][1])
        ) or (
            int(pairs[i][0][0]) >= int(pairs[i][1][0])
            and int(pairs[i][0][1]) <= int(pairs[i][1][1])
        ):
            contains_list[i] = True

    true_count = contains_list.count(True)

    return true_count


def main():

    file = "day4.txt"
    pairs = parse_file(file=file)
    true_count = fully_contains(pairs=pairs)

    return true_count


if __name__ == "__main__":
    print(main())
