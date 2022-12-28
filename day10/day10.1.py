def parse_input(file: str) -> list[str]:

    with open(file) as f:
        input = [ins.strip("\n") for ins in f.readlines()]

    instructions = []

    for ins in input:

        if ins == "noop":
            instructions.append(ins)
        else:
            instructions.append("")
            instructions.append(ins)

    return instructions


def get_running_totals(instructions: list[str]) -> dict[int:str]:
    counter = 1
    running_total = {}

    for i, v in enumerate(instructions):

        if v[:4] == "addx":
            counter += int(v[5:])

        running_total[i + 2] = counter

    return running_total


def main() -> int:
    instructions = parse_input("day10.txt")
    running_totals = get_running_totals(instructions)

    signal_strengths = []

    for i, v in running_totals.items():
        if i in (20, 60, 100, 140, 180, 220):
            signal_strengths.append(i * v)

    return sum(signal_strengths)


if __name__ == "__main__":
    print(main())
