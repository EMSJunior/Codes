#!/usr/bin/env python3

# OBI2022
# Tarefa Maior

N = int(input())
M = int(input())
S = int(input())

achou = False
for i in range(M, N - 1, -1):
    soma = 0
    x = i
    while x > 0:
        soma += x % 10
        print("x1:",x, " Soma1: ", soma)
        x //= 10
        print("x2:",x)
    if soma == S:
        achou = True
        resp = i
        break

if achou:
    print(resp)
else:
    print(-1)
