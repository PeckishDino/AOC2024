from collections import Counter


def one():
    rules = []
    order = []
    count = 0

    with open("input.txt", "r") as file:
        for line in file:
            if "|" in line:
                rules.append(line.strip().replace("|", " "))

            if "," in line:
                order.append(line.strip())
        for x in order:
            correct_order = 0
            x = x.split(",")
            length = len(x)
            for i, a in enumerate(x):
                if i < length - 1:
                    for y in rules:
                        y = y.split()
                        if x[i] == y[0] and x[i + 1] == y[-1]:
                            correct_order += 1
                    if correct_order == length - 1:
                        middle = int((length - 1) / 2)
                        count += int(x[middle])

    print(count)


# one()

def two():
    rules, order, pages, count = [], [], [], 0

    with open("input.txt", "r") as file:
        for line in file:
            if "|" in line:
                rules.append(line.strip().replace("|", " "))

            elif "," in line:
                order.append(line.strip())
    for x in order:
        correct_order = 0
        x = x.split(",")
        length = len(x)
        for i, a in enumerate(x):
            if i < length - 1:
                for y in rules:
                    y = y.split()
                    if x[i] == y[0] and x[i + 1] == y[-1]:
                        correct_order += 1
        if correct_order != length - 1:
            pages.append(x)

    counts = Counter(tuple(page) for page in pages)
    incorrect_order = [page for page in pages if counts[tuple(page)] != len(page) - 2]
    unique_order = [list(t) for t in set(tuple(page) for page in incorrect_order)]

    for x in unique_order:
        h = 0
        while h < len(x):
            for y in rules:
                y = y.split()
                if y[-1] in x:
                    right_number_index = x.index(y[-1])
                    if y[0] in x:
                        left_number_index = x.index(y[0])
                        if left_number_index > right_number_index:
                            x.insert(left_number_index, x.pop(right_number_index))
            h += 1
        middle_number = x[int((len(x) - 1) / 2)]
        count += int(middle_number)
    print(count)


two()
