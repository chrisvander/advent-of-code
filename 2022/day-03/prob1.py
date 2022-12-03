def char_to_priority(c):
    v = ord(c)
    if v < 97:
        return v - ord('A') + 27
    return v - ord('a') + 1


priority_sum = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        p1, p2 = line[:int(len(line) / 2)], line[int(len(line) / 2):]
        p1, p2 = set(p1), set(p2)
        in_both = p1.intersection(p2)

        priorities = list(map(char_to_priority, in_both))
        priority_sum += sum(priorities)


print(priority_sum)
