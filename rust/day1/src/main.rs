fn parse_input(input: String) -> Vec<u32> {
    let calories = input
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.parse::<u32>().unwrap()).sum::<u32>())
        .collect::<Vec<_>>();

    calories
}

fn main() {
    let input = std::fs::read_to_string("../day1.txt").unwrap();

    let mut calories = parse_input(input);
    calories.sort();

    let day1 = calories[calories.len() - 1];
    let day2 = calories[calories.len() - 3..calories.len()]
        .iter()
        .sum::<u32>();

    println!("Day 1: {}\nDay 2: {}", day1, day2);
}
