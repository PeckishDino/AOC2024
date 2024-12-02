def one():
    sum=0
    left=[]
    right=[]
    with open("input.txt","r") as file:
        for line in file:
            x = line.strip().split()
            left.append(x[0])
            right.append(x[-1])
    left.sort()
    right.sort()
    for x in range(len(left)):
        sum+=abs(int(left[x])-int(right[x]))
    print(sum)


def two():
    sum=0
    left=[]
    right=[]
    with open("input.txt", "r") as file:
        for line in file:
            x = line.strip().split()
            left.append(x[0])
            right.append(x[-1])
    left.sort()
    right.sort()
    for x in range(len(left)):
        similarity = right.count(left[x])
        sum+=(int(left[x])*similarity)
    print(sum)


one()
two()