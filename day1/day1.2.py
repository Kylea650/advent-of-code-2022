def parse_file(file):
    with open(file) as f:
        lines = f.readlines()

    calories = [line.rstrip("\n") for line in lines]

    return calories


def calorie_counter(lst):
    sums = []
    count = 0

    for i in lst:
        if i == "":
            sums.append(count)
            count = 0
        else:
            count += int(i)

    sorted_sums = sorted(sums)
    top_three = sorted_sums[-3:]

    return sum(top_three)


def main():
    calories = parse_file("day1.txt")
    max_calories = calorie_counter(calories)

    print(max_calories)


if __name__ == "__main__":
    main()
