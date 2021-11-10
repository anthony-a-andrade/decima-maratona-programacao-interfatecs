X = int(input())

base = 1
mult = 0
for m in range(1, X, 4):
    mult = mult + 2
    base = mult + 1

if base + mult == X: print(mult * (X - 2))
elif base + mult == X + 2: print(mult * X)
