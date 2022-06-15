# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 21:05:47 2020

@author: Luiz
"""


import pycep_correios


def getEnderecobyCEP(cep):
    endereco = pycep_correios.get_address_from_cep(str(cep))
    return [endereco['logradouro'],endereco['bairro'],endereco['cidade'],endereco['uf']]
