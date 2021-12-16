lines = [x.strip() for x in open("input")]
lines2 = lines[:]

N = len(lines[0])

for i in range(N):
    x = round(0.001 + sum(int(l[i]) for l in lines) / len(lines))
    lines = [l for l in lines if int(l[i]) == x]
    if len(lines) == 1:
        break

for i in range(N):
    x = 1 - round(0.001 + sum(int(l[i]) for l in lines2) / len(lines2))
    lines2 = [l for l in lines2 if int(l[i]) == x]
    if len(lines2) == 1:
        break

print(int(lines[0], 2) * int(lines2[0], 2))
