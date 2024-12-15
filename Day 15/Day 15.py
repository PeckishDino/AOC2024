grid = []
movements = None


def parse(file):
    global movements
    with open(file, "r") as f:
        for line in f:
            grid.append(line.strip())
        movements = grid.pop(-1)
        grid.pop(-1)
        print(grid)
        print(movements)


def grid_movement():
    directions_dict = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if y == "@":
                print("index of robot starting location:", i, j)
                start = [i, j]
    print(start)

    for char in movements:



def main():
    parse("input.txt")
    grid_movement()


main()
