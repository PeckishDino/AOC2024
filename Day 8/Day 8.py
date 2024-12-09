def one():
    map = []
    antennas = set()
    f = read_file("input.txt")
    #print(f)
    for _ in f:
        map.append(_.strip())
    #print(map)
    width = len(map)
    height = len(map[0])
    antinodes = []

    for _ in map:
        for __ in _:
            if __ != ".":
                antennas.add(__)
    #print(antennas)

    for _ in antennas:
        coords = []
        for i, __ in enumerate(map):
            index = __.find(_)
            if index != -1:
                #print(_, "found at index", i, index)
                coords.append((i, index))

        print(coords)
        for _ in coords:
            for i in range(len(coords)):
                if _ != coords[i]:
                    #print(_, coords[i])
                    x = _[0]-coords[i][0]
                    y = _[-1]-coords[i][-1]
                    #print("distance:",x,y)
                    antinode_coords = (_[0] - (2*x), _[-1] - (2*y))
                    #print(antinode_coords)
                    if 0 <= antinode_coords[0] < width:
                        if 0 <= antinode_coords[-1] < height:
                            antinodes.append(antinode_coords)
    #print(antinodes)
    print(len(set(antinodes)))



def read_file(file):
    with open(file, "r") as f:
        return f.readlines()


one()
