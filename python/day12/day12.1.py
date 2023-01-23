def parse_input(file: str) -> list[list[str]]:

    with open(file) as f:
        height_matrix = [list(x) for x in [y.strip() for y in f.readlines()]]
    return height_matrix


def find_S_and_E(
    height_matrix: list[list[str]],
) -> tuple[tuple[int, int], tuple[int, int]]:

    for i in range(len(height_matrix)):
        for j in range(len(height_matrix[i])):

            if height_matrix[i][j] == "S":
                S = (i, j)

            elif height_matrix[i][j] == "E":
                E = (i, j)

    return (S, E)


file = "text.txt"
height_matrix = parse_input(file)
start, end = find_S_and_E(height_matrix)
