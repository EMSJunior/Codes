#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

struct dados
{
    char nome[50], funcao[50];
    int idade;
    float salario[3];
};

void conta()
{
    int i;
    struct dados dados;

    printf("Nome: ");
    fgets(dados.nome, 50, stdin);

    printf("Função: ");
    fgets(dados.funcao, 50, stdin);

    printf("Idade: ");
    scanf("%d",&dados.idade);

    printf("Ultimos 3 salarios: ");
    for (i = 0; i < 3; i++)
    {
        printf("\n%d° salário: ",i+1);
        scanf("%f",&dados.salario[i]);
    }

    system("cls");
    printf("----- FICHA FUNCIONÁRIO -----\n\nNome: %sFunção: %sIdade: %d\nÚltimos salários:\n1° - R$%.2f\n2° - R$%.2f\n3° - R$%.2f\n",dados.nome,dados.funcao,dados.idade,dados.salario[1],dados.salario[2],dados.salario[3]);
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