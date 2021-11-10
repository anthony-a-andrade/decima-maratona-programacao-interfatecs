#include <stdio.h>

int main(void) {
    int X, Y;
    scanf("%d %d", &X, &Y);
    getchar();

    if (X >= 1 && X <= 100 && Y >= 1 && Y <= 100 && X != Y) {
        printf("%d %d\n", X, Y);
        printf("%d %d\n", Y, X);
        printf("%d %d\n", Y, -X);
        printf("%d %d\n", X, -Y);
        printf("%d %d\n", -X, -Y);
        printf("%d %d\n", -Y, -X);
        printf("%d %d\n", -Y, X);
        printf("%d %d\n", -X, Y);
    } else printf("ERRO\n");

    return 0;
}