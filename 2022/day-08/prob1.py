grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([int(c) for c in line.strip()])

# exterior
num_visible = len(grid) * 2 + (len(grid[0]) - 2) * 2


def visible(i, j):
    h = grid[i][j]
    top = all([grid[ix][j] < h for ix in range(0, i)])
    bottom = all([grid[ix][j] < h for ix in range(i + 1, len(grid))])
    left = all([grid[i][jx] < h for jx in range(0, j)])
    right = all([grid[i][jx] < h for jx in range(j + 1, len(grid[0]))])

    return top or bottom or left or right


# interior
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if visible(i, j):
            num_visible += 1

print(num_visible)
