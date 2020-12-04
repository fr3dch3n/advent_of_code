use std::fs;
use regex::Regex;

fn passports_have_necessary_fields(input: String) -> Vec<String> {
    let necessary_fields = vec![
        "byr".to_string(),
        "iyr".to_string(),
        "eyr".to_string(),
        "hgt".to_string(),
        "hcl".to_string(),
        "ecl".to_string(),
        "pid".to_string()];

    input.split("\n\n").filter(|l|
        necessary_fields.iter().filter(|f| l.contains(*f)).count() == 7
    ).map(|x| String::from(x)).collect()
}

fn validate_byr(input: &str) -> bool {
    lazy_static! {
        static ref RE_BYR: Regex = Regex::new(r".*byr:(\d{0,4}).*").unwrap();
    }
    let byr_cap = RE_BYR.captures(&input).unwrap();
    let byr_val: &str = &byr_cap[1];
    let byr_int = byr_val.parse::<i32>().unwrap();
    byr_int >= 1920 && byr_int <= 2002
}

fn validate_iyr(input: &str) -> bool {
    lazy_static! {
        static ref RE_IYR: Regex = Regex::new(r".*iyr:(\d{0,4}).*").unwrap();
    }
    let iyr_cap = RE_IYR.captures(&input).unwrap();
    let iyr_val: &str = &iyr_cap[1];
    let iyr_int = iyr_val.parse::<i32>().unwrap();
    iyr_int >= 2010 && iyr_int <= 2020
}

fn validate_eyr(input: &str) -> bool {
    lazy_static! {
        static ref RE_EYR: Regex = Regex::new(r".*eyr:(\d{0,4}).*").unwrap();
    }
    let eyr_cap = RE_EYR.captures(&input).unwrap();
    let eyr_val: &str = &eyr_cap[1];
    let eyr_int = eyr_val.parse::<i32>().unwrap();
    eyr_int >= 2020 && eyr_int <= 2030
}

fn validate_hgt(input: &str) -> bool {
    lazy_static! {
        static ref RE_HGT: Regex = Regex::new(r".*hgt:(\d+)([a-z]{0,4}).*").unwrap();
    }
    let hgt_cap = RE_HGT.captures(&input).unwrap();
    let hgt_val: &str = &hgt_cap[1];
    let hgt_kind: &str = &hgt_cap[2];
    let hgt_int = hgt_val.parse::<i32>().unwrap();
    (hgt_kind == "cm" && hgt_int >= 150 && hgt_int <= 193)
        || (hgt_kind == "in" && hgt_int >= 59 && hgt_int <= 76)
}

fn validate_hcl(input: &str) -> bool {
    lazy_static! {
        static ref RE_HCL: Regex = Regex::new(r".*hcl:#[0-9a-f]{6}.*").unwrap();
    }
    RE_HCL.is_match(&input)
}

fn validate_ecl(input: &str) -> bool {
    lazy_static! {
        static ref RE_ECL: Regex = Regex::new(r".*ecl:([a-z]{0,3}).*").unwrap();
    }
    let ecl_cap = RE_ECL.captures(&input).unwrap();
    let ecl_val: &str = &ecl_cap[1];
    let allowed: Vec<String> = vec!["amb".to_string(), "blu".to_string(), "brn".to_string(), "gry".to_string(), "grn".to_string(), "hzl".to_string(), "oth".to_string()];
    allowed.iter().filter(|a| a == &ecl_val).count() == 1
}

fn validate_pid(input: &str) -> bool {
    lazy_static! {
        static ref RE_PID: Regex = Regex::new(r".*pid:([\d]+).*").unwrap();
    }
    let ecl_cap = RE_PID.captures(&input);
    match ecl_cap {
        Some(result) => result[1].len() == 9,
        None => false
    }
}

fn fields_are_valid(input: Vec<String>) -> Vec<String> {
    input.iter().filter(|p|
        validate_byr(p) &&
            validate_iyr(p) &&
            validate_eyr(p) &&
            validate_hgt(p) &&
            validate_hcl(p) &&
            validate_ecl(p) &&
            validate_pid(p)
    ).map(|x| x.to_string()).collect()
}


fn day04a() -> usize {
    let content = fs::read_to_string("resources/year2020/day04.txt")
        .expect("Something went wrong reading the file");
    passports_have_necessary_fields(content).len()
}

fn day04b() -> usize {
    let content = fs::read_to_string("resources/year2020/day04.txt")
        .expect("Something went wrong reading the file");
    let passports = passports_have_necessary_fields(content);
    fields_are_valid(passports).len()
}

#[test]
fn validate_byr_test() {
    assert!(validate_byr("byr:2002"));
    assert!(!validate_byr("byr:2003"))
}

#[test]
fn validate_hgt_test() {
    assert!(validate_hgt("hgt:60in"));
    assert!(validate_hgt("hgt:190cm"));
    assert!(!validate_hgt("hgt:190in"));
    assert!(!validate_hgt("hgt:190"));
}

#[test]
fn validate_hcl_test() {
    assert!(validate_hcl("hcl:#123abc"));
    assert!(!validate_hcl("hcl:#123abz"));
    assert!(!validate_hcl("hcl:123abc"));
}

#[test]
fn validate_ecl_test() {
    assert!(validate_ecl("ecl:brn"));
    assert!(!validate_ecl("ecl:wat"));
}

#[test]
fn validate_pid_test() {
    assert!(validate_pid("pid:000000001"));
    assert!(!validate_pid("pid:0123456789"));
}

#[test]
fn valid_passports_example() {
    let input = "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in";
    assert_eq!(2, passports_have_necessary_fields(String::from(input)).len())
}

#[test]
fn real_valid_examples() {
    let invalid_passports = "eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007".to_string();

    let invalid_passports_with_fields = passports_have_necessary_fields(invalid_passports);
    assert_eq!(0, fields_are_valid(invalid_passports_with_fields).len());

    let valid_passports = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719".to_string();

    let valid_passports_with_fields = passports_have_necessary_fields(valid_passports);
    assert_eq!(4, fields_are_valid(valid_passports_with_fields).len());
}

#[test]
fn solution_day04() {
    assert_eq!(260, day04a());
    assert_eq!(153, day04b());
}
