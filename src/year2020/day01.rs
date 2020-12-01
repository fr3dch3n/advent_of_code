use std::fs;

fn find_2020(input: Vec<i32>) -> (i32, i32) {
    let vec = input.clone();
    for x in input {
        for y in &vec {
            if x + y == 2020 {
                return (x, *y);
            }
        }
    }
    return (-1, -1);
}

fn find_2020_by_three(input: Vec<i32>) -> (i32, i32, i32) {
    let vec = input.clone();
    let vec2 = input.clone();
    for x in input {
        for y in &vec {
            for z in &vec2 {
                if x + y + z == 2020 {
                    return (x, *y, *z);
                }
            }
        }
    }
    return (-1, -1, -1);
}

fn string_to_ints(input: &str) -> Vec<i32> {
    input
        .split('\n')
        .filter(|x| *x != "")
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

fn day01a() -> i32 {
    let content = fs::read_to_string("resources/year2020/day01.txt")
        .expect("Something went wrong reading the file");
    let ints = string_to_ints(&content);
    let (a, b) = find_2020(ints);
    a * b
}

fn day01b() -> i32 {
    let content = fs::read_to_string("resources/year2020/day01.txt")
        .expect("Something went wrong reading the file");
    let ints = string_to_ints(&content);
    let (a, b, c) = find_2020_by_three(ints);
    a * b * c
}

#[test]
fn find_2020_examples() {
    assert_eq!((1721, 299), find_2020(vec![1721, 979, 366, 299, 675, 1456]));
}

#[test]
fn find_2020_by_three_examples() {
    assert_eq!((979, 366, 675), find_2020_by_three(vec![1721, 979, 366, 299, 675, 1456]));
}

#[test]
fn string_to_ints_simple_parsing() {
    assert_eq!(vec![1, 2, 3], string_to_ints("1\n2\n3\n"));
    assert_eq!(vec![1], string_to_ints("1"));
}

#[test]
fn solution_day01() {
    assert_eq!(888331, day01a());
    assert_eq!(130933530, day01b());
}
