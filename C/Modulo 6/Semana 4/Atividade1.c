#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

void conta()
{
    int a[5], b[5], i;

    for (i = 0; i <= 4; i++)
    {
        printf("Digite o %d° valor de A: ", i+1);
        scanf("%d", &a[i]);
    }

    for (i = 0; i <= 4; i++)
    {
        b[i] = a[i];
    }
    printf("\nOs valores de B são: \n");
    for (i = 0; i <= 4; i++)
    {
        printf("%d° valor: %d\n", i+1, b[i]);
    }
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