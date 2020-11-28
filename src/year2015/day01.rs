use std::fs;

fn count_floor(input: &str) -> i32 {
    let mut count = 0;
    for c in input.chars() {
        match c {
            '(' => count += 1,
            ')' => count -= 1,
            _ => println!("Ain't special"),
        }
    }
    count
}

fn find_basement(input: &str) -> i32 {
    let mut count = 0;
    for (i, c) in input.chars().enumerate() {
        match c {
            '(' => count += 1,
            ')' => count -= 1,
            _ => println!("Ain't special"),
        }
        if count == -1 {
            return i as i32 + 1;
        }
    }
    return -1;
}

fn day01a() -> i32 {
    let content = fs::read_to_string("resources/year2015/day01.txt")
        .expect("Something went wrong reading the file");
    count_floor(&content)
}

fn day01b() -> i32 {
    let content = fs::read_to_string("resources/year2015/day01.txt")
        .expect("Something went wrong reading the file");
    find_basement(&content)
}

#[test]
fn count_floor_examples() {
    assert_eq!(0, count_floor("(())"));
    assert_eq!(0, count_floor("()()"));
    assert_eq!(3, count_floor("((("));
    assert_eq!(3, count_floor("(()(()("));
    assert_eq!(3, count_floor("))((((("));
    assert_eq!(-1, count_floor("())"));
    assert_eq!(-1, count_floor("))("));
    assert_eq!(-3, count_floor(")))"));
    assert_eq!(-3, count_floor(")())())"));
}
#[test]
fn find_basement_examples() {
    assert_eq!(1, find_basement(")"));
    assert_eq!(5, find_basement("()())"));
}
#[test]
fn solution_day01() {
    assert_eq!(280, day01a());
    assert_eq!(1797, day01b());
}
