use std::collections::HashSet;

fn parse_input(input: String) -> Vec<Vec<String>> {
    input
        .lines()
        .map(|x| {
            x.split_whitespace()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn not_touching(head_row: i32, head_col: i32, tail_row: i32, tail_col: i32) -> bool {
    (head_row - tail_row).abs() > 1 || (head_col - tail_col).abs() > 1
}

fn main() {
    let input = std::fs::read_to_string("day9.txt").unwrap();
    let motions = parse_input(input);

    let mut head = (0, 0);
    let mut tail = (0, 0);
    let mut visited_p1: HashSet<(i32, i32)> = HashSet::new();
    let mut visited_p2: HashSet<(i32, i32)> = HashSet::new();
    let mut knots = vec![
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ];
    visited_p1.insert(tail);
    visited_p2.insert(knots[0]);

    for motion in motions.iter() {
        let direction = motion[0].as_str();
        let steps = motion[1].parse::<i32>().unwrap();

        for _i in 0..steps {
            match direction {
                "L" => {
                    knots[0] = (knots[0].0 - 1, knots[0].1);
                    head = (head.0 - 1, head.1);
                    match not_touching(head.0, head.1, tail.0, tail.1) {
                        true => {
                            tail = (tail.0 - 1, head.1);
                            visited_p1.insert(tail);
                        }
                        false => continue,
                    }
                }
                "R" => {
                    knots[0] = (knots[0].0 + 1, knots[0].1);
                    head = (head.0 + 1, head.1);
                    match not_touching(head.0, head.1, tail.0, tail.1) {
                        true => {
                            tail = (tail.0 + 1, head.1);
                            visited_p1.insert(tail);
                        }
                        false => continue,
                    }
                }
                "U" => {
                    knots[0] = (knots[0].0, knots[0].1 + 1);
                    head = (head.0, head.1 + 1);
                    match not_touching(head.0, head.1, tail.0, tail.1) {
                        true => {
                            tail = (head.0, tail.1 + 1);
                            visited_p1.insert(tail);
                        }
                        false => continue,
                    }
                }
                "D" => {
                    knots[0] = (knots[0].0, knots[0].1 - 1);
                    head = (head.0, head.1 - 1);
                    match not_touching(head.0, head.1, tail.0, tail.1) {
                        true => {
                            tail = (head.0, tail.1 - 1);
                            visited_p1.insert(tail);
                        }
                        false => continue,
                    }
                }
                _ => panic!("Direction not recognised."),
            }

            for i in 0..knots.len() - 1 {
                match not_touching(knots[i].0, knots[i].1, knots[i + 1].0, knots[i + 1].1) {
                    true => {
                        let row_diff = knots[i].0 - knots[i + 1].0;
                        let col_diff = knots[i].1 - knots[i + 1].1;

                        let row = match row_diff {
                            0 => 0,
                            x if x < 0 => -1,
                            _ => 1,
                        };
                        let col = match col_diff {
                            0 => 0,
                            x if x < 0 => -1,
                            _ => 1,
                        };
                        knots[i + 1] = (knots[i + 1].0 + row, knots[i + 1].1 + col);
                    }
                    false => continue,
                }
                visited_p2.insert(*knots.last().unwrap());
            }
        }
    }
    let part_one = visited_p1.len();
    let part_two = visited_p2.len();

    println!("Part 1: {}\nPart 2: {}", part_one, part_two);
}
