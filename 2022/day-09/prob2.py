knots = [(0, 0) for _ in range(10)]
visited_by_tail = set([(0, 0)])

move = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


def touching(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) <= 1 and abs(y1-y2) <= 1


def sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    return 0


f = open("input.txt", "r")
for line in f.readlines():
    d, n = line.strip().split(" ")
    n = int(n)
    m = move[d]
    for step in range(n):
        dx, dy = m
        x, y = knots[0]
        knots[0] = (x + dx, y + dy)
        for i in range(1, len(knots)):
            if not touching(knots[i - 1], knots[i]):
                x, y = knots[i - 1]
                ox, oy = knots[i]
                knots[i] = (ox + sign(x - ox), oy + sign(y - oy))

        visited_by_tail.add(knots[-1])

print(len(visited_by_tail))
