#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

void conta()
{
    int q, i, j, i50, i21;
    i50 = 0;
    i21 = 0;

    while (1)
    {
        printf("Idade: ");
        scanf("%d", &i);
        if (i == 0)
            break;
        if (i > 50)
        {
            i50++;
        }
        if (i < 21)
        {
            i21++;
        }
    }
    printf("\nMenores de 21 são %d pessoas.\nMaoires de 50 são %d pessoas.", i21, i50);

    return (0);
}

void load()
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
            load();
            break;
        }
    }
}