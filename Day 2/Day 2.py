def one():
    valid_levels = 0
    with open("input.txt", "r") as file:
        for line in file:
            status = None
            levels = line.split()
            length = len(levels)
            ascend_or_descend = int(levels[0]) - int(levels[1])  # if the initial 2 values are ascending, descending,
            # or no difference.
            if ascend_or_descend > 0:
                status = True
            if ascend_or_descend < 0:
                status = False
            for x in range(length):
                if x + 1 == length:  # if it reaches the end of the level aka reads every number
                    valid_levels += 1
                    break
                ascend_or_descend2 = int(levels[x]) - int(levels[x + 1])
                if status is False and ascend_or_descend2 > 0 or status is True and ascend_or_descend2 < 0 or status is None or abs(
                        ascend_or_descend2) < 1 or abs(ascend_or_descend2) > 3:
                    break  # breaks if the increment is 0, or it switches from ascend to descend or vice versa

        print(valid_levels)


def two():
    valid_levels = 0
    with open("input.txt", "r") as file:
        for line in file:
            valid_levels2 = 0
            status = None
            for y in range(len(line.strip().split())):
                levels = line.strip().split()
                levels.pop(y)
                length = len(levels)
                ascend_or_descend = int(levels[0]) - int(
                    levels[1])  # if the initial 2 values are ascending, descending,
                # or no difference.
                if ascend_or_descend > 0:
                    status = True
                if ascend_or_descend < 0:
                    status = False
                for x in range(length):
                    if x + 1 == length:  # if it reaches the end of the level aka reads every number
                        valid_levels2 += 1
                        break
                    ascend_or_descend2 = int(levels[x]) - int(levels[x + 1])
                    if (status is False and ascend_or_descend2 > 0) \
                            or (status is True and ascend_or_descend2 < 0) \
                            or status is None \
                            or abs(ascend_or_descend2) < 1 or abs(ascend_or_descend2) > 3:
                        break  # breaks if the increment is 0, or it switches from ascend to descend or vice versa
            if valid_levels2 > 0:
                valid_levels += 1

        print(valid_levels)


one()
two()
