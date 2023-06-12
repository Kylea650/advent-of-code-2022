use std::collections::HashSet;

fn parse_input(input: String) -> Vec<char> {
    input.chars().into_iter().collect::<Vec<_>>()
}

fn split_windows(chars: &[char], size: usize) -> Vec<HashSet<char>> {
    chars
        .windows(size)
        .map(|x| x.iter().map(|x| x.to_owned()).collect::<HashSet<_>>())
        .collect::<Vec<_>>()
}

fn find_marker(windows: &[HashSet<char>], window_size: usize) -> usize {
    let mut marker: usize = 0;

    for (i, set) in windows.iter().enumerate() {
        match set.len() {
            x if x == window_size => {
                marker = i;
                break;
            }
            _ => continue,
        }
    }
    marker + window_size
}

fn main() {
    let input = std::fs::read_to_string("day6.txt").unwrap();
    let chars = parse_input(input);

    let windows_part_one = split_windows(&chars, 4);
    let windows_part_two = split_windows(&chars, 14);

    let part_one = find_marker(&windows_part_one, 4);
    let part_two = find_marker(&windows_part_two, 14);

    println!("Part 1: {}\nPart 2: {}", part_one, part_two);

    // for (i, set) in windows_part_one.iter().enumerate() {
    //     match set.len() {
    //         4 => {
    //             println!("Part 1: {}", i + 4);
    //             break;
    //         }
    //         _ => continue,
    //     }
    // }

    // for (i, set) in windows_part_two.iter().enumerate() {
    //     match set.len() {
    //         14 => {
    //             println!("Part 2: {}", i + 14);
    //             break;
    //         }
    //         _ => continue,
    //     }
    // }
}
