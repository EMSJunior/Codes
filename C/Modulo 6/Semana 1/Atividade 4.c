#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

void dez(float s)
{
    s=s*1.1;
    printf("Salário = %f",s);
}

void quinze(float s)
{
    s=s*1.15;
    printf("Salário = %f",s);
}

void vinte(float s)
{
    s=s*1.2;
    printf("Salário = %f",s);
}

void conta()
{
    float sala;
    char plano;

    printf("Digite o Salário, depois o plano(separado por espaço): ");
    scanf("%f %s",&sala, &plano);

    switch (plano)
    {
        case 'a' : case 'A' :
            dez(sala);
            break;
        case 'b': case 'B':
            quinze(sala);
            break;
        case 'c' : case 'C':
            vinte(sala);
            break;
        default:
            printf("Plano não registrado !!!");
            system("color 4");

    }

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
{setlocale(LC_ALL,"portuguese");
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