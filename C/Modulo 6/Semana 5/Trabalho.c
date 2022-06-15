#include <stdio.h>
#include <locale.h>
#include <conio.h>
#include <stdlib.h>
#include <windows.h>
#include <math.h>
#include <string.h>

void load();

int main();

void questao1()
{
    float n, i;
    char u;
    int aux;

    system("cls");

    printf("--Calculadora Celsius e Fahrenheit--\n\nDigite a temperatura e em seguido o sua unidade de medida(c/f): ");
    scanf("%f %c", &n, &u);

    switch (u)
    {
    case 'f':
        printf("A temperatura %.2f°f em Celsius é %.2f°c.", n, ((n - 32) * .5556));
        break;
    case 'c':
        printf("A temperatura %.2f°c em Fahrenheit é %.2f°f", n, (n * 1.8) + 32);
        break;
    }
    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        questao1();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao2()
{
    float height, weight;
    char sex;
    int aux;

    printf("--Calculadora de peso ideal--\nDigite a altura(em metros, utilizando \",\") e seu gênero(M-masculino/F-feminino) separados por espaço: ");
    scanf("%f %c", &height, &sex);

    switch (sex)
    {
    case 'm':
    case 'M':
        printf("\nO seu peso ideal é %.0f Kg.", (72.7 * height) - 58);
        break;

    case 'f':
    case 'F':
        printf("\nO seu peso ideal é %.0f Kg.", (62.1 * height) - 44.7);
        break;
    }

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        questao2();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao3()
{
    char nome[32], nome2[32];
    float sabruto, vhora, qhora, aux;

    printf("-Calculadora de almento na folha de pagamento-\n\nInsira o primeiro e último nome do Funcionário: ");
    scanf("%s %s", &nome, &nome2);

    printf("Valor da hora: ");
    scanf("%f", &vhora);

    printf("Quantidade de Horas trabalhadas: ");
    scanf("%f", &qhora);

    sabruto = vhora * qhora;

    if (sabruto <= 900)
    {
        system("cls");
        printf("\n--Salario e impostos de %s %s --\n\n> Salário bruto: %f\n\n> (-) Imposto de Renda(IR):                        [ 0%%] +-ISENTO-+\n> (-) Instituto Nacional do Seguro Social(INSS):   [10%%] %.2f\n> (+) Fundo de Garantia do Tempo de Serviço(FGTS): [11%%] R$ %.2f \n\n> Total de descontos: R$ %.2f\n> Salário Líquido:    R$ %.2f", nome, nome2, sabruto, (sabruto * 0.10), (sabruto * 0.11), (sabruto * 0.10), (sabruto - (sabruto * 0.10)));
    }

    if (sabruto > 900 && sabruto <= 1500)
    {
        system("cls");
        printf("\n--Salario e impostos de %s %s --\n\n> Salário bruto: %f\n\n> (-) Imposto de Renda(IR):                        [ 5%%] R$ %.2f \n> (-) Instituto Nacional do Seguro Social(INSS):   [10%%] R$ %.2f\n> (+) Fundo de Garantia do Tempo de Serviço(FGTS): [11%%] R$ %.2f \n\n> Total de descontos: R$ %.2f\n> Salário Líquido:    R$ %.2f", nome, nome2, sabruto, (sabruto * 0.05), (sabruto * 0.10), (sabruto * 0.11), (sabruto * 0.05) + (sabruto * 0.10), (sabruto - (sabruto * 0.05) - (sabruto * 0.10)));
    }

    if (sabruto > 1500 && sabruto <= 2500)
    {
        system("cls");
        printf("\n--Salario e impostos de %s %s --\n\n> Salário bruto: %f\n\n> (-) Imposto de Renda(IR):                        [10%%] R$ %.2f \n> (-) Instituto Nacional do Seguro Social(INSS):   [10%%] R$ %.2f\n> (+) Fundo de Garantia do Tempo de Serviço(FGTS): [11%%] R$ %.2f \n\n> Total de descontos: R$ %.2f\n> Salário Líquido:    R$ %.2f", nome, nome2, sabruto, (sabruto * 0.10), (sabruto * 0.10), (sabruto * 0.11), (sabruto * 0.10) + (sabruto * 0.10), (sabruto - (sabruto * 0.10) - (sabruto * 0.10)));
    }

    if (sabruto > 2500)
    {
        system("cls");
        printf("\n--Salario e impostos de %s %s --\n\n> Salário bruto: %f\n\n> (-) Imposto de Renda(IR):                        [10%%] R$ %.2f \n> (-) Instituto Nacional do Seguro Social(INSS):   [20%%] R$ %.2f\n> (+) Fundo de Garantia do Tempo de Serviço(FGTS): [11%%] R$ %.2f \n\n> Total de descontos: R$ %.2f\n> Salário Líquido:    R$ %.2f", nome, nome2, sabruto, (sabruto * 0.10), (sabruto * 0.20), (sabruto * 0.11), (sabruto * 0.20) + (sabruto * 0.10), (sabruto - (sabruto * 0.20) - (sabruto * 0.10)));
    }

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%f", &aux);
    if (aux == 1)
    {
        system("cls");
        questao3();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao4()
{
    int num, aux;

    printf("--Calculadora de ímpar ou par--\n\nColoque o número desejado: ");
    scanf("%d", &num);

    if (num % 2 == 0)
        printf("\n%d é um número PAR !", num);

    else
        printf("\n%d é um número ÍMPAR !", num);

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao4();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao5()
{
    int aux, x, j, k = 0;
    char user[32], pass[32], i;

    system("cls");
    printf("--Calculadora de credibilidade da senha--\n\nUsuario: ");
    scanf("%s", &user);

    printf("Senha: ");
    scanf("%s", &pass);

    j = strcmp(user, pass);

    if (j == 0)
    {
        system("color 4");
        printf("Senha igual ao usuario, por favor tente novamente !");
        Sleep(4000);
        system("color 7");
        questao5();
    }
    else
    {
        printf("\n\nUsuario: %s\nSenha: %s\nConfirma(s/n)? ", user, pass);
        scanf("%s", &i);

        if (i == 'n')
        {
            for (i = 0; i < 11; i++)
            {
                Sleep(10);
                system("cls");
                printf("Tentando novamente...");
                printf("(%d%%)", i * 10);
            }
            Sleep(500);
            questao5();
        }
        else
        {
            printf("Usuario registrado!\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
            scanf("%d", &aux);
            if (aux == 1)
            {
                system("cls");
                questao5();
            }
            else if (aux == 2)
            {
                load();
                main();
            }
        }
    }
}

void questao6()
{
    int num, aux;

    printf("--Calculadora de tabuada--\n\nDigite o número no qual deseja as suas multiplicações: ");
    scanf("%d", &num);

    system("cls");
    printf("-- TABUADA DO %d --\n\n>%d x 1 : %d\n>%d x 2 : %d\n>%d x 3 : %d\n>%d x 4 : %d\n>%d x 5 : %d\n>%d x 6 : %d\n>%d x 7 : %d\n>%d x 8 : %d\n>%d x 9 : %d\n>%d x 10: %d", num, num, num * 1, num, num * 2, num, num * 3, num, num * 4, num, num * 5, num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10);

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao6();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao7()
{
    int num, aux, i = 0, j = 1, r, x;

    printf("--Calculadora de sequencia de Fibonacci--\n\nDigite o n-ésimo termo: ");
    scanf("%d", &num);

    printf("0");
    for (x = 0; x <= num; x++)
    {
        r = i + j;
        printf(",%d", r);
        j = i;
        i = r;
    }
    printf(".");

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao7();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao8()
{
    int aux, i, j = 1, c;

    printf("--Calculadora de número fatorial--\n\n Digite o número: ");
    scanf("%d", &c);

    printf("> Fatorial de %d:\n> %d! = ", c, c);

    for (i = c; i >= 2; i--)
    {
        j = j * i;
        printf("%d .", i);
    }
    printf("1 = %d", j);

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao8();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao9()
{
    int n, aux, i, j, aux2, aux3;
    aux2 = 0;

    printf("--Calculadora de números primos--\n\nDigite n-ésimo termo primo: ");
    scanf("%d", &n);

    printf("\nNúmeros primos: 2");

    for (i = 2; i < n; i++)
    {
        aux3 = 0;
        for (j = 3; j <= i; ++j)
        {
            //printf("\n %d,%d",i,j);
            if (i % j == 0)
            {
                aux3++;
            }
            if (aux > 1)
            {
                break;
            }
        }
        if (aux3 == 1)
        {
            printf(", %d", j - 1);
            aux2++;
        }
    }
    printf("\nExistem %d numeros primos entre %d  e  %d", aux2, 1, n);

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao9();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void questao10()
{
    int n, i, h = 1,aux;

    printf("--Calculadora de serie /2! --\n\n Digite o n-ésimo termo: ");
    scanf("%d", &n);
    printf("H = 1");
    for (i = 1; i <= n; i++)
    {
        printf(" + 1/%d", i);
        h += 1 / i;
    }
    printf("\n H = %d", h);

    printf("\n\n1-Colocar outro número.\n2-Voltar ao menu principal\n");
    scanf("%d", &aux);
    if (aux == 1)
    {
        system("cls");
        questao10();
    }
    else if (aux == 2)
    {
        load();
        main();
    }
}

void load()
{
    int i;

    for (i = 0; i < 11; i++)
    {
        Sleep(10);
        system("cls");
        printf("Carregando ");
        printf("(%d%%)", i * 10);
    }
    Sleep(500);
    system("cls");
}

void exite()
{
    int i;
    char aux;

    system("cls");
    system("color 4");
    printf("Tem certeza que deseja sair(s/n)? ");
    scanf("%s", &aux);
    printf("%c", aux);

    if (aux == 's')
    {
        system("color 1");
        for (i = 0; i < 11; i++)
        {
            Sleep(10);
            system("cls");
            printf("Obrigado por utilizar!\nSaindo ");
            printf("(%d%%)", i * 10);
        }
    }
    else
    {
        system("color 7");
        main();
    }
}

int main()
{
    setlocale(LC_ALL, "Portuguese");
    int i;
    char a;

    system("cls");

    printf("********** Introdução a programação ********\n*** Aluno: Edson Mendes de Souza Júnior  ***\n*** Turma: 1º ano Informática            ***\n********************************************\n\n1  - Questão 9\n2  - Questão 13\n3  - Questão 30 \n4  - Questão 40\n5  - Questão 48\n6  - Questão 58\n7  - Questão 61\n8  - Questão 78\n9  - Questão 81\n10 - Questão 91\n0 - Sair do Progama\n\nSelecione a questão que deseja executar: ");
    scanf("%i", &i);

    switch (i)
    {
    case 0:
        exite();
        break;
    case 1:
        load();
        questao1();
        break;
    case 2:
        load();
        questao2();
        break;
    case 3:
        load();
        questao3();
        break;
    case 4:
        load();
        questao4();
        break;
    case 5:
        load();
        questao5();
        break;
    case 6:
        load();
        questao6();
        break;
    case 7:
        load();
        questao7();
        break;
    case 8:
        load();
        questao8();
        break;
    case 9:
        load();
        questao9();
        break;
    case 10:
        load();
        questao10();
        break;
    default:
        system("color 4");
        printf("Você inseriu um digito inválido !\nPor favor tente novamente!");
        Sleep(4000);
        system("color 7");
        main();
        break;
    }
    return (0);
}
