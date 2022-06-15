#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

void conta()
{
    int i, j, n[3][3];

    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
        {
            printf("Digite o %d° número: ",i+j+1);
            scanf("%d",&n[i][j]);
        }

    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
        {
            printf("\n%d° termo(%d) * 5 =%d",n+j+1,n[i][j],n[i][j]*5);
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