of_interest = [20, 60, 100, 140, 180, 220]
v = 1
cycle = 0
cycle_to_val: list[int] = [v]

f = open("input.txt", "r")
for line in f.readlines():
    lspl = line.strip().split(" ")
    op = lspl[0]
    if op == "noop":
        cycle_to_val.append(v)
        cycle += 1
        continue
    n = int(lspl[1])
    cycle_to_val.append(v)
    cycle_to_val.append(v)
    cycle += 2
    v = v + n

print(sum([c * cycle_to_val[c] for c in of_interest]))
