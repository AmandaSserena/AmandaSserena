#include <stdio.h>

int main() {
    int[] notas = [1, 2, 3];
    float soma = 0;

    for (int i = 0; i < sizeof(notas); i++) {
        soma += notas[i];
    }

    printf("Media %d", soma / sizeof(notas))

    return 0;
}