#!/bin/bash

set -exo pipefail
if [ -z "$1" ]; then
    echo "Run with ./create_day.sh 2021/04"
fi
echo "Creating $1"
arrIN=(${1//\// })
year=${arrIN[0]}
day=${arrIN[1]}
echo $year
echo $day

mkdir -p "src/year${year}"
mkdir -p "test-resources/year${year}"
touch "resources/year${year}/day${day}.txt"

cat <<EOT >>src/year${year}/day${day}.rs
use std::fs;

fn day${day}a() -> usize {
    let content = fs::read_to_string("resources/year${year}/day${day}.txt")
        .expect("Something went wrong reading the file");
    let input = content
        .split("\n")
        .filter(|x| *x != "")
        .collect::<Vec<&str>>();
}

fn day${day}b() -> usize {
    let content = fs::read_to_string("resources/year${year}/day${day}.txt")
        .expect("Something went wrong reading the file");
    let input = content
        .split("\n")
        .filter(|x| *x != "")
        .collect::<Vec<&str>>();
}

#[test]
fn solution_day${day}() {
    // assert_eq!(-1, day${day}a());
    // assert_eq!(-1, day${day}b());
}

EOT
