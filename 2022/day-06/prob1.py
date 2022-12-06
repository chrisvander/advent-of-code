def process_input():
    with open("input.txt", "r") as f:
        line = f.readline()
        backlog = []
        for i, c in enumerate(line):
            backlog.append(c)
            if len(backlog) < 4:
                continue

            if len(set(backlog)) == 4:
                return i + 1

            backlog.pop(0)


print(process_input())
