use std::fs;

fn find_first_weakness(input: Vec<usize>, preamble: usize) -> usize {
    for (i, n) in input.iter().enumerate() {
        if i <= preamble { continue }
        let possible_numbers: Vec<usize> = input.clone()[i - preamble.. i].to_vec();
        if !is_the_sum_of(n.clone(), possible_numbers) {
            return n.clone()
        }
    }
    0
}

fn is_the_sum_of(number: usize, possible_numbers: Vec<usize>) -> bool {
    for el1 in possible_numbers.iter() {
        for el2 in possible_numbers.clone().iter() {
            if el1 != el2 && el1 + el2 == number {
                return true
            }
        }
    }
    return false
}

fn day09a() -> usize {
    let content = fs::read_to_string("resources/year2020/day09.txt")
        .expect("Something went wrong reading the file");
    let input: Vec<usize> = content.lines().map(|x| x.parse::<usize>().unwrap()).collect();
    find_first_weakness(input, 25)
}

fn break_encryption(possible_numbers: Vec<usize>, target: usize) -> usize{
    let max_elements = possible_numbers.len() - 1;
    for i in 0..max_elements {
        for j in i..max_elements {
            let mut sub_v = possible_numbers[i..j].to_vec();
            let sum: usize = sub_v.iter().sum();
            if sum == target {
                sub_v.sort();
                return sub_v[0] + sub_v[sub_v.len() - 1]
            }
        }
    }
    return 0
}

fn day09b() -> usize {
    let content = fs::read_to_string("resources/year2020/day09.txt")
        .expect("Something went wrong reading the file");
    let input: Vec<usize> = content.lines().map(|x| x.parse::<usize>().unwrap()).collect();
    break_encryption(input, 756008079)
}

#[test]
fn is_the_sum_of_test() {
    assert!(is_the_sum_of(3, vec![1,2]));
    assert!(!is_the_sum_of(3, vec![2,2]));
    assert!(is_the_sum_of(5, vec![1,2,3,4,5,6]));
    assert!(!is_the_sum_of(2, vec![1,1]));
}

#[test]
fn find_first_weakness_test() {
    let input = vec![35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576];
    assert_eq!(127, find_first_weakness(input, 5));
}

#[test]
fn break_encryption_test() {
    let input = vec![35, 20, 15, 25, 47, 40, 62, 55, 65, 95, 102, 117, 150, 182, 127, 219, 299, 277, 309, 576];
    assert_eq!(62, break_encryption(input, 127));
}

#[test]
fn solution_day09() {
    assert_eq!(756008079, day09a());
    assert_eq!(93727241, day09b());
}
