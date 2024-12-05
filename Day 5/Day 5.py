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


one()
