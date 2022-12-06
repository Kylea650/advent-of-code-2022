def parse_file(file: str) -> str:

    with open(file) as f:
        input = f.readline()

    return input


def get_marker(datastream: str) -> int:
    """
    Iterates though datastream in groups of 4 with two pointers.
    Checks if the current substring is unique with each iteration.

    Returns: first character after which a unique string is found
    """

    def check_unique(substring: str) -> bool:
        return len(set(list(substring))) == len(list(substring))

    l, r = 0, 14

    for i in range(len(datastream) - 4):

        if check_unique(datastream[l:r]):
            return r
        else:
            l += 1
            r += 1
    return -1


def main() -> int:
    file = "day6.txt"
    datastream = parse_file(file)
    char = get_marker(datastream)
    return char


if __name__ == "__main__":
    print(main())
