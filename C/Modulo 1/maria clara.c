#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

int voto();
int header();
int result();

int main(){
    int n,nc1,nc2,nc3;
    nc1=0;
    nc2=0;
    nc3=0;

    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;

    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;

    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;
    header();
    n = voto();
    if(n==1){
        nc1=nc1+1;
        system("cls");
    }
    else if(n==2){
        nc2=nc2+1;
        system("cls");
    }
    else if(n==3){
        nc3=nc3+1;
        system("cls");
    }
    else{printf("Número invalido!");}
    n = 0;

    result(nc1,nc2,nc3);

}

int header(){
    char nome[30];
    printf("Urna do IF:\nNumero do titulo de eleitor: ");
    scanf("%s",nome);
    printf("\nPara votar coloque o nome do candidato e tecle Enter.\n Os candidatos são:\n[1] João do Feijão\n[2] Maria da Igreja\n[3] Tirulipa");
     return(0);
}
int voto(){
    int voto,nc1,nc2,nc3;

    printf("\nVoto:");
    scanf("%d",&voto);
    return(voto);
}

int result(int nc1, int nc2,int nc3){
    printf("Resultado:\nCandidato [1]: %d votos\nCandidato [2]: %dvotos\nCandidato [3]: %dvotos\n",nc1,nc2,nc3);
}