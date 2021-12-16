lines = [[int(i) for i in x.strip()] for x in open("input")]
gamma = epsilon = ""
for bin in zip(*lines):
    g = round(sum(bin) / len(bin))
    e = 1 - g
    gamma += str(g)
    epsilon += str(e)

print(int(gamma, 2) * int(epsilon, 2))
