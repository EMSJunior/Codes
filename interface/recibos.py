
from PIL import Image, ImageDraw, ImageFont

from extenso import cardinal999, cardinal
from datetime import date,datetime,timedelta

from unicodedata import normalize

from classes import *

today = date.today()

# create Image object with the input image
 
image = Image.open('utilitarios/recibo.png')
 


# initialise the drawing context with
# the image object as background
 
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('utilitarios/Sofia-Regular.otf', size=48)
color = 'rgb(0, 0, 0)' # black color
# starting position of the message

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
        message ="Error"
    return message


def gerarRecibo(clt,agd):
    
    cliente = Clientes(clt[0],clt[1],clt[2],clt[3],clt[4],clt[5],clt[6],clt[7],clt[8],clt[9],clt[10],clt[11],clt[12][0:2],clt[12][2::],clt[13][0:2],clt[13][2::],clt[14])
    agd = agd[0]
    agendamento = Agendamentos(agd[0],agd[1],agd[2],agd[3],agd[4],agd[5],agd[6],agd[7],agd[8],agd[9],agd[10],'000000')

    global font
    
    (x, y) = (721, 978) # Recebi de: NOME
    message = cliente.nome
    draw.text((x, y), message, fill=color, font=font)
    
    ##########################################
    message = 'R$  ' + agendamento.sinal  #A QUANTIA DE:
    draw.text((x+200, y+130), message, fill=color, font=font)
    
    message = agendamento.descricao + '  +  ' + agendamento.acessorios
    draw.text((x+150, y+240), message, fill=color, font=font)
    
    d1 = today.strftime("%d/%m/%Y")
    message = d1[0:2]  # Data MOC
    draw.text((963, 1687), message, fill=color, font=font)

    z = int(d1[3:5])

    message = mes(z)
    draw.text((1367, 1687), message, fill=color, font=font)


    message = d1[8:10]
    draw.text((1965, 1687), message, fill=color, font=font)

    font = ImageFont.truetype('utilitarios/century-gothic.ttf', size=36)



    def remover_acentos(txt):
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    image.save('recibos/'+str(remover_acentos(cliente.nome))+'.png')