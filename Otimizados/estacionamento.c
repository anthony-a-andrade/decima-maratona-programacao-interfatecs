#include <stdio.h>
#include <string.h>
#include <math.h>

int getASCII(char chr) {
    int result = chr - '0';
    if (result <= 9) return result;
    return result + 18;
}

int concat1(int P) {
    int digitos = 1;
    if (P != 0) digitos = (int)log10(P) + 1;
    return pow(10, digitos) + P;
}

int main(void) {
    char placas[15][8] = { '\0' }, placa[7];
    int i;

    while (scanf("%s", placa) != EOF) {
        int P = 0;
        for (i = 0; i < 7; i++)
            P += getASCII(placa[i]);

        P = (concat1(P % 15) % 15) - 1;
        if (P < 0) P += 15;

        if (placas[P][0] == '\0') {
            strcpy(placas[P], placa);
            placas[P][7] = '\0';
        }
    }

    for (i = 0; i < 15; i++)
        if (placas[i][0] != '\0')
            printf("%d %s\n", i + 1, placas[i]);

    return 0;
}