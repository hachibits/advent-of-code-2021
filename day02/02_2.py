def parse(line):
    cmd, x = line.split()
    return (cmd, int(x))

h = d = a = 0
for cmd, x in [parse(line) for line in open("input")]:
    if cmd == "down":
        a += x
    elif cmd == "up":
        a -= x
    else:
        h += x
        d += a * x

print(h * d)
