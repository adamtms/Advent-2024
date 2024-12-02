#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <unordered_map>

std::vector<std::vector<int> > readFile() {
    std::ifstream inputFile;
    inputFile.open("input.txt");
    std::string text;
    std::vector<int> left;
    std::vector<int> right;
    while ( inputFile.is_open() ) {
        inputFile >> text;
        left.insert(left.begin(), std::stoi(text));
        inputFile >> text;
        right.insert(right.begin(), std::stoi(text));
        if (inputFile.eof()) {
            break;
        }
    }
    inputFile.close();
    std::vector<std::vector<int> > output;
    output.insert(output.begin(), left);
    output.insert(output.begin(), right);
    return output;
}

void task1() {
    std::vector<std::vector<int> > data = readFile();
    std::vector<int> left = data.at(0);
    std::vector<int> right = data.at(1);
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());
    int sum = 0;
    for (int i=0; i<left.size(); i++) {
        sum += abs(left.at(i) - right.at(i));
    }
    std::cout << sum << std::endl;
}

void task2() {
    std::vector<std::vector<int> > data = readFile();
    std::vector<int> left = data.at(0);
    std::vector<int> right = data.at(1);
    std::unordered_map<int, int> counter;
    int times;
    int element;
    for (int i=0; i<right.size(); i++) {
        element = right.at(i);
        std::unordered_map<int,int>::const_iterator found = counter.find(element);
        if (found == counter.end()) {
            counter[element] = 1;
        } else {
            counter[element] = found->second + 1;
        }
    }
    int sum = 0;
    for (int i=0; i<left.size(); i++) {
        element = left.at(i);
        std::unordered_map<int,int>::const_iterator found = counter.find(element);
        if (found != counter.end()) {
            sum += element * found->second;
        }
    }
    std::cout << sum << std::endl;
}

int main() {
    task1();
    task2();
}