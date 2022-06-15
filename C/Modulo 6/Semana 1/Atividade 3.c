#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

int escolha(n){
    switch(n){
        case 1:
            printf("\nO dia referente é Domingo");
            break;
        case 2:
            printf("\nO dia referente é Segunda");
            break;
        case 3:
            printf("\nO dia referente é Terça");
            break;
        case 4:
            printf("\nO dia referente é Quarta");
            break;
        case 5:
            printf("\nO dia referente é Quinta");
            break;
        case 6:
            printf("\nO dia referente é Sextou BB");
            break;
        case 7:
            printf("\nO dia referente é Sabado");
            break;
        default:
            printf("\nNúmero errado !!!"); system("color 4");
        return(0);
    }
}

void conta(){
    int n;

    printf("\nNúmero referente: ");
    scanf("%d",&n);

    escolha(n);

    return(0);
    }

void car(){
     int i;
        system("cls");
        printf("Obrigado por utilizar!\nSaindo ");

        for(i=0;i<10;i++)
        {
            Sleep(100);
            printf(".");
        }
}

void main(){setlocale(LC_ALL,"portuguese");
    char aux;

    printf("---------------------------------------------------\nOlá, seja bem vindo !\n---------------------------------------------------");
    while (1)
    {
        conta();

        printf("\nColocar outro número (s/n)? ");
        scanf("%s",&aux);

        if (aux == 'n')
        {
            car();
            break;
        }
    }

}
