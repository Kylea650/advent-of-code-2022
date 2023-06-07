fn parse_input(input: String) -> Vec<String> {
    input.lines().map(|x| x.to_string()).collect::<Vec<_>>()
}

fn find_common_item_part_one(rucksack: &str) -> char {
    let (a, b) = rucksack.split_at(rucksack.len() / 2);
    a.chars().find(|item| b.contains(*item)).unwrap()
}

fn find_common_item_part_two(rucksacks: Vec<String>) -> char {
    let (a, b, c) = (
        rucksacks[0].as_str(),
        rucksacks[1].as_str(),
        rucksacks[2].as_str(),
    );
    a.chars()
        .find(|item| b.contains(*item) && c.contains(*item))
        .unwrap()
}

fn get_char_value(char: char) -> u16 {
    match char {
        'a'..='z' => char as u16 - 96,
        'A'..='Z' => char as u16 - 38,
        _ => panic!(),
    }
}

fn main() {
    let input = std::fs::read_to_string("day3.txt").unwrap();
    let rucksacks = parse_input(input);

    let mut part_one = 0;

    for rucksack in &rucksacks {
        part_one += get_char_value(find_common_item_part_one(rucksack));
    }

    let mut part_two = 0;

    for group in rucksacks.chunks(3) {
        part_two += get_char_value(find_common_item_part_two(group.to_owned()));
    }

    println!("Part 1: {}\nPart 2: {}", part_one, part_two);
}
