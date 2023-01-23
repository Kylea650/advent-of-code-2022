def parse_file(file: str) -> str:

    with open(file) as f:
        input = f.readline()

    return input


def get_marker(datastream: str, window_size: int) -> int:
    """
    Iterates though datastream in groups of 4 with two pointers.
    Checks if the current substring is unique with each iteration.

    Returns: first character after which a unique string is found
    """

    def check_unique(substring: str) -> bool:
        return len(set(list(substring))) == len(list(substring))

    for i in range(len(datastream) - window_size):
        r = i + window_size

        if check_unique(datastream[i:r]):
            return r

    return -1


def main() -> int:
    file = "day6.txt"
    datastream = parse_file(file)
    char = get_marker(datastream, 14)
    return char


if __name__ == "__main__":
    print(main())
