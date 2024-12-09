def readfile(file):
    with open(file,"r") as f:
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
    #print(string_list)
    length = len(string_list)
    #print(length)
    z = length - 1
    while z > 0 and "." in string_list:
            closest_dot = string_list.index(".")
            if string_list[z] == ".":
                string_list.pop(z)
            else:
                string_list[closest_dot] = string_list.pop(z)
            z -= 1
            #print(string_list)


    for i,_ in enumerate(string_list):
        if _ != ".":
            sum += i*_
    print("sum:",sum)
one()