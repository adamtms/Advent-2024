from collections import Counter

def read_file():
    left = []
    right = []
    with open("input.txt") as f:
        for line in f:
            l, r = line.split()
            left.append(int(l))
            right.append(int(r))
    return left, right

def main_1():
    left, right = read_file()
    left.sort()
    right.sort()
    summ = 0
    for l, r in zip(left, right):
        summ += abs(l - r)
    print(summ)

def main_2():
    left, right = read_file()
    right = Counter(right)
    summ = 0
    for element in left:
        summ += element * right.get(element, 0)
    print(summ)
    
if __name__ == "__main__":
    main_1()
    main_2()