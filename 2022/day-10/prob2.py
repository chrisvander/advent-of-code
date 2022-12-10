of_interest = [20, 60, 100, 140, 180, 220]
v = 1
cycle = 1
cycle_to_val: list[int] = []

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

pixels = [abs(v - (c % 40)) <= 1 for c, v in enumerate(cycle_to_val)]
for i, p in enumerate(pixels):
    print("#" if p else " ", end="")
    if i % 40 == 39:
        print("")
