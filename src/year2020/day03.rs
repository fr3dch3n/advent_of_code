use std::fs;

struct Line {
    row: String
}

struct StepSize {
    x: usize,
    y: usize,
}

impl Line {
    fn move_to(&self, pos: usize) -> char {
        let length = self.row.len();
        if pos >= length {
            self.move_to(pos - length)
        } else {
            return self.row.chars().nth(pos).unwrap();
        }
    }
}

fn walk_forest(input: Vec<&str>, step_size: StepSize) -> u64 {
    let mut x_pos: usize = 0;
    let mut trees = 0;
    let nr_of_lines = input.len();

    for x in ((step_size.y - 1)..nr_of_lines).step_by(step_size.y) {
        x_pos += step_size.x;
        let line = Line { row: input.get(x).unwrap().to_string() };
        if line.move_to(x_pos) == '#' {
            trees += 1;
        }
    }
    trees
}

fn walk_forest_different_steps(input: Vec<&str>, step_sizes: Vec<StepSize>) -> u64 {
    step_sizes
        .iter()
        .fold(1u64, |agg, val|
            agg * walk_forest(input.clone(), StepSize { x: val.x, y: val.y }))
}

fn step_part_a() -> StepSize {
    StepSize { x: 3, y: 1 }
}

fn day03a() -> u64 {
    let content = fs::read_to_string("resources/year2020/day03.txt")
        .expect("Something went wrong reading the file");
    let input = content.lines().skip(1).collect();
    walk_forest(input, step_part_a())
}

fn steps_part_b() -> Vec<StepSize> {
    vec![StepSize { x: 1, y: 1 }, StepSize { x: 3, y: 1 }, StepSize { x: 5, y: 1 }, StepSize { x: 7, y: 1 }, StepSize { x: 1, y: 2 }]
}

fn day03b() -> u64 {
    let content = fs::read_to_string("resources/year2020/day03.txt")
        .expect("Something went wrong reading the file");
    let input = content.lines().skip(1).collect();
    walk_forest_different_steps(input, steps_part_b())
}

#[test]
fn walk_forest_example() {
    let input = String::from("..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#");
    let vec: Vec<&str> = input.lines().skip(1).collect();
    assert_eq!(7, walk_forest(vec, step_part_a()))
}

#[test]
fn walk_forest_different_steps_example() {
    let input = String::from("..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#");
    let vec: Vec<&str> = input.lines().skip(1).collect();
    assert_eq!(336, walk_forest_different_steps(vec, steps_part_b()))
}


#[test]
fn move_to_simple_tests() {
    let line = Line { row: String::from("123") };
    assert_eq!('1', line.move_to(3));
    assert_eq!('2', line.move_to(1));
    assert_eq!('3', line.move_to(5));
}

#[test]
fn solution_day03() {
    assert_eq!(234, day03a());
    assert_eq!(5813773056, day03b());
}
