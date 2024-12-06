def one():
    guard_x = 0
    guard_y = 0
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    unique_positions = []
    obstacles = []

    with open("input.txt", "r") as file:
        path = file.readlines()

        for x, line in enumerate(path):
            line = line.strip()
            width = len(line)

            for y, letter in enumerate(line):

                if letter == "#":
                    obstacles.append((y, x))

                elif letter == "^":
                    guard_x = y
                    guard_y = x

        height = len(path)
    while True:

        if guard_x <= 0 or \
                guard_x >= width or \
                guard_y <= 0 or \
                guard_y >= height:
            unique_positions.append((guard_x, guard_y))
            break

        next_x = guard_x + direction[0][0]
        next_y = guard_y + direction[0][-1]

        if (next_x, next_y) in obstacles:
            direction.append(direction.pop(0))

        unique_positions.append((guard_x, guard_y))
        guard_x += direction[0][0]
        guard_y += direction[0][-1]
    unique_positions = set(unique_positions)
    print(len(unique_positions))


one()
