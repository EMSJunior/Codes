#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

void dia(int n)
    {
    switch(n)
        {
            case 1:
                printf("\nUm");
                break;
            case 2:
                printf("\nDois");
                break;
            case 3:
                printf("\nTrês");
                break;
            case 4:
                printf("\nQuatro");
                break;
            case 5:
                printf("\nCinco");
                break;
            case 6:
                printf("\nSeis");
                break;
            case 7:
                printf("\nSete");
                break;
            case 8:
                printf("\nOito");
                break;
            case 9:
                printf("\nNove");
                break;
            case 10:
                printf("\nDez");
                break;
            default:
                printf("\nNúmero Inválido !!!");
        }
    }
void conta()
    {
    int n;

    printf("Digite o número: ");
    scanf("%d",&n);

    dia(n);

    return(0);
    }

void car()
{
    int i;
        system("cls");
        printf("Obrigado por utilizar!\nSaindo ");
        for(i=0;i<10;i++)
        {
            Sleep(100);
            printf(".");
        }
}

void main()
{
    setlocale(LC_ALL,"portuguese");
    char aux;

    printf("---------------------------------------------------\nOlá, seja bem vindo !\n---------------------------------------------------\n");
    while (1)
    {
        conta();

        printf("\nColocar outro número (s/n)? ");
        scanf("%s",&aux);
        system("color 7");

        if (aux == 'n')
        {
            car();
            break;
        }
        }
}