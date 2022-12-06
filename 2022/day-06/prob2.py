def process_input():
    with open("input.txt", "r") as f:
        line = f.readline()
        backlog = []
        for i, c in enumerate(line):
            backlog.append(c)
            if len(backlog) < 14:
                continue

            if len(set(backlog)) == 14:
                return i + 1

            backlog.pop(0)


print(process_input())
