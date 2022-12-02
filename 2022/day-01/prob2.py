max_queue = []


def push_to_queue(n):
    max_queue.append(n)
    max_queue.sort(reverse=True)
    if len(max_queue) > 3:
        max_queue.pop(-1)


curr_val = 0
f = open("input.txt", "r")
for line in f.readlines():
    if line.strip() == "":
        push_to_queue(curr_val)
        curr_val = 0
    else:
        curr_val += int(line.strip())

print(sum(max_queue))
