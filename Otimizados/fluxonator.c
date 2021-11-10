#include <stdio.h>

int posA = -1, posB = -1, posC = -1;

char B() {
    posB *= -1;
    if (posB == 1) return 'D';
    return 'E';
}

char A() {
    posA *= -1;
    if (posA == 1) return 'D';
    return B();
}

char C() {
    posC *= -1;
    if (posC == -1) return 'E';
    return B();
}

int main(void) {
    int N, n;
    scanf("%d", &N);
    getchar();

    for (n = 0; n < N; n++) {
        char chr;
        while (scanf("%c", &chr)) {
            if (chr == 'A') printf("%c", A());
            else if (chr == 'B') printf("%c", B());
            else if (chr == 'C') printf("%c", C());
            else break;
        }
        printf("\n");
        posA = -1;
        posB = -1;
        posC = -1;
    }

    return 0;
}