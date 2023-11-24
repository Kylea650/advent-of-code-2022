from collections import deque

def parse_input(file: str) -> list[list[str]]:
    # return 2D matrix of heights
    with open(file) as f:
        height_matrix = [list(x) for x in [y.strip() for y in f.readlines()]]
    return height_matrix


def find_S_and_E(height_matrix: list[list[str]]) -> (tuple[int, int], tuple[int, int]):
    # iterate over matrix and return the coordinates of the start point S and end point E
    for i in range(len(height_matrix)):
        for j in range(len(height_matrix[i])):

            if height_matrix[i][j] == "S":
                S = (i, j)

            if height_matrix[i][j] == 'E':
                E = (i, j)
    return (S, E)


def find_all_starts(height_matrix: list[list[str]]) -> list[tuple[int, int]]:
    # find all potential start points (S or a)
    starts = []

    for i in range(len(height_matrix)):
        for j in range(len(height_matrix[i])):

            match height_matrix[i][j]:
                case 'S':
                    starts.append((i, j))
                case 'a':
                    starts.append((i, j))
                case _:
                    continue
    return starts


def can_move_to(height_matrix:list[list[str]], cur_row: int, cur_col: int, new_row: int, new_col: int):
    # if new row or column value goes out of bounds
    if (new_row < 0 or new_col < 0 or new_row >= len(height_matrix) or new_col >= len(height_matrix[0])):
        return False

    # convert letter at current position to ordinal value. Give S and E the value of a and z respectively
    match height_matrix[cur_row][cur_col]:
        case 'S':
            current_height = 1
        case 'E':
            current_height = 26
        case _:
            current_height = ord(height_matrix[cur_row][cur_col]) - 96
    
    # convert letter at new position to ordinal value. Give S and E the value of a and z respectively
    match height_matrix[new_row][new_col]:
        case 'S':
            new_height = 1
        case 'E':
            new_height = 26
        case _:
            new_height = ord(height_matrix[new_row][new_col]) - 96

    # check if the difference between current and new is greater than 1
    if new_height > current_height + 1:
        return False

    return True


def traverse(height_matrix: list[list[str]], start: tuple[int, int], end: tuple[int, int]):

    # initialise set for all visited coordinates
    visited = set()

    # initialise queue and add start point
    queue = deque()
    queue.append([start])

    # BFS algorithm
    while queue:
        path = queue.popleft()

        # current point is the last point in our current path
        cur_row, cur_col = path[-1]

        # if we haven't been to this coordinate yet, add it to our set
        if (cur_row, cur_col) not in visited:
            visited.add((cur_row, cur_col))

            # we've made it to E, return the length of the current path
            if (cur_row, cur_col) == end:
                return len(path) - 1

            # check all surrounding points. If we can move to it, add it to our queue
            for new_row, new_col in ((cur_row + 1, cur_col), (cur_row - 1, cur_col), (cur_row, cur_col + 1), (cur_row, cur_col - 1)):
                if can_move_to(height_matrix, cur_row, cur_col, new_row, new_col):
                    queue.append(path + [(new_row, new_col)])


def main():
    file = "day12.txt"
    height_matrix = parse_input(file)

    start_part_one, end = find_S_and_E(height_matrix)
    part_one = traverse(height_matrix, start_part_one, end)

    all_path_lengths = []
    for start_part_two in find_all_starts(height_matrix):
        path_length = traverse(height_matrix, start_part_two, end)

        # not None
        if path_length:
            all_path_lengths.append(path_length)
    
    part_two = min(all_path_lengths)

    print(f"part 1: {part_one}")
    print(f"part 2: {part_two}")


if __name__ == "__main__":
    main()