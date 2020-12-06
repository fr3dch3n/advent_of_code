extern crate crypto;

use std::fs;

use crypto::md5::Md5;
use crypto::digest::Digest;


fn md5_hash_with_x_zeros(salt: String, needed_zeros: usize) -> u64 {
    let mut hasher = Md5::new();
    let zeros = "0".repeat(needed_zeros);
    for number in 1.. {
        hasher.input(salt.as_bytes());
        hasher.input(number.to_string().as_bytes());
        if hasher.result_str().starts_with(&zeros) {
            return number;
        }
        hasher.reset();
    }
    0 // Should not happen
}

fn day04a() -> u64 {
    let content = fs::read_to_string("resources/year2015/day04.txt")
        .expect("Something went wrong reading the file");
    md5_hash_with_x_zeros(content, 5)
}

fn day04b() -> u64 {
    let content = fs::read_to_string("resources/year2015/day04.txt")
        .expect("Something went wrong reading the file");
    md5_hash_with_x_zeros(content, 6)
}

#[test]
fn md5_hash_with_x_zeros_examples() {
    assert_eq!(609043, md5_hash_with_x_zeros("abcdef".to_string(), 5));
    assert_eq!(1048970, md5_hash_with_x_zeros("pqrstuv".to_string(), 5));
}

#[test]
fn solution_day04() {
    assert_eq!(117946, day04a());
    assert_eq!(3938038, day04b());
}
