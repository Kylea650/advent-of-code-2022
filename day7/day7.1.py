def parse_file(file: str) -> list[str]:
    """
    Parses the input file into a list, removing "$"'s. The list comprehension produces
    a list of lists so we use map(list, zip(*[[...]])) to flatten it to a single list.

    Returns: a list of string commands
    """
    with open(file) as f:
        commands = list(
            map(
                list,
                zip(
                    *[
                        line.strip().replace("$ ", "").split("\n")
                        for line in f.readlines()
                    ]
                ),
            )
        )[0]
        return commands


def get_dir_sizes(commands: list[str]) -> dict[str:int]:
    """
    Initialises dictionary and our path list then iterates through the commands.
    Our full filepath for our current directory is formed by concatenating all the
    file paths so far e.g ["/", "a/", "a/e/"]. if we cd into a new directory
    then the new directory + current path is appended to our path list. This filepath
    is added to a dictionary "dir_dict" with value 0. When we reach a file, the size of
    the file is added to the value in the dictionary for EACH directory in our path
    list so that the size is also reflected in all parent directories.

    Returns: dictionary {"full directory filepath": total size}
    """
    dir_dict = {}
    path = ["/"]

    for command in commands:
        current_dir = "".join(path)[1:]

        if command[:2] == "cd":

            if command == "cd /":
                if command not in dir_dict.keys():
                    dir_dict["/"] = 0
                path = ["/"]

            elif command == "cd ..":
                path.pop()

            else:
                dir_name = f"{current_dir}" + f"{command[3:]}/"
                if dir_name not in dir_dict.keys():
                    dir_dict[dir_name] = 0
                path.append(dir_name)

        elif command == "ls":
            continue

        elif command[:3] == "dir":
            continue

        else:
            file_size = int(command.split(" ")[0])
            for dir in path:
                dir_dict[dir] += file_size

    return dir_dict


def get_dir_sums(dir_sizes: dict[str:int], max_size: int) -> int:
    """
    Returns: The sum of any values in the dir dictionary which are below a given size.
    """
    return sum([x for x in dir_sizes.values() if x <= max_size])


def main() -> int:
    file = "day7.txt"
    commands = parse_file(file=file)
    dir_sizes = get_dir_sizes(commands=commands)
    sum_dirs = get_dir_sums(dir_sizes=dir_sizes, max_size=100000)

    return sum_dirs


if __name__ == "__main__":
    print(main())
