use std::fs;

fn solve_captcha(seq: String, step_size: usize) -> u32 {
    let chars: Vec<char> = seq.chars().collect();
    seq.chars().enumerate().fold(0u32, |acc, (i, c)|
        if c == chars[(i + step_size) % seq.len()] {
            acc + c.to_digit(10).unwrap()
        } else {
            acc
        },
    )
}

fn day01a() -> u32 {
    let content = fs::read_to_string("resources/year2017/day01.txt")
        .expect("Something went wrong reading the file");
    solve_captcha(content, 1)
}

fn day01b() -> u32 {
    let content = fs::read_to_string("resources/year2017/day01.txt")
        .expect("Something went wrong reading the file");
    let step_size = content.len() / 2;
    solve_captcha(content, step_size)
}

#[test]
fn solve_captcha_examples() {
    assert_eq!(3, solve_captcha(String::from("1122"), 1));
    assert_eq!(4, solve_captcha(String::from("1111"), 1));
    assert_eq!(0, solve_captcha(String::from("1234"), 1));
    assert_eq!(9, solve_captcha(String::from("91212129"), 1));

    assert_eq!(6, solve_captcha(String::from("1212"), 2));
    assert_eq!(0, solve_captcha(String::from("1221"), 2));
    assert_eq!(4, solve_captcha(String::from("123425"), 3));
    assert_eq!(12, solve_captcha(String::from("123123"), 3));
    assert_eq!(4, solve_captcha(String::from("12131415"), 4));
}

#[test]
fn solution_day01() {
    assert_eq!(1136, day01a());
    assert_eq!(1092, day01b());
}
