def parse_input(file: str) -> list[list[int]]:
    """
    Returns: a 2D array of integers (tree heights)
    """
    with open(file) as f:
        rows = [x.strip() for x in f.readlines()]
        str_matrix = list(map(list, rows))
        matrix = [list(map(int, i)) for i in str_matrix]

        return matrix


def get_scenic_score(matrix: list[list[int]], row: int, col: int) -> int:
    """
    Iterates through the 2D array and counts the number of trees which can be seen in
    each direction. When we reach a tree that is the same height or taller, or reach
    then end of the forest, we stop counting in that direction.

    Returns: Scenic score (left * right * up * down)
    """
    value = matrix[row][col]

    left, right, up, down = 0, 0, 0, 0

    # checking left
    i = col - 1
    while i >= 0:
        if matrix[row][i] >= value:
            left += 1
            break
        else:
            left += 1
        i -= 1

    # checking right
    i = col + 1
    while i < len(matrix[row]):
        if matrix[row][i] >= value:
            right += 1
            break
        else:
            right += 1
        i += 1

    # checking up
    i = row - 1
    while i >= 0:
        if matrix[i][col] >= value:
            up += 1
            break
        else:
            up += 1
        i -= 1

    # checking down
    i = row + 1
    while i < len(matrix):
        if matrix[i][col] >= value:
            down += 1
            break
        else:
            down += 1
        i += 1

    return left * right * up * down


def main() -> int:
    """
    Iterates through the 2D array and checks if a given tree can be seen.
    If True (the tree can be seen), the count is increased by 1.

    Returns: Count of visible trees
    """
    file = "day8.txt"
    tree_matrix = parse_input(file)

    scenic_scores = []

    for i in range(len(tree_matrix)):
        for j in range(len(tree_matrix[i])):
            scenic_scores.append(get_scenic_score(tree_matrix, i, j))

    return max(scenic_scores)


if __name__ == "__main__":
    print(main())
