entrada = input().split(' ')
X = int(entrada[0])
Y = int(entrada[1])

if X >= 1 and X <= 100 and Y >= 1 and Y <= 100 and X != Y:
    print("%d %d" % (X, Y))
    print("%d %d" % (Y, X))
    print("%d %d" % (Y, -X))
    print("%d %d" % (X, -Y))
    print("%d %d" % (-X, -Y))
    print("%d %d" % (-Y, -X))
    print("%d %d" % (-Y, X))
    print("%d %d" % (-X, Y))
else: print("ERRO")
