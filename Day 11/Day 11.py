def one():
    with open("input.txt","r") as file:
        file = file.readlines()
    blinks = 25
    string = file[0]
    print(string)
    file = string.split()
    print(file)
    stones = []

    for x in range(blinks):
        print(x)
        stones.clear()
        for _ in file:
            if int(_) == 0:
                stones.append(1)
            elif len(str(_)) % 2 == 0:
                stones.append(int(str(_)[:int(len(str(_))/2)]))
                stones.append(int(str(_)[int(len(str(_))/2):]))
            else:
                stones.append((int(_)*2024))
        file.clear()
        file.extend(stones)
    print(stones)
    print(len(stones))

one()