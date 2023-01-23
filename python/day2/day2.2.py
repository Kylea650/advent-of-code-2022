def parse_file(file) -> list[list[str]]:
    
    with open(file) as f:
        lines = f.readlines()

    # removes newline chars and converts each 'round' to a list of values
    rounds = [line.rstrip("\n").split(" ") for line in lines]

    return rounds


def get_response_score(round: list[str]) -> int:
    #  again, probably a better way of mapping this...
    score_map = {"A": 1, "B": 2, "C": 3}

    # lose
    if round[1] == "X":
        if round[0] == "A":
            response = "C"
        if round[0] == "B":
            response = "A"
        if round[0] == "C":
            response = "B"

    # draw
    if round[1] == "Y":
        response = round[0]

    # win
    if round[1] == "Z":
        if round[0] == "A":
            response = "B"
        if round[0] == "B":
            response = "C"
        if round[0] == "C":
            response = "A"

    score = score_map[response]
    return score


def get_score(rounds: list[list]) -> int:

    score_map = {"X": 0, "Y": 3, "Z": 6}
    total_score = 0

    for round in rounds:
        total_score += score_map[round[1]] + get_response_score(round)
    
    return total_score


def main() -> int:

    rounds = parse_file("day2.txt")
    total_score = get_score(rounds)

    return total_score


if __name__ == "__main__":
    print(main())
