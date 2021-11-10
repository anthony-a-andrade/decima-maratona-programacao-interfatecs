posA = -1
posB = -1
posC = -1

N = int(input())
for n in range(N):
    entrada = input()
    for letra in entrada:
        if letra == 'A':
            if posA == -1: print("D", end='')
            else:
                if posB == -1: print("D", end='')
                else: print("E", end='')
                posB = posB * -1
            posA = posA * -1
        elif letra == 'B':
            if posB == -1: print("D", end='')
            else: print("E", end='')
            posB = posB * -1
        else:
            if posC == 1: print("E", end='')
            else:
                if posB == 1: print("E", end='')
                else: print("D", end='')
                posB = posB * -1
            posC = posC * -1
    print("")
    posA = -1
    posB = -1
    posC = -1
