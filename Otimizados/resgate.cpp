#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

bool contains(vector<int> vec, int item) {
    return find(vec.begin(), vec.end(), item) != vec.end();
}

bool possivelProsseguir(vector<int> Ligacoes, vector<vector<int>> Portas, int portaFinal) {
    int i, j;
    for (i = 0; i < Ligacoes.size(); i++) {
        int ligacao = Ligacoes[i];
        for (j = 0; j < Portas[ligacao - 1].size(); j++) {
            int porta = Portas[ligacao - 1][j];
            if (!contains(Ligacoes, porta)) Ligacoes.push_back(porta);
            if (porta == portaFinal) return true;
        }
    }
    return false;
}

int main() {
    int C, R, S, c;
    scanf("%d %d %d", &C, &R, &S);
    getchar();

    int qntT, t;
    scanf("%d", &qntT);
    getchar();

    vector<int> posT;
    for (t = 0; t < qntT; t++) {
        int pos;
        scanf(" %d", &pos);
        getchar();
        posT.push_back(pos);
    }

    int qntL, l;
    scanf("%d", &qntL);
    getchar();

    vector<vector<int>> Portas;
    for (c = 0; c < C; c++) {
        vector<int> tmp;
        Portas.push_back(tmp);
    }

    for (l = 0; l < qntL; l++) {
        int p1, p2;
        scanf("%d %d", &p1, &p2);
        getchar();

        if (!contains(posT, p1) && !contains(posT, p2)) {
            Portas[p1 - 1].push_back(p2);
            Portas[p2 - 1].push_back(p1);
        }
    }

    vector<int> Ligacoes;
    Ligacoes.push_back(R);

    if (possivelProsseguir(Ligacoes, Portas, S)) printf("PROSSEGUIR\n");
    else printf("ABORTAR\n");
    return 0;
}