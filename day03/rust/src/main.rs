use std::fs;
use regex::Regex;

fn read_file() -> String {
    fs::read_to_string("../input.txt")
        .expect("Should have been able to read the file")
}

fn task_1() {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
    let file = read_file();
    let mut sum: i64 = 0;
    for found in re.captures_iter(&file) {
        let (_, [first, second]) = found.extract();
        sum += first.parse::<i64>().unwrap() * second.parse::<i64>().unwrap();
    }
    println!("{}", sum);
}

fn task_2() {
    let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))").unwrap();
    let file = read_file();
    let mut enabled = true;
    let mut sum: i64 = 0;
    for found in re.captures_iter(&file) {
        let mut iterator = found.iter();
        let _ = iterator.next();
        let first = iterator.next().unwrap();
        let second = iterator.next().unwrap();
        let do_ = iterator.next().unwrap();
        let dont = iterator.next().unwrap();

        let do_ = match do_ {
            Some(_) => true,
            None => false
        };
        let dont = match dont {
            Some(_) => true,
            None => false
        };

        if do_ {
            enabled = true;
        } else if dont {
            enabled = false;
        } else if enabled{
            let first = first.unwrap().as_str();
            let second = second.unwrap().as_str();
            sum += first.parse::<i64>().unwrap() * second.parse::<i64>().unwrap();
        }
    }
    println!("{}", sum);
}

fn main() {
    task_1();
    task_2();
}
