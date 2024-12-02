const fs = require('fs');

function load_file() {
    data = fs.readFileSync('input.txt', 'utf8');
    lines = data.split("\n");
    left = [];
    right = [];
    for (i=0; i<lines.length; i++) {
        both = lines.at(i).split("   ");
        left.push(+both.at(0));
        right.push(+both.at(1));
    }
    return [left, right];
}

function task1() {
    let [left, right] = load_file();
    left.sort((a, b) => a-b);
    right.sort((a, b) => a-b);
    let sum = 0;
    for (i=0; i<left.length; i++) {
        sum += Math.abs(left.at(i) - right.at(i));
    }
    console.log(sum);
}

function task2() {
    let [left, right] = load_file();
    let counter = {};
    for (i=0; i<right.length; i++) {
        let number = right.at(i);
        if (number in counter) {
            counter[number] += 1;
        } else {
            counter[number] = 1;
        }
    }
    let sum = 0;
    for (i=0; i<left.length; i++) {
        let number = left.at(i);
        if (number in counter) {
            sum += number * counter[number];
        }
    }
    console.log(sum);
}

task1()
task2()