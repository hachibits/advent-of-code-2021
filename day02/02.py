map = dict(zip(["forward", "up", "down"], [0 for _ in range(3)]))

for line in open("input"):
    cmd, x = line.split()
    map[cmd] += int(x)

print(map["forward"]*(map["down"]-map["up"]))
