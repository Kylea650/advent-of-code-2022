def parse_file(file) -> list[list[str]]:
    
    with open(file) as f:
        lines = f.readlines()

    # removes newline chars and converts each 'round' to a list of values
    rounds = [line.rstrip("\n").split(" ") for line in lines]

    return rounds


def round_outcome(round: list[str]) -> int:
    # I'm sure there's a more elegent way of doing this...
    if round[0] == "A":
        if round[1] == "X":
            score = 3 # draw
        if round[1] == "Y":
            score = 6 # win
        if round[1] == "Z":
            score = 0 # loss

    if round[0] == "B":
        if round[1] == "X":
            score = 0
        if round[1] == "Y":
            score = 3
        if round[1] == "Z":
            score = 6

    if round[0] == "C":
        if round[1] == "X":
            score = 6
        if round[1] == "Y":
            score = 0
        if round[1] == "Z":
            score = 3

    return score


def get_score(rounds: list[list]) -> int:

    score_map = {"X": 1, "Y": 2, "Z": 3}
    total_score = 0

    for round in rounds:
        total_score += score_map[round[1]] + round_outcome(round)

    return total_score


def main() -> int:

    rounds = parse_file("day2.txt")
    total_score = get_score(rounds)

    return total_score


if __name__ == "__main__":
    print(main())
