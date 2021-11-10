Nomes = []
PT1 = []
PT2 = []
PT3 = []

PT1_ = []
PT2_ = []
PT3_ = []

while True:
        competidor_ = input()
        if competidor_ == "": break
        competidor = competidor_.split(' ')

        nome = competidor[0]
        t1 = int(competidor[1])
        t2 = int(competidor[2])
        t3 = int(competidor[3])

        Nomes.append(nome)
        PT1.append(t1)
        PT2.append(t2)
        PT3.append(t3)
        PT1_.append(t1)
        PT2_.append(t2)
        PT3_.append(t3)

PT1_.sort()
PT2_.sort()
PT3_.sort()

indexT1_1 = PT1.index(PT1_[0])
indexT1_2 = PT1.index(PT1_[1])
indexT1_3 = PT1.index(PT1_[2])

indexT2_1 = PT2.index(PT2_[0])
indexT2_2 = PT2.index(PT2_[1])
indexT2_3 = PT2.index(PT2_[2])

indexT3_1 = PT3.index(PT3_[0])
indexT3_2 = PT3.index(PT3_[1])
indexT3_3 = PT3.index(PT3_[2])
print("T1 %s %s %s" % (Nomes[indexT1_1], Nomes[indexT1_2], Nomes[indexT1_3]))
print("T2 %s %s %s" % (Nomes[indexT2_1], Nomes[indexT2_2], Nomes[indexT2_3]))
print("CHEGADA %s %s %s" % (Nomes[indexT3_1], Nomes[indexT3_2], Nomes[indexT3_3]))
print("")