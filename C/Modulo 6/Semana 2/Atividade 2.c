#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>

void conta()
{
    int i, n;

    printf("Quantos alunos tem na classe? ");
    scanf("%d", &n);

    float s, alunos[n];
    s = 0;

    for (i = 0; i < n; i++)
    {
        printf("Digite a nota do %d° aluno(a): ", i + 1);
        scanf("%f", &alunos[i]);
    }

    for (i = 0; i < n; i++)
    {
        s += alunos[i];
    }

    printf("%f", s / n);

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