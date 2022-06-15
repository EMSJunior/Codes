#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

void main()
{
  int j;
  char gabarito[10];
  char aux;

  printf("Ola, por favor insira o gabarito: \n");
  for (int j = 0; j < 10; j++)
      {
          printf("Questao %d : ", j+1);
          scanf("%c",&aux);
          switch(aux)
          {
            case 'a': case 'A':
              gabarito[j] = 'A';
              break;
            case 'b': case 'B':
              gabarito[j] = 'B';
              break;
            case 'c': case 'C':
              gabarito[j] = 'C';
              break;
            case 'd': case 'D':
              gabarito[j] = 'D';
              break;
            case 'E': case 'e':
              gabarito[j] = 'E';
              break;
            
          }
      }
  for (j = 0; j< 10;j++)
  {
    printf("%d-%c",j,gabarito[j]);
  }
}