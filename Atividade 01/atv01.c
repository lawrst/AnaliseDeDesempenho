#include <stdio.h>

int Primo(int n){
    if (n <= 1) return 0;

    for (int i = 2; i * i <= n; i++){
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int main (){
    int numero, verificacao, total = 0;

    printf("Digite um valor maior que zero: ");
    verificacao = scanf("%d", &numero);

    if (verificacao == 0){
        printf("Erro! Digite um número!\n");
        return 1;
    }

    if (numero <= 0){
        printf("Erro! Digite um número maior que 0!\n");
        return 1;
    }

    printf("Valor fornecido: %d\n", numero);
    printf("Primos encontrados: ");

    for(int i = 1; i <= numero; i++){
        if(Primo(i)){
            printf("%d-", i);
            total++;
        }
    }

    printf("\nA quantidade de números primos: %d\n", total);

    return 0;
}