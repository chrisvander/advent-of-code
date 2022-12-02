max_val, curr_val = None, 0
f = open("input.txt", "r")
for line in f.readlines():
    if line.strip() == "":
        if max_val is None:
            max_val = curr_val
        max_val = max(curr_val, max_val)
        curr_val = 0
    else:
        curr_val += int(line.strip())

print(max_val)
