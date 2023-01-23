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

    running_total[1] = 1

    for i, v in enumerate(instructions):

        if v[:4] == "addx":
            counter += int(v[5:])

        running_total[i + 2] = counter

    return running_total


def main() -> int:
    instructions = parse_input("day10.txt")
    running_totals = get_running_totals(instructions)

    screen = ["."] * 240
    lines = []

    for pixel in range(len(screen)):

        sprite_start = running_totals[pixel + 1] - 1
        sprite_end = running_totals[pixel + 1] + 1

        if 0 <= pixel < 40:
            if sprite_start <= pixel <= sprite_end:
                screen[pixel] = "#"

        if 40 <= pixel < 80:
            if sprite_start <= (pixel - 40) <= sprite_end:
                screen[pixel] = "#"

        if 80 <= pixel < 120:
            if sprite_start <= (pixel - 80) <= sprite_end:
                screen[pixel] = "#"

        if 120 <= pixel < 160:
            if sprite_start <= (pixel - 120) <= sprite_end:
                screen[pixel] = "#"

        if 160 <= pixel < 200:
            if sprite_start <= (pixel - 160) <= sprite_end:
                screen[pixel] = "#"

        if 200 <= pixel < 240:
            if sprite_start <= (pixel - 200) <= sprite_end:
                screen[pixel] = "#"

    lines.append(screen[:40])
    lines.append(screen[40:80])
    lines.append(screen[80:120])
    lines.append(screen[120:160])
    lines.append(screen[160:200])
    lines.append(screen[200:240])

    return lines


if __name__ == "__main__":
    for line in main():
        print(line)
