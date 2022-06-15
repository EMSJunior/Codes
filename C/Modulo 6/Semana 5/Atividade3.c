#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

int caractercout(int v1, int v2, int v3)
{
    char a[20], b[20], c[20];
    printf("\nTEST: %d %d %d",v1,v2,v3);

    sprintf(a, "%d", v1);
    sprintf(b, "%d", v2);
    sprintf(c, "%d", v3);

    printf("\nTEST2: %s %s %s",a,b,c);
    
    strcat(b, c);
    strcat(a, b);

    printf("\nTEST3: %s",a);

    return (strlen(a));
}

void printlinhas(int n)
{
    int x;
    printf("\n|");
    for (x = 0; x < n + 8; x++)
    {
        printf("-");
    }
    printf("|");
}

int retornarmaior(int a, int b, int c)
{
    if (a >= c && a >= b)
    {
        return (1);
    }
    else if (b >= c && b >= a)
    {
        return (2);
    }
    else
    {
        return (3);
    }
}

void conta()
{
    int x, y, v[3], m[3][3], mm[3][3], nlinha[3], aux;
    char s[20];

    for (x = 0; x < 3; x++)
    {
        printf("Digite o %d° vetor: ", x + 1);
        scanf("%d", &v[x]);
    }
    for (y = 0; y < 3; y++)
    {
        for (x = 0; x < 3; x++)
        {
            printf("Digite o %d° número da matriz: ", x + y + 1);
            scanf("%d", &m[x][y]);
        }
    }

    for (y = 0; y < 3; y++)
    {
        for (x = 0; x < 3; x++)
        {
            mm[x][y] = m[x][y] * v[x];
        }
    }

    for (y = 0; y < 3; y++)
    {
        nlinha[y] = caractercout(mm[1][y], mm[2][y], mm[3][y]);
    }

    aux = retornarmaior(nlinha[1], nlinha[2], nlinha[3]);
    printf("\n aux = %d\nnlinha [1] = %d\nnlinha [2] = %d\nnlinha [3] = %d", aux, nlinha[1], nlinha[2], nlinha[3]);

    switch (aux)
    {
    case 1:
        for (y = 0; y < 3; y++)
        {
            printlinhas(nlinha[aux]);
            printf("\n|");
            for (x = 0; x < 3; x++)
            {
                printf(" %d |", mm[x][y]);
            }
        }
        printlinhas(nlinha[aux]);
        break;
    case 2:
        for (y = 0; y < 3; y++)
        {
            printlinhas(nlinha[aux]);
            printf("\n|");
            for (x = 0; x < 3; x++)
            {
                printf(" %d |", mm[x][y]);
            }
        }
        printlinhas(nlinha[aux]);
        break;
    case 3:
        for (y = 0; y < 3; y++)
        {
            printlinhas(nlinha[aux]);
            printf("\n|");
            for (x = 0; x < 3; x++)
            {
                printf("%d", mm[x][y]);
            }
        }
        printlinhas(nlinha[aux]);
        break;
    default:
        printf("ERRO NO AUX");
        break;
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