use std::fs;
#[derive(Debug, PartialEq)]
enum MovementKind {
    Forward,
    Up,
    Down,
}

#[derive(Debug, PartialEq)]
struct Movement {
    kind: MovementKind,
    value: i32,
}

fn calculate_horizontal_pos_and_depth(moves: &Vec<Movement>) -> (i32, i32) {
    let mut horizontal_pos = 0;
    let mut depth = 0;
    for m in moves {
        match m.kind {
            MovementKind::Forward => {
                horizontal_pos += m.value;
            }
            MovementKind::Up => {
                depth -= m.value;
            }
            MovementKind::Down => {
                depth += m.value;
            }
        }
    }
    (horizontal_pos, depth)
}

fn calculate_horizontal_pos_and_depth_with_aim(moves: &Vec<Movement>) -> (i32, i32) {
    let mut aim = 0;
    let mut horizontal_pos = 0;
    let mut depth = 0;
    for m in moves {
        match m.kind {
            MovementKind::Forward => {
                horizontal_pos += m.value;
                depth += aim * m.value;
            }
            MovementKind::Up => {
                aim -= m.value;
            }
            MovementKind::Down => {
                aim += m.value;
            }
        }
    }
    (horizontal_pos, depth)
}

fn line_to_movement(input: &str) -> Movement {
    let g_index = input.find(" ").unwrap();
    let (kind, value) = input.split_at(g_index);
    let kind = match kind {
        "forward" => MovementKind::Forward,
        "up" => MovementKind::Up,
        "down" => MovementKind::Down,
        _ => panic!("Unknown movement kind"),
    };
    let value = value.trim().parse().unwrap();
    Movement { kind, value }
}
fn lines_to_movements(input: &str) -> Vec<Movement> {
    input
        .split('\n')
        .filter(|x| *x != "")
        .map(|x| line_to_movement(x))
        .collect()
}

fn day01a() -> i32 {
    let content = fs::read_to_string("resources/year2021/day02.txt")
        .expect("Something went wrong reading the file");
    let movements = lines_to_movements(&content);
    let (horizontal_pos, depth) = calculate_horizontal_pos_and_depth(&movements);
    horizontal_pos * depth
}

fn day01b() -> i32 {
    let content = fs::read_to_string("resources/year2021/day02.txt")
        .expect("Something went wrong reading the file");
    let movements = lines_to_movements(&content);
    let (horizontal_pos, depth) = calculate_horizontal_pos_and_depth_with_aim(&movements);
    horizontal_pos * depth
}

#[test]
fn string_to_movement_simple_parsing() {
    let result = lines_to_movements("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2\n");
    assert_eq!(
        Movement {
            kind: MovementKind::Forward,
            value: 5
        },
        result[0]
    );
}

#[test]
fn solution_day01() {
    assert_eq!(1636725, day01a());
    assert_eq!(1872757425, day01b());
}
