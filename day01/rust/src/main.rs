use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn load_file() -> [Vec<i64>; 2] {
    let mut left = vec![];
    let mut right = vec![];
    let path = Path::new("../input.txt");
    let file = File::open(&path).expect("Unable to open file");

    for line in io::BufReader::new(file).lines() {
        let line = line.expect("Unable to read line");
        let numbers: Vec<i64> = line.split_whitespace()
                                    .map(|s| s.parse::<i64>().unwrap()).collect();
        left.push(numbers[0]);
        right.push(numbers[1]);
    }

    [left, right]
}

fn task_1() {
    let [mut left, mut right] = load_file();
    left.sort();
    right.sort();
    let mut sum = 0;
    for (l, r) in left.iter().zip(right.iter()) {
        sum += (l - r).abs();
    }
    println!("{}", sum);
}

fn task_2() {
    let [left, right] = load_file();
    let mut right_hashmap: HashMap<i64, i64> = HashMap::new();
    for num in right.iter() {
        if let Some(i) = right_hashmap.get(num) {
            right_hashmap.insert(*num, i+1);
        } else {
            right_hashmap.insert(*num, 1);
        }
    }
    let mut sum = 0;
    for num in left.iter() {
        if let Some(i) = right_hashmap.get(num) {
            sum += num * i
        }
    }
    println!("{}", sum);
}

fn main() {
    task_1();
    task_2();
}
