fn parse_input(input: String) -> Vec<Vec<u32>> {
    input
        .lines()
        .map(|x| {
            x.split(',')
                .flat_map(|x| {
                    x.split('-')
                        .map(|x| x.parse::<u32>().unwrap())
                        .collect::<Vec<_>>()
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn fully_contains(pairs: &[u32]) -> bool {
    if (pairs[0] <= pairs[2] && pairs[1] >= pairs[3])
        || (pairs[0] >= pairs[2] && pairs[1] <= pairs[3])
    {
        return true;
    }
    false
}

fn overlaps(pairs: &[u32]) -> bool {
    if pairs[1] >= pairs[2] && pairs[3] >= pairs[0] {
        return true;
    }
    false
}

fn main() {
    let input = std::fs::read_to_string("day4.txt").unwrap();
    let pairs = parse_input(input);

    let mut part_one = 0;
    let mut part_two = 0;

    for pair in pairs {
        if fully_contains(&pair) {
            part_one += 1;
        }
        if overlaps(&pair) {
            part_two += 1;
        }
    }
    println!("Part 1: {}\nPart 2: {}", part_one, part_two);
}
