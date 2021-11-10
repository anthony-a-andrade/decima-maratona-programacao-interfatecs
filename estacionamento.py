placas = ["" for x in range(15)]

def getASCII(letra):
    pos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(letra)
    return pos + 65

while True:
    try:
        placa = input()

        P = 0
        for letra in placa:
            if letra.isdigit(): P = P + int(letra)
            else: P = P + getASCII(letra)

        P = P % 15
        P = int("1" + str(P)) % 15
        P = P - 1
        if placas[P] == "": placas[P] = placa
    except EOFError: break

for i in range(0, 15):
    if placas[i] != "":
        print("%d %s" % (i + 1, placas[i]))
