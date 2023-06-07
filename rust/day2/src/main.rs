fn parse_input(input: String) -> Vec<Vec<String>> {
    input
        .lines()
        .map(|x| x.split(' ').map(|x| x.to_string()).collect::<Vec<_>>())
        .collect::<Vec<_>>()
}

fn part1_outcome(round: &[String]) -> u32 {
    let (a, b) = (round[0].as_str(), round[1].as_str());

    match a {
        // they pick rock
        "A" => match b {
            "X" => 4, // we pick rock (1) + draw (3)
            "Y" => 8, // we pick paper (2) + win (6)
            "Z" => 3, // we pick scissors (3) + lose (0)
            _ => panic!(),
        },
        // they pick paper
        "B" => match b {
            "X" => 1,
            "Y" => 5,
            "Z" => 9,
            _ => panic!(),
        },
        //they pick scissors
        "C" => match b {
            "X" => 7,
            "Y" => 2,
            "Z" => 6,
            _ => panic!(),
        },
        _ => panic!(),
    }
}

fn part2_outcome(round: &[String]) -> u32 {
    let (a, b) = (round[0].as_str(), round[1].as_str());

    match a {
        // they pick rock
        "A" => match b {
            "X" => 3, // lose (0) + we pick scissors (3)
            "Y" => 4, // draw (3) + we pick rock (1)
            "Z" => 8, // win (6) + we pick paper (2)
            _ => panic!(),
        },
        // they pick paper
        "B" => match b {
            "X" => 1,
            "Y" => 5,
            "Z" => 9,
            _ => panic!(),
        },
        // they pick scissors
        "C" => match b {
            "X" => 2,
            "Y" => 6,
            "Z" => 7,
            _ => panic!(),
        },
        _ => panic!(),
    }
}

fn main() {
    let input = std::fs::read_to_string("day2.txt").unwrap();
    let rounds = parse_input(input);

    let mut part1_score = 0;
    let mut part2_score = 0;

    for round in rounds {
        part1_score += part1_outcome(&round);
        part2_score += part2_outcome(&round);
    }
    println!("Part 1: {}\nPart 2: {}", part1_score, part2_score);
}
