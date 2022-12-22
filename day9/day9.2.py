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

    knots = [(0, 0) for _ in range(10)]

    visited = set()
    visited.add(knots[-1])

    for motion in motions:
        direction, steps = motion[0], int(motion[2:])

        for _ in range(steps):

            if direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])

            if direction == "R":
                knots[0] = (knots[0][0] + 1, knots[0][1])

            if direction == "U":
                knots[0] = (knots[0][0], knots[0][1] + 1)

            if direction == "D":
                knots[0] = (knots[0][0], knots[0][1] - 1)

            for i in range(len(knots) - 1):

                if not_touching(knots[i][0], knots[i][1], knots[i + 1][0], knots[i + 1][1]):
                    row_diff = knots[i][0] - knots[i + 1][0]
                    col_diff = knots[i][1] - knots[i + 1][1]

                    if row_diff == 0:
                        row = 0
                    elif row_diff < 0:
                        row = -1
                    else:
                        row = 1
                    
                    if col_diff == 0:
                        col = 0
                    elif col_diff < 0:
                        col = -1
                    else:
                        col = 1

                    knots[i + 1] = (knots[i + 1][0] + row, knots[i + 1][1] + col)
                visited.add(knots[-1])

    total = len(visited)
    return total


if __name__ == "__main__":
    print(main())
