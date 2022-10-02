use std::fs;

fn bit_vec_to_decimal(bit_vec: &Vec<usize>) -> usize {
    let bstr: Vec<String> = bit_vec.iter().map(|x| x.to_string()).collect();
    let bstr_real = bstr.join("");
    usize::from_str_radix(&bstr_real, 2).expect("Not a binary number!")
}

fn find_most_common_bit(bit_vec: &Vec<Vec<usize>>, column_index: usize) -> usize {
    let mut zeros = 0;
    let mut ones = 0;
    for row in bit_vec.clone() {
        if row[column_index] == 0 {
            zeros += 1;
        } else {
            ones += 1;
        }
    }
    if zeros > ones {
        0
    } else {
        1
    }
}

fn filter_by_bit_criteria(
    bit_vec: Vec<Vec<usize>>,
    column_pos: usize,
    filter_fn: fn(&Vec<usize>, usize, usize) -> bool,
) -> Vec<usize> {
    if bit_vec.len() == 1 {
        return bit_vec[0].clone();
    }
    let most_common_bit = find_most_common_bit(&bit_vec, column_pos) as usize;
    let filtered_bit_vec = bit_vec
        .iter()
        .filter(|x| filter_fn(x.clone(), column_pos, most_common_bit))
        .map(|x| x.clone())
        .collect();
    return filter_by_bit_criteria(filtered_bit_vec, column_pos + 1, filter_fn);
}

fn calculate_oxygen_rating(bit_vec: Vec<Vec<usize>>, column_pos: usize) -> Vec<usize> {
    fn filter_fn(x: &Vec<usize>, column_pos: usize, most_common_bit: usize) -> bool {
        x[column_pos] == most_common_bit
    }
    return filter_by_bit_criteria(bit_vec, column_pos, filter_fn);
}

fn calculate_co2_rating(bit_vec: Vec<Vec<usize>>, column_pos: usize) -> Vec<usize> {
    fn filter_fn(x: &Vec<usize>, column_pos: usize, most_common_bit: usize) -> bool {
        x[column_pos] == 1 - most_common_bit
    }
    return filter_by_bit_criteria(bit_vec, column_pos, filter_fn);
}

fn calculate_life_support(input: Vec<&str>) -> usize {
    let two_dim_vector = vec_of_string_to_two_dim_vec(&input);

    let oxygen_rating = calculate_oxygen_rating(two_dim_vector.clone(), 0);
    let co2_rating = calculate_co2_rating(two_dim_vector.clone(), 0);
    bit_vec_to_decimal(&oxygen_rating) * bit_vec_to_decimal(&co2_rating)
}

fn vec_of_string_to_two_dim_vec(input: &Vec<&str>) -> Vec<Vec<usize>> {
    input
        .iter()
        .map(|x| {
            x.chars()
                .map(|c| c.to_digit(10).unwrap() as usize)
                .collect::<Vec<usize>>()
        })
        .collect::<Vec<Vec<usize>>>()
}

fn calculate_power_consumption(input: Vec<&str>) -> usize {
    let two_dim_vector = vec_of_string_to_two_dim_vec(&input);

    let mut gamma_rate_most_common: Vec<usize> = Vec::new();
    let mut epsilon_rate_least_common: Vec<usize> = Vec::new();

    let columns = two_dim_vector[0].len();
    for column_index in 0..columns {
        let most_common_bit = find_most_common_bit(&two_dim_vector, column_index);
        gamma_rate_most_common.push(most_common_bit);
        epsilon_rate_least_common.push(1 - most_common_bit);
    }
    let dec_gamma_rate = bit_vec_to_decimal(&gamma_rate_most_common);
    let dec_epsilon_rate = bit_vec_to_decimal(&epsilon_rate_least_common);
    dec_epsilon_rate * dec_gamma_rate
}

fn day01a() -> usize {
    let content = fs::read_to_string("resources/year2021/day03.txt")
        .expect("Something went wrong reading the file");
    let input = content
        .split("\n")
        .filter(|x| *x != "")
        .collect::<Vec<&str>>();
    calculate_power_consumption(input)
}

fn day01b() -> usize {
    let content = fs::read_to_string("resources/year2021/day03.txt")
        .expect("Something went wrong reading the file");
    let input = content
        .split("\n")
        .filter(|x| *x != "")
        .collect::<Vec<&str>>();
    calculate_life_support(input)
}

#[test]
fn calculate_power_consumption_sample() {
    let sample = [
        "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
        "00010", "01010",
    ]
    .to_vec();
    assert_eq!(198, calculate_power_consumption(sample));
}

#[test]
fn calculate_life_support_sample() {
    let sample = [
        "00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
        "00010", "01010",
    ]
    .to_vec();
    assert_eq!(230, calculate_life_support(sample));
}
#[test]
fn calculate_oxygen_rating_sample() {
    let sample = vec![
        vec![0, 0, 1, 0, 0],
        vec![1, 1, 1, 1, 0],
        vec![1, 0, 1, 1, 0],
        vec![1, 0, 1, 1, 1],
        vec![1, 0, 1, 0, 1],
        vec![0, 1, 1, 1, 1],
        vec![0, 0, 1, 1, 1],
        vec![1, 1, 1, 0, 0],
        vec![1, 0, 0, 0, 0],
        vec![1, 1, 0, 0, 1],
        vec![0, 0, 0, 1, 0],
        vec![0, 1, 0, 1, 0],
    ];
    assert_eq!(vec![1, 0, 1, 1, 1], calculate_oxygen_rating(sample, 0));
}
#[test]
fn solution_day01() {
    assert_eq!(4191876, day01a());
    assert_eq!(3414905, day01b());
}
