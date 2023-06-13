fn parse_input(input: String) -> Vec<Vec<u32>> {
    input
        .lines()
        .map(|x| {
            x.chars()
                .map(|x| x.to_digit(10).unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn can_be_seen(trees: &Vec<Vec<u32>>, row: usize, col: usize) -> bool {
    let height = trees[row][col];

    let mut left = true;
    let mut right = true;
    let mut up = true;
    let mut down = true;

    if (col == 0 || col == trees[row].len() - 1) | (row == 0 || row == trees.len() - 1) {
        // tree on the edge
        true
    } else {
        // checking left
        for i in 0..trees[row][..col].len() {
            match trees[row][i] {
                x if x >= height => left = false,
                _ => continue,
            }
        }
        // checking right
        for i in (col + 1)..trees[row].len() {
            match trees[row][i] {
                x if x >= height => right = false,
                _ => continue,
            }
        }
        // checking up
        for i in trees.iter().take(trees[..row].len()) {
            match i[col] {
                x if x >= height => up = false,
                _ => continue,
            }
        }
        // checking down
        for i in trees.iter().skip(row + 1) {
            match i[col] {
                x if x >= height => down = false,
                _ => continue,
            }
        }
        // if can be seen from any direction
        left | right | up | down
    }
}

fn get_scenic_score(trees: &Vec<Vec<u32>>, row: usize, col: usize) -> u32 {
    let height = trees[row][col];

    let mut left = 0;
    let mut right = 0;
    let mut up = 0;
    let mut down = 0;

    let mut idx: i32;

    // checking left
    idx = col as i32 - 1;
    while idx >= 0 {
        match trees[row][idx as usize] {
            x if x >= height => {
                left += 1;
                break;
            }
            _ => {
                left += 1;
            }
        }
        idx -= 1;
    }

    // checking right
    idx = (col + 1) as i32;
    while idx < trees[row].len() as i32 {
        match trees[row][idx as usize] {
            x if x >= height => {
                right += 1;
                break;
            }
            _ => {
                right += 1;
            }
        }
        idx += 1;
    }

    // checking up
    idx = row as i32 - 1;
    while idx >= 0 {
        match trees[idx as usize][col] {
            x if x >= height => {
                up += 1;
                break;
            }
            _ => {
                up += 1;
            }
        }
        idx -= 1;
    }

    // checking down
    idx = (row + 1) as i32;
    while idx < trees.len() as i32 {
        match trees[idx as usize][col] {
            x if x >= height => {
                down += 1;
                break;
            }
            _ => {
                down += 1;
            }
        }
        idx += 1;
    }
    left * right * up * down
}

fn main() {
    let input = std::fs::read_to_string("day8.txt").unwrap();
    let trees = parse_input(input);

    let mut part_one = 0;
    let mut scenic_scores: Vec<u32> = Vec::new();

    for i in 0..trees.len() {
        for j in 0..trees[i].len() {
            match can_be_seen(&trees, i, j) {
                true => part_one += 1,
                false => continue,
            }
            scenic_scores.push(get_scenic_score(&trees, i, j));
        }
    }
    let part_two = scenic_scores.iter().max().unwrap();
    println!("Part 1: {}\nPart 2: {}", part_one, part_two);
}
