use std::fs;

fn checksum_by_min_max(input: Vec<i32>) -> i32 {
    input.iter().max().unwrap() - input.iter().min().unwrap()
}

fn checksum_by_dividable(input: Vec<i32>) -> i32 {
    let vec = input.clone();
    for i in &vec {
        for j in &input {
            if i == j {
                continue;
            }
            if i % j == 0 {
                return i / j;
            } else if j % i == 0 {
                return j / i;
            }
        }
    }
    0
}

fn checksum(input: String, f: &dyn Fn(Vec<i32>) -> i32) -> i32 {
    input
        .lines()
        .map(|l|
            l.split('\t')
                .filter(|c| !c.is_empty())
                .map(|x| x.parse::<i32>().unwrap())
                .collect())
        .fold(0i32, |acc, ints| acc + f(ints))
}

fn day02a() -> i32 {
    let content = fs::read_to_string("resources/year2017/day02.txt")
        .expect("Something went wrong reading the file");
    checksum(content, &checksum_by_min_max)
}

fn day02b() -> i32 {
    let content = fs::read_to_string("resources/year2017/day02.txt")
        .expect("Something went wrong reading the file");
    checksum(content, &checksum_by_dividable)
}

#[test]
fn checksum_examples() {
    assert_eq!(8, checksum_by_min_max(vec![5, 1, 9, 5]));
    assert_eq!(4, checksum_by_min_max(vec![7, 5, 3]));
    assert_eq!(6, checksum_by_min_max(vec![2, 4, 6, 8]));

    assert_eq!(4, checksum_by_dividable(vec![5, 9, 2, 8]));
    assert_eq!(3, checksum_by_dividable(vec![9, 4, 7, 3]));
    assert_eq!(2, checksum_by_dividable(vec![3, 8, 6, 5]));
}

#[test]
fn solution_day02() {
    assert_eq!(47136, day02a());
    assert_eq!(250, day02b());
}
