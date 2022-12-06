n_cols = 0
state = []


def parse_move(s):
    s_arr = s.split(" ")
    els = []

    for si in s_arr:
        try:
            els.append(int(si))
        except:
            continue

    return els


num_containing = 0
with open("input.txt", "r") as f:
    initial_crates = []
    for line in f:
        line = line.strip("\n")
        if line.strip() == "":
            n_cols = max(map(lambda c: int(c) if c != "" else 0,
                         initial_crates[-1].split(" ")))
            initial_crates.pop(-1)
            break
        initial_crates.append(line)
        print(line)

    state = [[] for _ in range(n_cols)]
    print(state)

    for crate_row in initial_crates:
        for i, c in enumerate(crate_row):
            idx = i - 1
            if idx % 4 == 0 and c != " ":
                d_idx = idx // 4
                state[d_idx].append(c)

    for line in f:
        n, i, j = parse_move(line)
        tmp = []
        for _ in range(n):
            tmp.append(state[i - 1].pop(0))
        state[j - 1] = tmp + state[j - 1]


print([c[0] for c in state])
