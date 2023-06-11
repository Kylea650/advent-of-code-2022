fn parse_crates(crates: Vec<String>) -> Vec<Vec<String>> {
    crates
        .into_iter()
        .map(|x| x.replace("    ", "[0]").replace(' ', ""))
        .collect::<Vec<_>>()
        .into_iter()
        .map(|x| {
            x.split("][")
                .map(|x| x.replace(['[', ']'], ""))
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn rotate_crates(crates: Vec<Vec<String>>) -> Vec<Vec<String>> {
    let mut rotated = Vec::new();

    for i in 0..=crates.len() {
        let mut tmp = Vec::new();

        for j in crates.iter().rev() {
            let value = j[i].to_owned();
            match value.as_str() {
                "0" => break,
                _ => tmp.push(value),
            }
        }
        rotated.push(tmp);
    }
    rotated
}

fn parse_instructions(insructions: Vec<String>) -> Vec<Vec<u32>> {
    insructions
        .iter()
        .map(|x| {
            x.split_whitespace()
                .enumerate()
                .filter(|&(i, _)| i % 2 != 0)
                .map(|(_, x)| x.parse::<u32>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn get_top_crates(crates: Vec<Vec<String>>) -> String {
    let mut top_crates = String::new();

    for i in crates {
        let top_crate = i[(i.len() - 1)].as_str();
        top_crates.push_str(top_crate);
    }
    top_crates
}

fn main() {
    let input = std::fs::read_to_string("day5.txt")
        .unwrap()
        .split("\n\n")
        .map(|x| x.lines().map(|x| x.to_string()).collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let str_instructions = input[1].to_owned();
    let instructions = parse_instructions(str_instructions);

    let rotated_crates = parse_crates(input[0][0..input[0].len() - 1].to_owned());
    let mut crates1 = rotate_crates(rotated_crates);
    let mut crates2 = crates1.clone();

    for i in instructions {
        let num_crates = i[0];
        let src = (i[1] - 1) as usize;
        let dst = (i[2] - 1) as usize;

        let crates2_len = crates2[src].len();
        let to_move_part_two =
            crates2[src][(crates2_len - (num_crates as usize))..crates2_len].to_owned();

        for i in to_move_part_two {
            crates2[dst].push(i);
        }

        for _j in 0..=num_crates - 1 {
            let to_move_part_one = crates1[src][(crates1[src].len() - 1)].to_owned();
            crates1[dst].push(to_move_part_one);
            crates1[src].pop();
            crates2[src].pop();
        }
    }
    let part_one = get_top_crates(crates1);
    let part_two = get_top_crates(crates2);
    println!("Part 1: {:?}\nPart 2: {:?}", part_one, part_two);
}
