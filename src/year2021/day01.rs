use std::fs;

fn string_to_ints(input: &str) -> Vec<i32> {
    input
        .split('\n')
        .filter(|x| *x != "")
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

fn how_often_decreases(input: Vec<i32>) -> i32 {
    let mut nr_of_decreases: i32 = 0;
    for (i, x) in input.iter().enumerate() {
        if i == 0 {
            continue;
        }
        if x > &input[i - 1] {
            nr_of_decreases += 1;
        }
    }
    nr_of_decreases
}

fn how_often_decreases_window(input: Vec<i32>) -> i32 {
    let mut nr_of_decreases: i32 = 0;
    let windows = input.windows(3);
    let sums = windows.map(|x| x.iter().sum()).collect::<Vec<i32>>();
    for (i, x) in sums.iter().enumerate() {
        if i == 0 {
            continue;
        }
        if x > &sums[i - 1] {
            nr_of_decreases += 1;
        }
    }

    return nr_of_decreases
}

fn day01a() -> i32 {
    let content = fs::read_to_string("resources/year2021/day01.txt")
        .expect("Something went wrong reading the file");
    let ints = string_to_ints(&content);
    let x = how_often_decreases(ints);
    x
}

fn day01b() -> i32 {
    let content = fs::read_to_string("resources/year2021/day01.txt")
        .expect("Something went wrong reading the file");
    let ints = string_to_ints(&content);
    let x = how_often_decreases_window(ints);
    x
}

#[test]
fn string_to_ints_simple_parsing() {
    assert_eq!(vec![1, 2, 3], string_to_ints("1\n2\n3\n"));
    assert_eq!(vec![1], string_to_ints("1"));
}

#[test]
fn how_often_decreases_example() {
    assert_eq!(7,how_often_decreases(vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263]));
}

#[test]
fn how_often_decreases_windows_example() {
    assert_eq!(5,how_often_decreases_window(vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263]));
}

#[test]
fn solution_day01() {
    assert_eq!(1532, day01a());
    assert_eq!(1571, day01b());
}
