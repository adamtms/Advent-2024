from collections import defaultdict, deque

def load_file():
    rules = defaultdict(list)
    orderings = []
    mode = 'rules'
    with open('input.txt') as f:
        for line in f.readlines():
            if line.strip() == "":
                mode = 'orderings'
                continue
            if mode == 'rules':
                before, after = line.strip().split('|')
                rules[before].append(after)
            else:
                orderings.append(line.strip().split(","))
    return rules, orderings


def check_ordering(ordering, rules):
    for i, before in enumerate(ordering[:-1]):
        for after in ordering[i+1:]:
            if before in rules[after]:
                return False
    return True


def task_1():
    rules, orderings = load_file()
    summ = 0
    for ordering in orderings:
        if check_ordering(ordering, rules):
            summ += int(ordering[len(ordering)//2])
    print(summ)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)


def build_tree(rules):
    nodes = {}
    for before, afters in rules.items():
        if before not in nodes:
            nodes[before] = Node(before)
        for after in afters:
            if after not in nodes:
                nodes[after] = Node(after)
            nodes[before].add_child(nodes[after])
    return nodes


def topological_sort(nodes):
    parents = {node: 0 for node in nodes.keys()}
    for node in nodes.values():
        for child in node.children:
            if child.value not in parents:
                continue
            parents[child.value] += 1
    sorted_nodes = [node for node, count in parents.items() if count == 0]
    queue = deque(sorted_nodes)
    while queue:
        node = queue.popleft()
        for child in nodes[node].children:
            if child.value not in parents:
                continue
            parents[child.value] -= 1
            if parents[child.value] == 0:
                queue.append(child.value)
                sorted_nodes.append(child.value)
    return sorted_nodes


def test_topological_sort():
    rules, orderings = load_file()
    nodes = build_tree(rules)
    for ordering in orderings:
        sorted_nodes = topological_sort({val: node for val, node in nodes.items() if val in ordering})
        for i, node in enumerate(sorted_nodes):
            if node != ordering[i]:
                print("Failed")
                break
    

def task_2():
    rules, orderings = load_file()
    nodes = build_tree(rules)
    summ = 0
    for ordering in orderings:
        if not check_ordering(ordering, rules):
            ordering = topological_sort({val: node for val, node in nodes.items() if val in ordering})
            summ += int(ordering[len(ordering)//2])
    print(summ)


if __name__ == '__main__':
    task_1()
    task_2()