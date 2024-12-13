def readfile(file):
    with open(file, "r") as f:
        return f.readlines()


def one():
    sum = 0
    string_list = []
    f = readfile("input.txt")
    string = f[0]
    start = 0
    id = 0
    for c in string:
        if (start % 2) == 0:
            for _ in range(int(c)):
                string_list.append(id)
        else:
            for _ in range(int(c)):
                string_list.append(".")
        if string_list[-1] != "." and c != "0":
            id += 1
        start += 1
    print(string_list)
    length = len(string_list)
    # print(length)
    z = length - 1
    while z > 0 and "." in string_list:
        closest_dot = string_list.index(".")
        if string_list[z] == ".":
            string_list.pop(z)
        else:
            string_list[closest_dot] = string_list.pop(z)
        z -= 1
    print(string_list)

    for i, _ in enumerate(string_list):
        if _ != ".":
            sum += i * _
    print("sum:", sum)


#one()


def two():
    ran_through = set()
    sum = 0
    string_list = []
    f = readfile("input.txt")
    string = f[0]
    start = 0
    id = 0
    for c in string:
        if (start % 2) == 0:
            for _ in range(int(c)):
                string_list.append(id)
        else:
            for _ in range(int(c)):
                string_list.append(".")
        if string_list[-1] != "." and c != "0":
            id += 1
        start += 1
    print(string_list)
    length = len(string_list)
    print(length)

    loop1 = True
    closest_dot = string_list.index(".")
    dot_range = 0
    while loop1:
        print("dot index",closest_dot)
        loop2 = True
        dot = 1
        while loop2:
            if string_list[closest_dot + dot] == ".":
                dot += 1
            else:
                print(dot,"dots")
                loop2 = False
        try:
            closest_dot = string_list.index(".",closest_dot + dot)
        except:
            print("no more dots")
            loop1 = False

        z = length - 1
        ran_through.clear()
        print(string_list)
        while z >= 0 and string_list[z] not in ran_through:
            while string_list[z] == ".":
                z -= 1
            # print(string_list)
            print("size",string_list[z])
            ran_through.add(string_list[z])
            repeats = string_list.count(string_list[z])
            print(repeats,"repeats with",dot,"space")
            if repeats <= dot:
                loop3 = True
                for x in range(repeats):
                    print(string_list[closest_dot + x])
                    print(string_list[z-x])
                    string_list[closest_dot + x] = string_list.pop(z-x)
                z -= repeats
                print(string_list)
                break
            else:
                z-=repeats
            print(z)



two()
