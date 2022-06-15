# create font object with the font file and specify
# desired size

# import required classes

from PIL import Image, ImageDraw, ImageFont

from extenso import cardinal999, cardinal
from datetime import date, datetime, timedelta

from unicodedata import normalize

from classes import *

today = date.today()

# create Image object with the input image



def mes(z):
    message = ""
    if z == 1:
        message = "janeiro"
    elif z == 2:
        message = "fevereiro"
    elif z == 3:
        message = "março"
    elif z == 4:
        message = "abril"
    elif z == 5:
        message = "maio"
    elif z == 6:
        message = "junho"
    elif z == 7:
        message = "julho"
    elif z == 8:
        message = "agosto"
    elif z == 9:
        message = "setembro"
    elif z == 10:
        message = "outubro"
    elif z == 11:
        message = "novembro"
    elif z == 12:
        message = "dezembro"
    else:
        message = "Error"
    return message


def gerarContrato(clt, agd, dde):
    image = Image.open(
        'C:\\Users\\Usuario\\Documents\\interface\\utilitarios\\contrato.png')


    # initialise the drawing context with
    # the image object as background

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(
        'C:\\Users\\Usuario\\Documents\\interface\\utilitarios\\Sofia-Regular.otf', size=36)
    color = 'rgb(0, 0, 0)'  # black color
    # starting position of the message
    print(clt, agd,dde)
    cliente = Clientes(clt[0],clt[1],clt[2],clt[3],clt[4],clt[5],clt[6],clt[7],clt[8],clt[9],clt[10],clt[11],clt[12][0:2],clt[12][2::],clt[13][0:2],clt[13][2::],clt[14])
    agendamento = Agendamentos(agd[0],agd[1],agd[2],agd[3],agd[4],agd[5],agd[6],agd[7],agd[8],agd[9],agd[10],dde)

    print(cliente,agendamento)

    (x, y) = (333, 745)  # Evento
    message = agendamento.evento
    print('evento',agendamento.evento)

    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ##########################################
    message = cliente.ddn[0:2]  # Data de Nascimento
    draw.text((x+1267, y-10), message, fill=color, font=font)
    draw.text((x+3527, y-10), message, fill=color, font=font)

    message = cliente.ddn[2:4]
    draw.text((x+1367, y-10), message, fill=color, font=font)
    draw.text((x+3627, y-10), message, fill=color, font=font)

    message = cliente.ddn[4::]
    draw.text((x+1467, y-10), message, fill=color, font=font)
    draw.text((x+3727, y-10), message, fill=color, font=font)

    ##########################################
    (x, y) = (390, 822)  # Nome
    message = cliente.nome
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (290, 910)  # CPF
    message = cliente.cpf
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (1345, 910)  # RG
    message = cliente.rg
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (375, 995)  # Endereco
    message = cliente.endereco
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (338, 1075)  # Bairro
    message = cliente.bairro
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (1195, 1075)  # Cidade
    message = cliente.cidade
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (1815, 1075)  # Estado
    message = cliente.estado
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (395, 1162)  # ()
    message = "(   )"
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    (x, y) = (410, 1162)  # DDD 1
    message = cliente.ddd1
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    ################################
    (x, y) = (395+80, 1162)  # Telefone 1
    message = cliente.telefone1
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (395, 1162)  # ()
    message = "(   )"
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    (x, y) = (395+15, 1162)  # DDD 2
    message = cliente.ddd1
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    ################################
    (x, y) = (395+80, 1162)  # Telefone 2
    message = cliente.telefone1
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    if(cliente.ddd2 != ""):
        (x, y) = (395+970, 1162)  # ( )
        message = "(   )"
        draw.text((x, y), message, fill=color, font=font)
        draw.text((x+2260, y), message, fill=color, font=font)
        (x, y) = (395+15+970, 1162)  # DDD 2
        message = cliente.ddd2
        draw.text((x, y), message, fill=color, font=font)
        draw.text((x+2260, y), message, fill=color, font=font)
        ################################
        (x, y) = (395+80+970, 1162)  # Telefone 2
        message = cliente.telefone2
        draw.text((x, y), message, fill=color, font=font)
        draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    d1 = today.strftime("%d/%m/%Y")
    (x, y) = (540, 1253)
    message = d1[0:2]  # Data de Entrega
    draw.text((x, y-10), message, fill=color, font=font)
    draw.text((x+2260, y-10), message, fill=color, font=font)

    message = d1[3:5]
    draw.text((x+80, y-10), message, fill=color, font=font)
    draw.text((x+2350, y-10), message, fill=color, font=font)

    message = d1[6:10]
    draw.text((x+170, y-10), message, fill=color, font=font)
    draw.text((x+2440, y-10), message, fill=color, font=font)

    ################################
    (x, y) = (1515, 1253)
    message = agendamento.ddd[0:2]  # Data de Devolucao
    draw.text((x, y-10), message, fill=color, font=font)
    draw.text((x+2260, y-10), message, fill=color, font=font)

    message = agendamento.ddd[2:4]
    draw.text((x+80, y-10), message, fill=color, font=font)
    draw.text((x+2350, y-10), message, fill=color, font=font)

    message = agendamento.ddd[4::]
    draw.text((x+170, y-10), message, fill=color, font=font)
    draw.text((x+2440, y-10), message, fill=color, font=font)

    d1 = today.strftime("%d        %m       %Y")
    ################################
    (x, y) = (1830, 3015)  # ()
    message = d1  # Data de Emissao
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (1910, 1845)  # Valor Descricao
    if(',' not in agendamento.valor and '.' not in agendamento.valor):
        message = "R$ "+str(int(agendamento.valor))+",00"  # valor
    else:
        message = "R$"+agendamento.valor
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ##########################################
    d1 = today.strftime("%d/%m/%Y")
    message = d1[0:2]  # Data MOC
    (x, y) = (1080, 2590)
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    z = int(d1[3:5])

    message = mes(z)
    draw.text((x+400, y), message, fill=color, font=font)
    draw.text((x+2660, y), message, fill=color, font=font)

    message = d1[8:10]
    draw.text((x+750, y), message, fill=color, font=font)
    draw.text((x+3010, y), message, fill=color, font=font)

    ################################
    (x, y) = (280, 1490)  # Descricao
    fantasia = agendamento.descricao+" + " + \
        (agendamento.acessorios).replace(";", ", ")
    print(fantasia, len(fantasia))
    message = fantasia[0:100]
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    if(len(fantasia) > 100):
        (x, y) = (240, 1555)
        message = fantasia[100:len(fantasia)-1]
        draw.text((x, y), message, fill=color, font=font)
        draw.text((x+2260, y), message, fill=color, font=font)

    font = ImageFont.truetype('utilitarios/century-gothic.ttf', size=36)

    ################################
    (x, y) = (380, 3015)
    message = cliente.nome  # Nome Nota
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (370, 3060)
    message = cliente.cpf  # CPF Nota
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################

    """
    Verificar o tamanho do endereco q cabe na Nota
    
    Somar endereco, numero, bairro,UF
    
    separar entre duas linhas
    
    """
    (x, y) = (1390, 3060)
    endereco = cliente.endereco+", "+cliente.numero+", "+cliente.complemento + \
        ", "+cliente.bairro+"  "+cliente.cidade+"-"+cliente.estado

    message = endereco[0:int(endereco.rfind(' ', 0, 42))]  # Endereco Nota
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    (x, y) = (180, 3110)
    message = endereco[int(endereco.rfind(' ', 0, 42))+1:len(endereco)]
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    ################################
    (x, y) = (760, 2690)

    date = datetime.strptime(
        agendamento.ddd, '%d%m%Y').date()+timedelta(days=7)  # Vencimento Nota
    message = str(date)[8:10]
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
    message = mes(int(str(date)[5:7]))
    draw.text((x+350, y), message, fill=color, font=font)
    draw.text((x+2650, y), message, fill=color, font=font)
    message = str(date)[0:4]
    draw.text((x+750, y), message, fill=color, font=font)
    draw.text((x+3010, y), message, fill=color, font=font)

    ################################
    (x, y) = (1800, 2680)  # Valor nota

    if(',' not in agendamento.valor and '.' not in agendamento.valor):
        message = str(int(agendamento.valor)*3)+",00        " + \
        (20-len(str(int(agendamento.valor)*3)+",00"))*"*"  # valor
    else:
        message = str(int(agendamento.valor[0:agendamento.valor.index(',')])*3)+",00        " + \
        (20-len(str(int(agendamento.valor[0:agendamento.valor.index(',')])*3)+",00"))*"*"  # valor

    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (830, 2870)  # Valor extenso nota
    if(',' not in agendamento.valor and '.' not in agendamento.valor):
        valor = str(cardinal(int(agendamento.valor)*3)).upper() + " REAIS"
    else:

        valor = str(cardinal(int(agendamento.valor[0:agendamento.valor.index(',')])*3)).upper() + " REAIS"
    
    message = valor+"   "+((86-len(valor)-10)*"*")
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    ################################
    (x, y) = (178, 2935)  # Valor extenso nota
    message = 137*"*"
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)
   
    ################################
    (x, y) = (300, 2730)  # DATA NOTA
    message = str(cardinal999(int(str(date)[8:10]))) + " dias do mês de " + mes(
        int(str(date)[5:7])) + " do ano de "+str(cardinal(int(str(date)[0:4])))
    draw.text((x, y), message, fill=color, font=font)
    draw.text((x+2260, y), message, fill=color, font=font)

    def remover_acentos(txt):
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    image.save('contratos/'+str(remover_acentos(cliente.nome))+'.png')
