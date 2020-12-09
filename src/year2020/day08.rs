use std::fs;

fn parse_commands(input: String) -> Vec<(String, isize)> {
    input.lines().map(|l| {
        let parts: Vec<&str> = l.split(" ").collect();
        let instruction = parts[0];
        let sign: char = parts[1].chars().nth(0).unwrap();
        let number = parts[1][1..].to_string().parse::<i32>().unwrap() as isize;
        if sign == '-' {
            (instruction.to_string(), number * -1)
        } else {
            (instruction.to_string(), number)
        }
    }).collect()
}

fn find_infinite_loop(current_index: usize, all_commands: Vec<(String, isize)>, acc: isize, mut visited_indices: Vec<usize>) -> isize {
    if visited_indices.contains(&current_index) {
        return acc;
    }
    let (instruction, amount) = all_commands.get(current_index).unwrap();
    visited_indices.push(current_index.clone());
    match instruction.as_str() {
        "acc" => find_infinite_loop(current_index + 1, all_commands.clone(), acc + amount, visited_indices),
        "jmp" => find_infinite_loop((current_index as isize + amount) as usize, all_commands.clone(), acc, visited_indices),
        _ => find_infinite_loop(current_index + 1, all_commands.clone(), acc, visited_indices),
    }
}

fn finishes(current_index: usize, all_commands: Vec<(String, isize)>, acc: isize, mut visited_indices: Vec<usize>) -> Option<isize> {
    if current_index == all_commands.len() {
        return Some(acc);
    }
    if visited_indices.contains(&current_index) {
        return None;
    }
    let (instruction, amount) = all_commands.get(current_index).unwrap();
    visited_indices.push(current_index.clone());
    match instruction.as_str() {
        "acc" => finishes(current_index + 1, all_commands.clone(), acc + amount, visited_indices),
        "jmp" => finishes((current_index as isize + amount) as usize, all_commands.clone(), acc, visited_indices),
        _ => finishes(current_index + 1, all_commands.clone(), acc, visited_indices),
    }
}

fn change_command(all_commands: Vec<(String, isize)>, index: usize) -> Vec<(String, isize)> {
    let command = all_commands.get(index).unwrap();
    let new_cmd = if command.0 == "jmp" {
        ("nop".to_string(), command.1)
    } else if command.0 == "nop" {
        ("jmp".to_string(), command.1)
    } else {
        (command.0.clone(), command.1)
    };
    let mut my_new_commands = all_commands.clone();
    my_new_commands[index] = new_cmd;
    my_new_commands
}

fn bug_fix(all_commands: Vec<(String, isize)>) -> isize {
    all_commands.iter().enumerate().map(|(i, c)| {
        let cmd_set = change_command(all_commands.clone(), i.clone());
        finishes(0, cmd_set, 0, vec![])
    }).filter(|o| o.is_some()).nth(0).unwrap().unwrap()
}

fn day08a() -> isize {
    let content = fs::read_to_string("resources/year2020/day08.txt")
        .expect("Something went wrong reading the file");
    let commands = parse_commands(content);
    find_infinite_loop(0, commands, 0, vec![])
}

fn day08b() -> isize {
    let content = fs::read_to_string("resources/year2020/day08.txt")
        .expect("Something went wrong reading the file");
    let commands = parse_commands(content);
    bug_fix(commands)
}

#[test]
fn change_command_test() {
    assert_eq!(vec![("jmp".to_string(), -1)], change_command(vec![("nop".to_string(), -1)], 0));
    assert_eq!(vec![("jmp".to_string(), -1), ("jmp".to_string(), -1)], change_command(vec![("jmp".to_string(), -1), ("nop".to_string(), -1)], 1));
}

#[test]
fn find_infinite_loop_example() {
    let input = "nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6".to_string();
    let commands = parse_commands(input);
    assert_eq!(5, find_infinite_loop(0, commands.clone(), 0, vec![]));
}

#[test]
fn bug_fix_example() {
    let input = "nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6".to_string();
    let commands = parse_commands(input);
    assert_eq!(8, bug_fix(commands.clone()));
}

#[test]
fn solution_day08() {
    assert_eq!(1723, day08a());
    assert_eq!(846, day08b());
}
