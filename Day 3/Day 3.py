import re


def one():
    sum = 0
    p = r"mul\(\d+,\d+\)"
    with open("input.txt", "r") as file:
        for line in file:
            x = re.findall(p, line)
            for y in x:
                nums = re.findall(r"\d+", y)
                sum += int(nums[0]) * int(nums[-1])
    print(sum)

def two():
    sum = 0
    status = True
    p = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    with open("input.txt", "r") as file:
        for line in file:
            x = re.findall(p, line)
            print(x)
            for y in x:
                if y == "don't()":
                    status = False
                elif y == "do()":
                    status = True
                elif status is True:
                    nums = re.findall(r"\d+", y)
                    sum += int(nums[0]) * int(nums[-1])
    print(sum)

one()
two()