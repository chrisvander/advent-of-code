def char_to_priority(c):
    v = ord(c)
    if v < 97:
        return v - ord('A') + 27
    return v - ord('a') + 1


priority_sum = 0
with open("input.txt", "r") as f:
    lines = []
    for line in f.readlines():
        lines.append(line.strip())
        if len(lines) < 3:
            continue

        l1, l2, l3 = lines
        l1, l2, l3 = set(l1), set(l2), set(l3)
        in_all = l1.intersection(l2).intersection(l3)

        priorities = list(map(char_to_priority, in_all))
        priority_sum += sum(priorities)

        lines = []


print(priority_sum)
