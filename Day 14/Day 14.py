import re


def one():
    seconds = 100
    width = 101
    height = 103
    quadrants = [0, 0, 0, 0]
    locations = []
    p = r"\d+|\-\d+"
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            # print(line)
            x = re.findall(p, line)
            x = list(map(int, x))
            x[2] *= seconds
            x[3] *= seconds
            x[0] = (x[0] + x[2]) % width
            x[1] = (x[1] + x[3]) % height

            if x[0] == (width-1)/2 or x[1] == (height-1)/2:
                continue
            elif x[0] < (width - 1) / 2 and x[1] < (height - 1) / 2:
                quadrants[0] += 1
            elif x[0] > (width - 1) / 2 and x[1] < (height - 1) / 2:
                quadrants[1] += 1
            elif x[0] < (width - 1) / 2 and x[1] > (height - 1) / 2:
                quadrants[2] += 1
            else:
                quadrants[3] += 1
        print(quadrants)

    total = 1
    for _ in quadrants:
        total *= _
    print(total)


one()

import re
from functools import reduce
from PIL import Image, ImageDraw
import sys

pattern = "p=(?P<x>-?[0-9]+),(?P<y>-?[0-9]+).+v=(?P<vx>-?[0-9]+),(?P<vy>-?[0-9]+)"


def quadrant(x, y, width, height):
    if x < (width - 1) / 2 and y < (height - 1) / 2:
        return 0
    elif x > (width - 1) / 2 and y < (height - 1) / 2:
        return 1
    elif x < (width - 1) / 2 and y > (height - 1) / 2:
        return 2
    elif x > (width - 1) / 2 and y > (height - 1) / 2:
        return 3
    return 4


def getrobots():
    width = 101
    height = 103
    robots = []
    with open("input.txt", "r") as file:
        for line in file:
            line = line.strip()
            match = re.search(pattern, line)
            x, y, vx, vy = int(match.group("x")), int(match.group("y")), \
                           int(match.group("vx")), int(match.group("vy"))
            robots.append((x, y, vx, vy))

    return robots, width, height


def simulate(robots, width, height, seconds):
    return [((x + vx * seconds) % width, (y + vy * seconds) % height) for (x, y, vx, vy) in robots]


def bitmap(robots, width, height):
    bitmap = [0 for _ in range(width * height)]
    for x, y in robots:
        bitmap[x + y * width] = 255
    return bitmap


def textnquadrants(robots, width, height, seconds):
    quadrants = [0, 0, 0, 0]
    text = [0 for _ in range(width * height)]
    for x, y in simulate(robots, width, height, seconds):
        quad = quadrant(x, y, width, height)
        if quad < 4:
            quadrants[quad] += 1
        text[x + y * width] += 1
    return quadrants, text


def one(robots, width, height):
    seconds = 100
    quadrants, text = textnquadrants(robots, width, height, seconds)
    print(quadrants)
    for y in range(height):
        for x in range(width):
            if x == (width - 1) / 2 or y == (height - 1) / 2:
                print('#', end='')
                continue
            print('.' if text[x + y * width] == 0 else text[x + y * width], end='')
        print()

    print(reduce(lambda x, y: x * y, quadrants))


one(*getrobots())


def two(robots, width, height):
    for i in range(10000):
        bmp = bitmap(simulate(robots, width, height, i), width, height)

        with Image.new("L", (width, height), 0) as im:
            # draw = ImageDraw.Draw(im)
            im.putdata(bmp)
            im.save(f"images/{i}.bmp")


two(*getrobots())