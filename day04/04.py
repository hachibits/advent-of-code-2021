def solve():
    nums = [int(x) for x in open("input").readline().strip().split(",")]
    boards = [
        [[int(c) for c in r.split()] for r in mat.splitlines()]
        for mat in open("input").read().strip().split("\n\n")[1:]
    ]
    for n in nums: 
        for b in boards:
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == n:
                        b[i][j] = "X"
            for row in b:
                if row.count("X") == 5: 
                    score = sum(cell for r in b for cell in r if cell != "X")
                    return score * n
            for col in zip(*b):
                if col.count("X") == 5:
                    score = sum(cell for r in b for cell in r if cell != "X")
                    return score * n

if __name__ == "__main__":
    print(solve())
