#include<stdio.h>
#include<locale.h>
#include<conio.h>
#include<stdlib.h>
#include<windows.h>

int main()
{
    float n1, n2;

    printf("\nNúmeros separados por espaço: ");
    scanf("%f %f", &n1, &n2);

    if(n1 > n2){
        printf ("%f é maior que %f", n1,n2);
     }
    else{
        printf ("%.0f é maior que %.0f", n2,n1);
     }

    return(0);
}