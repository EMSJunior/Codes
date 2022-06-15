#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

int conta(){
    float nota1, nota2,media;

    printf("\nInforme as notas(separadas por espaço): ");
    scanf("%f %f",&nota1,&nota2);

    media=(nota1+nota2)/2;

    if(media < 3){
        printf("\nMédia= %.2f\n --REPROVADO--",media);
        system("color 4");
    }
    else if(media >= 7){
        printf("\nMédia= %.2f\n --APROVADO--",media);
        system("color 1");
    }
    else{
        printf("\nMédia= %.2f\n --RECUPERAÇÂO--",media);
        system("color 6");
    }
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


