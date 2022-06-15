# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:59:14 2020

@author: Luiz
"""


# Classe Clientes e Classe Agendamentos

"""
-
Criar lista de objetos
lista[]
a cada iteracao de linha,
enquanto dados != vazio
cria obj e append na lista


-
Organizar pp do contrato com cada dado
Limitar len(string) descricao
colocar acessorios junto


"""


class Clientes:
    def __init__(self, ID="", nome="", ddn="", cpf="", rg="", cep="", endereco="", numero="", complemento="", bairro="", cidade="", estado="", ddd1="", telefone1="", ddd2="", telefone2="", saldo=""):

        self.nome = nome
        self.ddn = ddn
        self.cpf = cpf
        self.rg = rg
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.ddd1 = ddd1
        self.telefone1 = telefone1
        self.ddd2 = ddd2
        self.telefone2 = telefone2
        self.saldo = saldo
        self.ID = ID


class Agendamentos:
    def __init__(self, ID="", cpf="", evento="", descricao="", acessorios="", ajustes="", valor="",cupom = "", desconto="", sinal="", dde="", ddd=""):

        self.ID = ID
        self.cpf = cpf
        self.evento = evento
        self.descricao = descricao
        self.acessorios = acessorios
        self.ajustes = ajustes
        self.valor = valor
        self.cupom = cupom
        self.desconto = desconto
        self.sinal = sinal
        self.dde = dde
        self.ddd = ddd
