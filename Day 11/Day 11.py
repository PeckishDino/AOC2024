def one():
    blinks = 25
    stones = [int(x) for x in open("input.txt").read().split()]

    for _ in range(blinks):
        output = []
        for stone in stones:
            string = str(stone)
            length = len(string)
            if stone == 0:
                output.append(1)
            elif length % 2 == 0:
                output.append(int(string[:length // 2]))
                output.append(int(string[length // 2:]))
            else:
                output.append(stone * 2024)
        stones = output
    print(len(stones))


one()

from functools import cache

stones = [int(x) for x in open("input.txt").read().split()]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)
    return count(stone * 2024, steps - 1)

print(sum(count(stone, 75) for stone in stones))



