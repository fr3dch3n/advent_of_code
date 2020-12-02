use std::fs;
use regex::Regex;

struct Line {
    first: i32,
    second: i32,
    letter: String,
    password: String,
}

fn parse_line(input: &str) -> Line {
    lazy_static! {
        static ref RE: Regex = Regex::new(r"(\d{0,4})-(\d{0,4}) (.+): (.+)").unwrap();
    }
    let cap = RE.captures(input).unwrap();
    let min: &str = &cap[1];
    let max: &str = &cap[2];
    let letter: &str = &cap[3];
    let password: &str = &cap[4];
    let min_int = min.parse::<i32>().unwrap();
    let max_int = max.parse::<i32>().unwrap();
    Line {
        first: min_int,
        second: max_int,
        letter: letter.to_string(),
        password: password.to_string(),
    }
}

fn pw_is_valid(input: &str) -> bool {
    let l = parse_line(input);
    let c = l.password.matches(&l.letter).count() as i32;
    l.first <= c && c <= l.second
}

fn pw_is_valid_part_two(input: &str) -> bool {
    let l = parse_line(input);
    let first_char = l.password.chars().nth((l.first - 1) as usize).unwrap().to_string();
    let second_char = l.password.chars().nth((l.second - 1) as usize).unwrap().to_string();

    (first_char == l.letter && second_char != l.letter) || (first_char != l.letter && second_char == l.letter)
}

fn how_many_passwords_are_valid(input: &str, f: &dyn Fn(&str) -> bool) -> i32 {
    input
        .split('\n')
        .filter(|x| !x.is_empty())
        .filter(|x| f(x))
        .count() as i32
}

fn day02a() -> i32 {
    let content = fs::read_to_string("resources/year2020/day02.txt")
        .expect("Something went wrong reading the file");
    how_many_passwords_are_valid(&content, &pw_is_valid)
}

fn day02b() -> i32 {
    let content = fs::read_to_string("resources/year2020/day02.txt")
        .expect("Something went wrong reading the file");
    how_many_passwords_are_valid(&content, &pw_is_valid_part_two)
}

#[test]
fn how_many_passwords_are_valid_examples() {
    assert_eq!(2, how_many_passwords_are_valid("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n", &pw_is_valid));
    assert_eq!(1, how_many_passwords_are_valid("1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n", &pw_is_valid_part_two));
}

#[test]
fn solution_day02() {
    assert_eq!(456, day02a());
    assert_eq!(308, day02b());
}
