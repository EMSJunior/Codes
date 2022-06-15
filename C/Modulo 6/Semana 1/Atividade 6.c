#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

void prod(int c)
{
    int q;

    switch (c)
    {
    case (100):
        printf("Cachorro Quente --> R$ 1,20\nQantidade: ");
        scanf("%d", &q);
        printf("\nProduto: Cachorro Quente\nQuantidade: %d\nPreço: R$ %.2f",q, (1.20*q));
        break;
    case (101):
        printf("Coxinha --> R$ 1,30\nQantidade: ");
        scanf("%d", &q);
        printf("\nProduto: Coxinha\nQuantidade: %d\nPreço: R$ %.2f",q, (1.30*q));
        break;
    case (102):
        printf("Coxinha com catupiry --> R$ 1,50\nQantidade: ");
        scanf("%d", &q);
        printf("\nProduto: Coxinha com catupiry\nQuantidade: %d\nPreço: R$ %.2f",q, (1.50*q));
        break;
    case (103):
        printf("Refrigerante --> R$ 1,20\nQantidade: ");
        scanf("%d", &q);
        printf("\nProduto: Refrigerante\nQuantidade: %d\nPreço: R$ %.2f",q, (1.20*q));
        break;
    case (104):
        printf("Suco --> R$ 1,30\nQantidade: ");
        scanf("%d", &q);
        printf("\nProduto: Suco\nQuantidade: %d\nPreço: R$ %.2f",q, (1.30*q));
        break;
    default:
        printf("\nCódigo inválido !!!");
        system("color 4");
        break;
    }
}

void conta()
{
    int c;

    printf("Codigo: ");
    scanf("%d", &c);

    prod(c);

    return (0);
}

void car()
{
    int i;
    system("cls");
    printf("Obrigado por utilizar!\nSaindo ");
    for (i = 0; i < 10; i++)
    {
        Sleep(100);
        printf(".");
    }
}

void main()
{
    setlocale(LC_ALL, "portuguese");
    char aux;

    printf("---------------------------------------------------\nOlá, seja bem vindo !\n---------------------------------------------------\n");
    while (1)
    {
        conta();

        printf("\nColocar outro número (s/n)? ");
        scanf("%s", &aux);
        system("color 7");

        if (aux == 'n')
        {
            car();
            break;
        }
    }
}