use std::collections::HashMap;

fn parse_input(input: String) -> Vec<Vec<String>> {
    input
        .lines()
        .map(|x| {
            x.to_owned()
                .replace("$ ", "")
                .split_whitespace()
                .map(|x| x.to_owned())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>()
}

fn get_dir_sizes(commands: Vec<Vec<String>>) -> HashMap<String, u32> {
    let mut dir_dict: HashMap<String, u32> = HashMap::new();
    let mut path = vec![String::from("/")];

    for command in commands.iter() {
        let current_dir = path.join("")[1..].to_owned();

        match command[0].as_str() {
            "cd" => match command[1].as_str() {
                "/" => {
                    dir_dict.insert(String::from("/"), 0);
                }
                ".." => {
                    let len = path.len() - 1;
                    path.truncate(len)
                }
                _ => {
                    let dir_name = current_dir + &command[1] + "/";
                    let d_name = dir_name.clone();
                    dir_dict.insert(dir_name, 0);
                    path.push(d_name);
                }
            },
            "ls" => continue,
            "dir" => continue,
            _ => {
                let file_size = command[0].parse::<u32>().unwrap();
                for dir in &path {
                    let cur_size = dir_dict.get(dir).unwrap();
                    dir_dict.insert(dir.to_string(), cur_size + file_size);
                }
            }
        }
    }
    dir_dict
}

fn get_dir_sums(dirs: HashMap<String, u32>, max_size: u32) -> u32 {
    dirs.into_values().filter(|x| *x <= max_size).sum::<u32>()
}

fn get_min_dir_size(dir_sizes: &HashMap<String, u32>) -> u32 {
    const TOTAL_DISK_SPACE: u32 = 70_000_000;
    const UPDATE_SIZE: u32 = 30_000_000;
    let free_space = TOTAL_DISK_SPACE - dir_sizes.get("/").unwrap();

    UPDATE_SIZE - free_space
}

fn get_dir_to_delete(dir_sizes: HashMap<String, u32>, min_size: u32) -> u32 {
    let mut vec_dir_sizes = dir_sizes.values().cloned().collect::<Vec<_>>();
    vec_dir_sizes.sort();

    let mut dir = 0;

    for i in vec_dir_sizes {
        match i {
            x if x >= min_size => {
                dir = i;
                break;
            }
            _ => continue,
        }
    }
    dir
}

fn main() {
    let input = std::fs::read_to_string("day7.txt").unwrap();
    let commands = parse_input(input);

    let dir_sizes = get_dir_sizes(commands);
    let dir_sizes_two = dir_sizes.clone();
    let min_size = get_min_dir_size(&dir_sizes_two);

    let part_one = get_dir_sums(dir_sizes, 100000);
    let part_two = get_dir_to_delete(dir_sizes_two, min_size);

    println!("Part 1: {}\nPart 2: {}", part_one, part_two);
}
