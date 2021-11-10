def obterLigacoes(Ligacoes, Portas, portaFinal):
    for ligacao in Ligacoes:
        for porta in Portas[ligacao - 1]:
            if porta not in Ligacoes:
                Ligacoes.append(porta)

entrada = input().split(' ')
Comodos = int(entrada[0])
Refens = int(entrada[1])
Saida = int(entrada[2])

qntTerroristas = int(input())
posTerroristas = [int(x) for x in input().split(' ')]

qntLigacoes = int(input())
Portas = [[] for x in range(Comodos)]
for i in range(qntLigacoes):
    ligacao = input().split(' ')
    porta1 = int(ligacao[0])
    porta2 = int(ligacao[1])

    if porta1 not in posTerroristas and porta2 not in posTerroristas:
        Portas[porta1 - 1].append(porta2)
        Portas[porta2 - 1].append(porta1)

Ligacoes = [Refens]
obterLigacoes(Ligacoes, Portas, Saida)
if Saida in Ligacoes: print("PROSSEGUIR")
else: print("ABORTAR")
