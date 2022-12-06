def get_crates(file: str) -> list[list[str]]:
    """
    Parses the text input and converts the crate rows into columns

    Returns: lists of crate stacks
    """
    with open(file) as f:
        lines = f.readlines()

        # replaces empty crate spaces to "0" and removes numbering
        str_crates = []
        for line in lines:
            if line == "\n":
                break
            else:
                str_crates.append(
                    line.strip("\n")
                    .replace("    ", "0")
                    .replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                )
        str_crates.pop()

        # converts crate strings to 2D array
        crates = [list(crate) for crate in str_crates]
        # rotates the crate array so each list is now a crate column
        rotated = [list(crate) for crate in (zip(*crates[::-1]))]

        # iterates through the rotated array and removes ending "0"
        for i in range(len(rotated)):
            while rotated[i][-1] == "0":
                rotated[i].pop()

    return rotated


def get_instructions(file: str) -> list[list[int]]:
    """
    Parses the text input to recieve the instructions
    [[number of crates to move, source column, target column],
     [number of crates to move, source column, target column]]

    Returns: lists of instructions
    """
    with open(file) as f:
        lines = f.readlines()

        instructions_str = []
        for line in lines[::-1]:
            if line == "\n":
                break
            else:
                instructions_str.append(
                    line.strip("\n")
                    .replace("move ", "")
                    .replace(" from ", ",")
                    .replace(" to ", ",")
                )
        instructions = [
            list(map(int, instruction.split(","))) for instruction in instructions_str
        ][::-1]

    return instructions


def move_crates(
    crates: list[list[str]], instructions: list[list[int]]
) -> list[list[str]]:
    """
    Iterates through the instructions list and adds the correct number of crates
    from the source stack to the target stack

    Returns: list of crate stacks after transformation
    """
    for instruction in instructions:
        amount = instruction[0]
        source = instruction[1] - 1
        target = instruction[2] - 1
        
        num_crates = amount
        for i in range(amount):
            crates[target].append(crates[source][-num_crates])
            num_crates -= 1
        
        for i in range(amount):
            crates[source].pop()

    return crates


def get_top_crates(crates: list[list[str]]) -> str:
    """
    Adds the top crate letter in each column to a final message
    Returns: string message
    """
    message = ""
    for stack in crates:
        if stack:
            message += stack[-1]

    return message


def main():
    file = "day5.txt"
    crates = get_crates(file)
    instructions = get_instructions(file)
    moved_crates = move_crates(crates, instructions)
    top_crates = get_top_crates(moved_crates)

    return top_crates


if __name__ == "__main__":
    print(main())
