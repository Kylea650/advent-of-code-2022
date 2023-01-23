def parse_input(file: str) -> list[list[int]]:
    """
    Returns: a 2D array of integers (tree heights)
    """
    with open(file) as f:
        rows = [x.strip() for x in f.readlines()]
        str_matrix = list(map(list, rows))
        matrix = [list(map(int, i)) for i in str_matrix]

        return matrix


def can_be_seen(matrix: list[list[int]], row: int, col: int) -> bool:
    """
    Iterates through the 2D array and checks if there are any trees to the left, right
    above or below with the same heigh value. If a tree with the same height or greater
    is found, that directrion is set to False. If any of the directions remains True,
    the tree can be seen.

    Returns: True or False
    """
    value = matrix[row][col]

    left, right, up, down = True, True, True, True
    can_be_seen = False

    # If the value is in the first or last row, or first or last column, it can be seen
    if (col == 0 or col == len(matrix[row]) - 1) or (
        row == 0 or row == len(matrix) - 1
    ):
        can_be_seen = True

    # checking left
    for i in range(0, len(matrix[row][:col])):
        if matrix[row][i] >= value:
            left = False
        else:
            continue

    # checking right
    for i in range(col + 1, len(matrix[row])):
        if matrix[row][i] >= value:
            right = False
        else:
            continue

    # checking up
    for i in range(0, len(matrix[:row])):
        if matrix[i][col] >= value:
            up = False
        else:
            continue

    # checking down
    for i in range(row + 1, len(matrix)):
        if matrix[i][col] >= value:
            down = False
        else:
            continue

    # if the tree can be seen from any direction, return True
    if left or right or up or down:
        can_be_seen = True

    return can_be_seen


def main() -> int:
    """
    Iterates through the 2D array and checks if a given tree can be seen.
    If True (the tree can be seen), the count is increased by 1.

    Returns: Count of visible trees
    """
    file = "day8.txt"
    tree_matrix = parse_input(file)

    count = 0

    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[i])):

            if can_be_seen(tree_matrix, i, j):
                count += 1

    return count


if __name__ == "__main__":
    print(main())
