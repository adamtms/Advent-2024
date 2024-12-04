import re

def read_file():
    with open('input.txt') as f:
        return f.read()


def task_1():
    regex = r'mul\((\d{1,3}),(\d{1,3})\)'
    data = read_file()
    summ = 0
    for left, right in re.findall(regex, data):
        summ += int(left) * int(right)
    print(summ)

def task_2():
    regex = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    data = read_file()
    summ = 0
    enabled = True
    for left, right, do, dont in re.findall(regex, data):
        if do:
            enabled = True
        elif dont:
            enabled = False
        elif enabled:
            summ += int(left) * int(right)
    print(summ)

if __name__ == '__main__':
    task_1()
    task_2()
