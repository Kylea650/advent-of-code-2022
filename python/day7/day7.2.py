def parse_file(file: str) -> list[str]:
    """
    Parses the input file into a list, removing "$"'s. The list comprehension produces
    a list of lists so we use map(list, zip(*[[...]])) to flatten it to a single list

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


def get_min_dir_size(dir_sizes: dict[str:int]) -> int:
    """
    Uses the given TOTAL_DISK_SPACE and UPDATE_SIZE to find the minimum directory
    size that should be deleted to free enough space.

    Returns: The minimum size of the directory to be deleted.
    """
    TOTAL_DISK_SPACE = 70000000
    UPDATE_SIZE = 30000000

    free_space = TOTAL_DISK_SPACE - dir_sizes["/"]
    min_dir_size = UPDATE_SIZE - free_space

    return min_dir_size


def get_dir_to_delete(dir_sizes: dict[str:int], min_size: int) -> int:
    """
    Sorts the dir dictionary based on the size of the values asc (e.g the total size of
    that directory). Iterates through the sorted directory and stops when it finds the
    first directory that is at least the minimum size of the directory to be deleted/

    Returns: The size of the directory to be deleted
    """
    sorted_dirs = dict(sorted(dir_sizes.items(), key=lambda x: x[1]))

    for dir_size in sorted_dirs.values():
        if dir_size >= min_size:
            return dir_size
        else:
            continue

    return dir_size


def main() -> int:
    file = "day7.txt"
    commands = parse_file(file=file)
    dir_sizes = get_dir_sizes(commands=commands)
    min_size = get_min_dir_size(dir_sizes)
    dir_to_delete = get_dir_to_delete(dir_sizes, min_size)

    return dir_to_delete


if __name__ == "__main__":
    print(main())
