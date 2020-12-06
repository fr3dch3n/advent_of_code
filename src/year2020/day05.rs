use std::fs;

fn seat_id(input: String) -> u32 {
    let (row_part, column_part) = input.split_at(7);
    move_to_destination(row_part.to_string(), 1, 128, 'B', 'F') * 8 + move_to_destination(column_part.to_string(), 1, 8, 'R', 'L')
}

fn move_to_destination(input: String, lower_bound: u32, upper_bound: u32, lower_key: char, upper_key: char) -> u32 {
    fn do_it(c: char, lower_key: char, upper_key: char, lower: u32, upper: u32) -> (u32, u32) {
        let step_size = (upper - lower) / 2;
        match c {
            _ if c == lower_key => (upper - step_size, upper),
            _ if c == upper_key => (lower, upper - step_size),
            _ => (0, 0)
        }
    }
    input
        .chars()
        .fold((lower_bound, upper_bound), |(lower, upper), x| do_it(x, lower_key, upper_key, lower, upper))
        .0 - 1
}

fn seat_ids(input: String) -> Vec<u32> {
    input.lines().map(|l| seat_id(l.to_string())).collect()
}

fn max_seat_id(input: String) -> u32 {
    seat_ids(input).iter().max().unwrap().clone()
}

fn my_seat_id(input: String) -> u32 {
    let mut seat_ids: Vec<u32> = input.lines().map(|l| seat_id(l.to_string())).collect();
    seat_ids.sort();
    for (i, x) in seat_ids.iter().enumerate() {
        if x + 2 == seat_ids[i + 1] {
            return x + 1;
        }
    }
    0
}

fn day05a() -> u32 {
    let content = fs::read_to_string("resources/year2020/day05.txt")
        .expect("Something went wrong reading the file");
    max_seat_id(content)
}

fn day05b() -> u32 {
    let content = fs::read_to_string("resources/year2020/day05.txt")
        .expect("Something went wrong reading the file");
    my_seat_id(content)
}

#[test]
fn seat_id_examples() {
    assert_eq!(567, seat_id(String::from("BFFFBBFRRR")));
    assert_eq!(119, seat_id(String::from("FFFBBBFRRR")));
    assert_eq!(820, seat_id(String::from("BBFFBBFRLL")));
}

#[test]
fn row_examples() {
    assert_eq!(70, move_to_destination(String::from("BFFFBBF"), 1, 128, 'B', 'F'));
    assert_eq!(14, move_to_destination(String::from("FFFBBBF"), 1, 128, 'B', 'F'));
    assert_eq!(102, move_to_destination(String::from("BBFFBBF"), 1, 128, 'B', 'F'));
}

#[test]
fn column_examples() {
    assert_eq!(7, move_to_destination(String::from("RRR"), 1, 8, 'R', 'L'));
    assert_eq!(4, move_to_destination(String::from("RLL"), 1, 8, 'R', 'L'));
    assert_eq!(3, move_to_destination(String::from("LRR"), 1, 8, 'R', 'L'));
    assert_eq!(0, move_to_destination(String::from("LLL"), 1, 8, 'R', 'L'));
}

#[test]
fn solution_day05() {
    assert_eq!(953, day05a());
    assert_eq!(615, day05b());
}
