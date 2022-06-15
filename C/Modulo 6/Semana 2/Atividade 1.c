#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

void conta()
{
    int i, j, aux, lista[10];

    for (i = 0; i < 10; i++)
    {
        printf("Digite a nota: ");
        scanf("%d", &lista[i]);
    }
    for (i = 0; i < 10; i++)
    {
        for (j = i + 1; j < 10; j++)
        {
            if (lista[i] > lista[j])
            {
                aux = lista[i];
                lista[i] = lista[j];
                lista[j] = aux;
            }
        }
    }

    printf("Números ordenados: ");

    for (i = 0; i < 10; i++)
    {
        printf("%d, ", lista[i]);
    }
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