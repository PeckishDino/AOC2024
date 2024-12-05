def one():
    count = 0
    with open("input.txt", "r") as file:
        word_search = [line.strip() for line in file.readlines()]

    length = len(word_search)
    directions = (0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)
    print(directions)

    for i, x in enumerate(word_search):
        for j, y in enumerate(x):
            if y == "X":
                print("Found X at index", i, j)
                for di, dj in directions:
                    if 0 <= i + 3 * di < length and 0 <= j + 3 * dj < length and \
                            word_search[i + di][j + dj] == "M" and \
                            word_search[i + 2 * di][j + 2 * dj] == "A" and \
                            word_search[i + 3 * di][j + 3 * dj] == "S":
                        print("Found XMAS")
                        count += 1
    print("found", count, "christmases", "meow")


one()


def two():
    count = 0

    with open("input.txt", "r") as file:
        word_search = [line.strip() for line in file.readlines()]
        print(word_search)
        length = len(word_search)
        print(length)
        directions = (1, 1), (1, -1), (-1, -1), (-1, 1)

        for i, x in enumerate(word_search):
            for j, y in enumerate(x):

                if y == "A":
                    mas_found = 0

                    print(y, "found at index:", i, j)

                    try:
                        for di, dj in directions:
                            if 0 <= i + di < length and 0 <= j + dj < length:
                                if word_search[i + di][j + dj] == "S":
                                    if word_search[i - di][j - dj] == "M":
                                        mas_found += 1
                                if word_search[i + di][j + dj] == "M":
                                    if word_search[i - di][j - dj] == "S":
                                        mas_found += 1
                        if mas_found == 4:
                            count += 1
                    except:
                        print("error")
    print(count)


two()
