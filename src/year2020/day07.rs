use std::fs;
use regex::Regex;
use std::collections::HashMap;
use rayon::prelude::*;

const TARGET_COLOR: &str = "shiny gold";

#[derive(Eq, PartialEq, Debug)]
struct Bag {
    color: String,
    can_contain_color: Vec<(String, u8)>,
}

impl Bag {
    pub fn new(input: String) -> Bag {
        lazy_static! {
            static ref MATCH_SUB_COLOR: Regex = Regex::new(r"(\d) (.+) bag").unwrap();
        }
        let splitted: Vec<&str> = input.split(" bags contain ").collect();
        let color = splitted[0].to_string();
        let rest = splitted[1];
        if rest == "no other bags." {
            return Bag { color, can_contain_color: vec![] };
        }
        let can_contain_color: Vec<(String, u8)> = rest.split(", ").map(|l| {
            let byr_cap = MATCH_SUB_COLOR.captures(l).unwrap();
            ((&byr_cap[2]).to_string(), (&byr_cap[1]).parse::<u8>().unwrap())
        }
        ).collect();
        Bag { color, can_contain_color }
    }
}

fn prepare_input(input: String) -> (Vec<Bag>, HashMap<String, Vec<(String, u8)>>) {
    let bags: Vec<Bag> = input.lines().map(|l| Bag::new(l.to_string())).collect();
    let mut book_reviews: HashMap<String, Vec<(String, u8)>> = HashMap::new();
    for b in &bags {
        book_reviews.insert(
            b.color.to_string(), b.can_contain_color.to_vec(),
        );
    }
    (bags, book_reviews)
}

fn has_shiny(color: String, look_up: HashMap<String, Vec<(String, u8)>>) -> bool {
    let child_colors: &Vec<(String, u8)> = look_up.get(&color).unwrap();
    let colors: Vec<String> = child_colors.par_iter().map(|x| x.0.to_string()).collect();
    if colors.contains(&TARGET_COLOR.to_string()) { return true; }
    let matches: Vec<String> = colors.par_iter().filter(|c| *c == TARGET_COLOR || has_shiny(c.to_string(), look_up.clone()))
        .map(|x| x.to_string())
        .collect();
    matches.len() >= 1
}

fn part_1(input: String) -> usize {
    let (bags, book_reviews) = prepare_input(input);
    bags.par_iter().filter(|b| {
        has_shiny((&b).color.to_string(), book_reviews.clone())
    }).count()
}

fn sum_sub_colors(my_color: (String, u8), look_up: HashMap<String, Vec<(String, u8)>>) -> usize {
    let sub_colors = look_up.get(&my_color.0).unwrap(); //blue, yellow
    if sub_colors.is_empty(){
        return 1
    }
    1 + sub_colors.iter().fold(0usize, |agg, sc| agg + sc.1 as usize * sum_sub_colors(sc.clone(), look_up.clone()))
}

fn part_2(input: String) -> usize {
    let (bags, book_reviews) = prepare_input(input);
    let shiny_bag = bags.iter().find(|b|b.color == TARGET_COLOR).unwrap();
    sum_sub_colors((shiny_bag.color.to_string(), 1), book_reviews.clone()) -1
}

// Long running, disabling test execution
#[allow(dead_code)]
fn day07a() -> usize {
    let content = fs::read_to_string("resources/year2020/day07.txt")
        .expect("Something went wrong reading the file");
    part_1(content)
}

fn day07b() -> usize {
    let content = fs::read_to_string("resources/year2020/day07.txt")
        .expect("Something went wrong reading the file");
    part_2(content)
}

#[test]
fn bag_new_test() {
    let input = "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.".to_string();
    let expected = Bag { color: "vibrant plum".to_string(), can_contain_color: vec![("faded blue".to_string(), 5), ("dotted black".to_string(), 6)] };
    assert_eq!(expected, Bag::new(input));
}

#[test]
fn has_shiny_test() {
    let mut map = HashMap::new();
    map.insert("blue".to_string(), vec![("red".to_string(), 1), ("yellow".to_string(), 1)]);
    map.insert("red".to_string(), vec![("green".to_string(), 1)]);
    map.insert("yellow".to_string(), vec![("purple".to_string(), 1)]);
    map.insert("purple".to_string(), vec![("shiny gold".to_string(), 1)]);
    map.insert("green".to_string(), vec![]);
    assert_eq!(true, has_shiny("blue".to_string(), map))
}

#[test]
fn part_test() {
    let input = "light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.".to_string();
    assert_eq!(4, part_1(input));
}

#[test]
fn part_2_test() {
    let input = "light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.".to_string();
    assert_eq!(32, part_2(input));

    let input_2 = "shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.".to_string();
    assert_eq!(126, part_2(input_2));
}

#[test]
fn solution_day07() {
    // assert_eq!(335, day07a());
    assert_eq!(2431, day07b());
}
