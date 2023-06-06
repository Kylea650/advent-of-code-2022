fn main() {
    let input: String = std::fs::read_to_string("../day1.txt").unwrap();

    let mut groups: Vec<u32> = input
        .split("\n\n")
        .map(|x: &str| {
            x.lines()
                .map(|x: &str| x.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<_>>();

    groups.sort();

    let day1: u32 = groups[groups.len() - 1];
    let day2: u32 = groups[groups.len() - 3..groups.len()].iter().sum::<u32>();

    println!("Day 1: {}\nDay 2: {}", day1, day2);
}
