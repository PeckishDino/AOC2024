def parse(file):
    global left, right
    left,right = [],[]
    with open(file, "r") as f:
        for line in f:
            x = line.strip().split()
            left.append(x[0])
            right.append(x[-1])
    left.sort()
    right.sort()


def one():
    sum = 0
    parse("input.txt")
    for x in range(len(left)):
        sum += abs(int(left[x]) - int(right[x]))
    print(sum)


def two():
    sum = 0
    parse("input.txt")
    for x in range(len(left)):
        similarity = right.count(left[x])
        sum += (int(left[x]) * similarity)
    print(sum)


one()
two()
