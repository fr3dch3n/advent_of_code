use std::fs;

fn sum_groups(lines: Vec<&str>) -> Vec<i32> {
    let res: Vec<&[&str]> = lines.split(|&e| e == "").collect();
    let mut sum_of_groups: Vec<i32> = res
        .iter()
        .map(|f| f.iter().map(|s| s.parse::<i32>().unwrap()).sum())
        .collect();
    sum_of_groups.sort();
    sum_of_groups.reverse();
    return sum_of_groups;
}
fn day01a() -> usize {
    let content = fs::read_to_string("resources/year2022/day01.txt")
        .expect("Something went wrong reading the file");
    let input = content.split("\n").collect::<Vec<&str>>();
    return sum_groups(input).first().unwrap().clone() as usize;
}

fn day01b() -> usize {
    let content = fs::read_to_string("resources/year2022/day01.txt")
        .expect("Something went wrong reading the file");
    let input = content.split("\n").collect::<Vec<&str>>();
    return sum_groups(input).iter().take(3).sum::<i32>() as usize;
}

#[test]
fn test_sum_groups() {
    let input = vec!["123", "456", "789", "", "123", "456", "789", "987"];
    assert_eq!(vec![2355, 1368], sum_groups(input))
}

#[test]
fn solution_day01() {
    assert_eq!(74711, day01a());
    assert_eq!(209481, day01b());
}
