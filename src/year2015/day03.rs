use std::collections::HashMap;
use std::fs;

#[derive(PartialEq, Eq, PartialOrd, Ord, Hash, Debug)]
struct Position {
    x: i32,
    y: i32,
}

fn move_santa(start: Position, c: char) -> Position {
    match c {
        '>' => Position {
            x: start.x + 1,
            y: start.y,
        },
        '<' => Position {
            x: start.x - 1,
            y: start.y,
        },
        '^' => Position {
            x: start.x,
            y: start.y + 1,
        },
        'v' => Position {
            x: start.x,
            y: start.y - 1,
        },
        _ => Position { x: start.x, y: start.y }
    }
}

fn count_houses_with_present(presents_per_position: HashMap<Position, i32>) -> i32 {
    presents_per_position.len() as i32
}

fn houses_with_at_least_one_present(input: &str) -> i32 {
    let mut pos = Position { x: 0, y: 0 };
    let mut presents_per_position: HashMap<Position, i32> = HashMap::new();
    presents_per_position.insert(Position { x: pos.x, y: pos.y }, 1);
    for x in input.chars() {
        pos = move_santa(pos, x);
        let new_pos = Position { x: pos.x, y: pos.y };
        let old_value = presents_per_position.get(&new_pos).unwrap_or(&0).clone();
        presents_per_position.insert(new_pos, old_value + 1);
    }

    count_houses_with_present(presents_per_position)
}

fn houses_with_at_least_one_present_w_robo(input: &str) -> i32 {
    let mut pos = Position { x: 0, y: 0 };
    let mut robopos = Position { x: 0, y: 0 };
    let mut presents_per_position: HashMap<Position, i32> = HashMap::new();
    presents_per_position.insert(Position { x: pos.x, y: pos.y }, 1);

    let mut robo = false;
    for x in input.chars() {
        let new_pos = if robo {
            robo = false;
            robopos = move_santa(robopos, x);
            Position { x: robopos.x, y: robopos.y }
        } else {
            robo = true;
            pos = move_santa(pos, x);
            Position { x: pos.x, y: pos.y }
        };
        let old_value = presents_per_position.get(&new_pos).unwrap_or(&0).clone();
        presents_per_position.insert(new_pos, old_value + 1);
    }

    count_houses_with_present(presents_per_position)
}


fn day03a() -> i32 {
    let content = fs::read_to_string("resources/year2015/day03.txt")
        .expect("Something went wrong reading the file");
    houses_with_at_least_one_present(&content)
}

fn day03b() -> i32 {
    let content = fs::read_to_string("resources/year2015/day03.txt")
        .expect("Something went wrong reading the file");
    houses_with_at_least_one_present_w_robo(&content)
}

#[test]
fn houses_with_at_least_one_present_examples() {
    assert_eq!(2, houses_with_at_least_one_present(">"));
    assert_eq!(4, houses_with_at_least_one_present("^>v<"));
    assert_eq!(2, houses_with_at_least_one_present("^v^v^v^v^v"));
}

#[test]
fn houses_with_at_least_one_present_w_robo_examples() {
    assert_eq!(3, houses_with_at_least_one_present_w_robo("^v"));
    assert_eq!(3, houses_with_at_least_one_present_w_robo("^>v<"));
    assert_eq!(11, houses_with_at_least_one_present_w_robo("^v^v^v^v^v"));
}

#[test]
fn move_santa_examples() {
    assert_eq!(Position { x: 1, y: 0 }, move_santa(Position { x: 0, y: 0 }, '>'));
}

#[test]
fn solution_day03() {
    assert_eq!(2572, day03a());
    assert_eq!(2631, day03b());
}
