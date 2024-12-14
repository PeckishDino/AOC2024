import re

pattern = r"mul\(\d+,\d+\)"
pattern2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
d = []
y = []


def parse(file):
    with open(file, "r") as f:
        d.extend([line for line in f])
    return d


def read_line(entry):
    for x in entry:
        y.extend(re.findall(pattern, x))
    return y

def read_line2(entry):
    for x in entry:
        y.extend(re.findall(pattern2, x))
    return y


def iterate_through(values):
    sum = 0
    print(values)
    for x in values:
        nums = re.findall(r"\d+", x)
        print(nums, nums[0], nums[-1])
        sum += int(nums[0]) * int(nums[-1])
    return sum


def one_functions():
    d.clear()
    y.clear()
    print(iterate_through(read_line(parse("input.txt"))))


one_functions()

def iterate_through2(values):
    sum = 0
    status = True
    for x in values:
        if x == "don't()":
            status = False
        elif x == "do()":
            status = True
        elif status:
            nums = re.findall(r"\d+", x)
            sum += int(nums[0]) * int(nums[-1])
    return sum

def two_functions():
    d.clear()
    y.clear()
    print(iterate_through2(read_line2(parse("input.txt"))))

two_functions()
