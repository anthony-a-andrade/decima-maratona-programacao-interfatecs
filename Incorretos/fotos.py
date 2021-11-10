soma = 0
numeros = []

while True:
    entrada = input()
    if entrada == "": break
    N = int(entrada)
    soma = soma + N
    numeros.append(N)

for num in numeros:
    result_ = num / soma
    result = "%.3f" % (num / soma)
    result = [x for x in result]

    if result[4] == '0':
        del result[4]
        if result[3] == '0': del result[3]
    print("".join(result))
