import re


def one():
    p = r"\d+"

    total = 0

    for block in open("input.txt").read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(p, block))
        min_score = float("inf")
        for i in range(101):
            for j in range(101):
                if ax * i + bx * j == px and ay * i + by * j == py:
                    min_score = min(min_score, i * 3 + j)
        if min_score != float("inf"):
            total += min_score

    print(total)


one()


def two():
    p = r"\d+"

    total = 0

    for block in open("input.txt").read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(p, block))
        px += 10000000000000
        py += 10000000000000
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)
    print(total)


two()


def one_efficient():
    p = r"\d+"

    total = 0

    for block in open("input.txt").read().split("\n\n"):
        ax, ay, bx, by, px, py = map(int, re.findall(p, block))
        ca = (px * by - py * bx) / (ax * by - ay * bx)
        cb = (px - ax * ca) / bx
        if ca % 1 == cb % 1 == 0:
            total += int(ca * 3 + cb)
    print(total)


one_efficient()
