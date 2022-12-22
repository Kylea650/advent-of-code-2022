def parse_input(file: str) -> list[str]:

    with open(file) as f:
        motions = [x.strip("\n") for x in f.readlines()]
    return motions


def not_touching(head_row: int, head_col: int, tail_row: int, tail_col: int) -> bool:

    if abs(head_row - tail_row) > 1 or abs(head_col - tail_col) > 1:
        return True
    return False


def main() -> int:

    motions = parse_input("day9.txt")

    head = (0, 0)
    tail = (0, 0)
    visited = set()
    visited.add(tail)

    for motion in motions:
        direction, steps = motion[0], int(motion[2:])

        for _ in range(steps):
            if direction == "L":
                head = (head[0] - 1, head[1])
                if not_touching(head[0], head[1], tail[0], tail[1]):
                    tail = (tail[0] - 1, head[1])
                    visited.add(tail)

            if direction == "R":
                head = (head[0] + 1, head[1])
                if not_touching(head[0], head[1], tail[0], tail[1]):
                    tail = (tail[0] + 1, head[1])
                    visited.add(tail)

            if direction == "U":
                head = (head[0], head[1] + 1)
                if not_touching(head[0], head[1], tail[0], tail[1]):
                    tail = (head[0], tail[1] + 1)
                    visited.add(tail)

            if direction == "D":
                head = (head[0], head[1] - 1)
                if not_touching(head[0], head[1], tail[0], tail[1]):
                    tail = (head[0], tail[1] - 1)
                    visited.add(tail)

    total = len(visited)
    return total


if __name__ == "__main__":
    print(main())
