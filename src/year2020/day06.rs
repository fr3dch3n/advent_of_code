use std::fs;
use std::collections::HashSet;

fn num_of_yes(input: String) -> usize {
    let mut chars: Vec<char> = input.chars().filter(|x| *x != '\n').collect();
    chars.sort();
    chars.dedup();
    chars.len()
}

fn sum_questions_yes(input: String) -> usize {
    input.split("\n\n").map(|s| num_of_yes(s.to_string())).sum()
}

fn yes_to_same_question(input: String) -> usize {
    let hashsets_per_person: Vec<HashSet<char>> = input.split('\n').map(|s| s.chars().collect()).collect();
    hashsets_per_person
        .iter()
        .skip(1)
        .fold(hashsets_per_person[0].clone(), |acc, hs| acc.intersection(hs).copied().collect())
        .len()
}

fn sum_everyone_yes(input: String) -> usize {
    input.split("\n\n").map(|s| yes_to_same_question(s.to_string())).sum()
}

fn day06a() -> usize {
    let content = fs::read_to_string("resources/year2020/day06.txt")
        .expect("Something went wrong reading the file");
    sum_questions_yes(content)
}

fn day06b() -> usize {
    let content = fs::read_to_string("resources/year2020/day06.txt")
        .expect("Something went wrong reading the file");
    sum_everyone_yes(content)
}

#[test]
fn num_of_yes_examples() {
    assert_eq!(3, num_of_yes("abc".to_string()));
    assert_eq!(3, num_of_yes("a\nb\nc".to_string()));
    assert_eq!(3, num_of_yes("ab\nac".to_string()));
    assert_eq!(1, num_of_yes("a\na\na\na".to_string()));
    assert_eq!(1, num_of_yes("b".to_string()));
}

#[test]
fn yes_to_same_question_examples() {
    assert_eq!(3, yes_to_same_question("abc".to_string()));
    assert_eq!(0, yes_to_same_question("a\nb\nc".to_string()));
    assert_eq!(1, yes_to_same_question("ab\nac".to_string()));
    assert_eq!(1, yes_to_same_question("a\na\na\na".to_string()));
    assert_eq!(1, yes_to_same_question("b".to_string()));
}

#[test]
fn sum_questions_yes_example() {
    let input = "abc

a
b
c

ab
ac

a
a
a
a

b";
    assert_eq!(11, sum_questions_yes(input.to_string()));
}

#[test]
fn sum_everyone_yes_example() {
    let input = "abc

a
b
c

ab
ac

a
a
a
a

b";
    assert_eq!(6, sum_everyone_yes(input.to_string()));
}

#[test]
fn solution_day06() {
    assert_eq!(6259, day06a());
    assert_eq!(3178, day06b());
}
