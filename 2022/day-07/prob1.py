dir_sizes = {"/": 0}
current_path = ["/"]


def incr_size(dir, size):
    if dir in dir_sizes:
        dir_sizes[dir] += size
    else:
        dir_sizes[dir] = size


with open("input.txt", "r") as f:
    for line in f.readlines():
        if line.startswith("$ cd"):
            cmd = line.strip().split(" ")[-1]
            if cmd == "..":
                current_path.pop(-1)
            elif cmd == "/":
                current_path = ["/"]
            else:
                current_path.append(cmd)
        elif line.startswith("$ ls"):
            continue
        else:
            size, name = line.strip().split(" ")
            if size == "dir":
                continue
            size = int(size)
            for i, _ in enumerate(current_path):
                pth = "/".join(current_path[:i+1])
                incr_size(pth, size)

sm = 0
for v in dir_sizes.values():
    if v <= 100000:
        sm += v

print(sm)
