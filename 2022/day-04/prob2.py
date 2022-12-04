def get_bounds(pair):
    n1, n2 = pair.split("-")
    return int(n1), int(n2)


num_containing = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        p1, p2 = line.split(',')
        b1, b2 = get_bounds(p1), get_bounds(p2)
        if (b1[1] <= b2[1] and b1[1] >= b2[0]) \
           or (b1[0] <= b2[1] and b1[0] >= b2[0]) \
           or (b1[0] <= b2[0] and b1[1] >= b2[1]) \
           or (b1[0] >= b2[0] and b1[1] <= b2[1]):
            num_containing += 1

print(num_containing)
