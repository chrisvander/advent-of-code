
scores = {
    "A": 1,
    "B": 2,
    "C": 3,

    "X": 1,
    "Y": 2,
    "Z": 3
}


score = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        m, t = line.strip().split(" ")
        m, t = scores[m], scores[t]
        draw = t == m
        win = (t - m) % 3 == 1
        loss = (m - t) % 3 == 1
        if win:
            score += t + 6
        if draw:
            score += t + 3
        if loss:
            score += t


print(score)
