#include <stdio.h>

int main(void) {
    int X;
    scanf("%d", &X);

    int base, mult = 0, m;
    for (m = 1; m < X; m += 4)
        mult += 2;

    base = mult + 1;

    if (base + mult == X) printf("%d\n", mult * (X - 2));
    else if (base + mult == X + 2) printf("%d\n", mult * X);

    return 0;
}