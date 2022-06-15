#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

void conta()
{
    int i, j, aux, a[8],b[8];

    for (i = 0; i < 8; i++)
    {
        printf("Digite o %d° valor : ",i+1);
        scanf("%d", &a[i]);
    }
    for (i = 0; i < 8; i++)
    {
        b[i] = a[i];
    }
    for (i = 0; i < 8; i++)
    {
        for (j = i + 1; j < 8; j++)
        {
            if (b[i] < b[j])
            {
                aux = b[i];
                b[i] = b[j];
                b[j] = aux;
            }
        }
    }

    printf("Números ordenados decrecentemente: ");

    for (i = 0; i < 7; i++)
    {
        printf("%d, ", b[i]);
    }
    printf("%d.",b[8]);
}

void load()
{
    int i;

    for (i = 0; i < 11; i++)
    {
        Sleep(10);
        system("cls");
        printf("Obrigado por utilizar!\nSaindo ");
        printf("(%d%%)", i * 10);
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
            load();
            break;
        }
    }
}