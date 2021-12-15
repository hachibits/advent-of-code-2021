def parse(ls):
    return "".join(str(l) for l in ls)

nums = [str(line.strip()) for line in open("input")]
gamma = epsilon = list() 
for bin in nums:
    map = dict(zip(['0', '1'], [0 for _ in range(2)]))
    for x in list(bin):
        map[x] += 1
    gamma.append(1), epsilon.append(0) if map['1'] > map['0'] else gamma.append(0), epsilon.append(1)
print(int(parse(gamma), 2) * int(parse(epsilon), 2))
