
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

        loss = t == 1
        draw = t == 2
        win = t == 3

        chosen = (m + t) % 3 + 1

        print(chosen)

        if win:
            score += chosen + 6
        if draw:
            score += chosen + 3
        if loss:
            score += chosen


print(score)
