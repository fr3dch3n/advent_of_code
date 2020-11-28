use std::fs;

fn square_foot_wrapping_paper(input: &str) -> i32 {
    let lines: Vec<&str> = input.split('\n').collect();
    lines.iter().fold(0, |acc, x| acc + wrapping_paper_per_present(x))
}

fn wrapping_paper_per_present(input: &str) -> i32 {
    let mut parts: Vec<i32> = input.split('x').map(|x| x.parse::<i32>().unwrap()).collect();
    let l = parts[0];
    let w = parts[1];
    let h = parts[2];
    parts.sort();
    (2*l*w + 2*w*h + 2*h*l) + (parts[0] * parts[1])
}

fn day02a() -> i32 {
    let content = fs::read_to_string("resources/year2015/day02.txt")
        .expect("Something went wrong reading the file");
    square_foot_wrapping_paper(&content)
}

fn ribbon(input: &str) -> i32 {
    let lines: Vec<&str> = input.split('\n').collect();
    lines.iter().fold(0, |acc, x| acc + ribbon_per_present(x))
}

fn ribbon_per_present(input: &str) -> i32 {
    let mut parts: Vec<i32> = input.split('x').map(|x| x.parse::<i32>().unwrap()).collect();
    let l = parts[0];
    let w = parts[1];
    let h = parts[2];
    parts.sort();
    (parts[0] * 2 + parts[1] * 2) + l * w * h
}

fn day02b() -> i32 {
    let content = fs::read_to_string("resources/year2015/day02.txt")
        .expect("Something went wrong reading the file");
    ribbon(&content)
}

#[test]
fn square_foot_wrapping_paper_examples() {
    assert_eq!(58, wrapping_paper_per_present("2x3x4"));
    assert_eq!(43, wrapping_paper_per_present("1x1x10"));
}
#[test]
fn ribbon_per_present_examples() {
    assert_eq!(34, ribbon_per_present("2x3x4"));
    assert_eq!(14, ribbon_per_present("1x1x10"));
}
#[test]
fn solution_day02() {
    assert_eq!(1598415, day02a());
    assert_eq!(3812909, day02b());
}
