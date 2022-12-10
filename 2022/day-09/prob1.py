head, tail = ((0, 0), (0, 0))
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


f = open("input.txt", "r")
for line in f.readlines():
    d, n = line.strip().split(" ")
    n = int(n)
    m = move[d]
    for step in range(n):
        dx, dy = m
        x, y = head
        head = (x + dx, y + dy)
        if not touching(head, tail):
            tail = (x, y)
            visited_by_tail.add(tail)

print(len(visited_by_tail))
