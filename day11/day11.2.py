def parse_input(file: str) -> dict[str:list]:
    monkey_dict = {}

    with open(file) as f:
        text = [x.split("\n") for x in f.read().split("\n\n")]

    for monkey in text:
        values = []
        # starting items
        values.append([int(x.strip(",")) for x in monkey[1][17:].split()])
        # operation
        values.append(monkey[2][23:])
        # test (divisible by)
        values.append(int(monkey[3][21:]))
        # if true, moves to
        values.append(monkey[4][22:])
        # if false, moves to
        values.append(monkey[5][23:])

        monkey_dict[monkey[0][:-1].lower()] = values

    return monkey_dict


def get_new_worry_level(worry_level: int, operation: str) -> int:

    if operation[0] == "+":

        if operation[2:] == "old":
            new_value = worry_level + worry_level
        else:
            new_value = worry_level + int(operation[2:])
        return new_value

    elif operation[0] == "*":

        if operation[2:] == "old":
            new_value = worry_level * worry_level
        else:
            new_value = worry_level * int(operation[2:])
        return new_value


def get_modulo(tests: list[int]) -> int:
    res = 1
    for test in tests:
        res *= test
    return res


def get_num_inspections(monkeys: dict[str:list]) -> dict[str:int]:
    inspect_count_dict = {}
    for k, v in monkeys.items():
        inspect_count_dict[k] = 0

    tests = [monkeys[monkey][2] for monkey in monkeys]
    modulo = get_modulo(tests)

    for _ in range(10_000):

        for k, v in monkeys.items():

            items = v[0]
            operation = v[1]
            test = v[2]
            true_monkey = v[3]
            false_monkey = v[4]

            for i in range(len(items)):
                new_worry_level = get_new_worry_level(items[i], operation)
                new_worry_level %= modulo

                if new_worry_level % test == 0:
                    monkeys[true_monkey][0].append(new_worry_level)

                else:
                    monkeys[false_monkey][0].append(new_worry_level)

            monkeys[k][0] = []
            inspect_count_dict[k] += len(items)

    return inspect_count_dict


def main():
    file = "day11.txt"
    monkeys = parse_input(file)
    inspect_count_dict = get_num_inspections(monkeys)
    sorted_counts = sorted(inspect_count_dict.items(), key=lambda x: x[1], reverse=True)

    monkey_business = 1

    for monkey in sorted_counts[:2]:
        monkey_business *= monkey[1]

    return monkey_business


if __name__ == "__main__":
    print(main())
