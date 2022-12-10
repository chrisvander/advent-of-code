grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([int(c) for c in line.strip()])


def scenic_score_direction(i, j, di, dj):
    h = grid[i][j]
    i += di
    j += dj
    score = 1
    while i < len(grid) - 1 and j < len(grid[0]) - 1 and i > 0 and j > 0:
        if grid[i][j] >= h:
            break
        score += 1
        i += di
        j += dj

    return score


def scenic_score(i, j):
    top = scenic_score_direction(i, j, 1, 0)
    bottom = scenic_score_direction(i, j, -1, 0)
    left = scenic_score_direction(i, j, 0, -1)
    right = scenic_score_direction(i, j, 0, 1)

    return top * bottom * left * right


max_scenic = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        max_scenic = max(max_scenic, scenic_score(i, j))

print(max_scenic)
