nums = [int(x) for x in open("input").readline().strip().split(",")]
boards = [
    [[int(c) for c in r.split()] for r in mat.splitlines()]
    for mat in open("input").read().strip().split("\n")[1:]
]

def solve():
    for n in nums: 
        for b in boards:
            for i, row in enumerate(b):
                for j, cell in enumerate(row):
                    if cell == n:
                        b[i][j] == "X"
            
            for row in b:
                #print(sum(cell == "X" for cell in row))
                if sum(cell == "X" for cell in row) == 5:
                    score = sum(cell != "X" for cell in row for row in b)
                    return score * n

            for col in zip(*b):
                if sum(cell == "X" for cell in col) == 5:
                    score = sum(cell != "X" for cell in row for row in b)
                    return score * n

if __name__ == "__main__":
    print(solve())
