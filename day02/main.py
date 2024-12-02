from typing import Literal


def load_data():
    with open("input.txt") as f:
        data = [[int(element) for element in line.split()] for line in f.readlines()]
    return data


def is_diff_correct(diff, direction):
    if direction == "increasing" and not (1 <= diff <= 3):
        return False
    elif direction == "decreasing" and not (-1 >= diff >= -3):
        return False
    return True

def task_1():
    data = load_data()
    counter = 0
    for line in data:
        line = iter(line)
        current_val = next(line)
        direction: Literal["increasing", "decreasing", "unknown"] = "unknown"
        for next_val in line:
            diff = current_val - next_val
            if diff == 0:
                break
            if direction == "unknown":
                direction = "increasing" if diff > 0 else "decreasing"
            if not is_diff_correct(diff, direction):
                break
            current_val = next_val
        else:
            counter += 1
    print(counter)



def task_2():
    data = load_data()
    counter = 0
    for line in data:
        is_safe = False
        to_check = [(line, "increasing", False), (line, "decreasing", False)]
        while to_check:
            line, direction, is_copied = to_check.pop()
            diffs = (a-b for a, b in zip(line, line[1:]))
            for i, diff in enumerate(diffs):
                if is_diff_correct(diff, direction):
                    continue
                j = i + 1
                if is_copied:
                    break
                line_copy = line.copy()
                line_copy.pop(i)
                to_check.append((line_copy, direction, True))
                line_copy = line.copy()
                line_copy.pop(j)
                to_check.append((line_copy, direction, True))
                break
            else:
                is_safe = True
        counter += is_safe
    print(counter)


if __name__ == "__main__":
    task_1()
    task_2()