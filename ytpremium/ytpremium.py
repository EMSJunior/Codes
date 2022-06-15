from __future__ import print_function

import os.path
import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from googleapiclient.http import MediaIoBaseDownload, MediaIoBaseDownload
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
import time
import requests
import base64
from datetime import date
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive']


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = {'LuizO':'1iV6EiQI0kUzv0Cf6I0kqMeB10VNGKf41b_zb-LBU2WA',
                        'Erik':'1s0eF_KrXETPIgBP1b67BxY0jYh83zzvK09nayPvkeWA',
                        'LuizF':'1gZYjzXCdy9vzc7CHvZEX8HAd06p47X6a1Dr20bB356c',
                        'Lucas':'1qnuL0bBjp-ru6HhzuEDndpnkhYB6M6uBMpwC7T8Ic6U'}
SAMPLE_RANGE_NAME = 'Página1!B5:D20'

#informações YT
pessoas=["LuizO","Erik","LuizF","Lucas"]
preço = 6.40
nomeconversa="ComprovantesYT"

#Driver info
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://web.whatsapp.com/")

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    service = build('drive', 'v3', credentials=creds)
    sservice = build('sheets', 'v4', credentials=creds)
    sheet = sservice.spreadsheets()

    conversaEntrar()
    coletardados(service,sheet) 
    desconectar()
    time.sleep(2)
    driver.close()


def encontrar(x):
   return(driver.find_element_by_xpath(x))

def encontrarvarios(x):
   return(driver.find_elements_by_xpath(x))

def getpng(uri):
    result = driver.execute_async_script("""
        var uri = arguments[0];
        var callback = arguments[1];
        var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
        var xhr = new XMLHttpRequest();
        xhr.responseType = 'arraybuffer';
        xhr.onload = function(){ callback(toBase64(xhr.response)) };
        xhr.onerror = function(){ callback(xhr.status) };
        xhr.open('GET', uri);
        xhr.send();
        """, uri)
    if type(result) == int :
        raise Exception("Request failed with status %s" % result)
    return base64.b64decode(result)

def conversaEntrar():
    print("Presione Enter quando entrar no whatsapp")
    input()
    print("Coletando dados...")
    try:
        pathconversa= "//span[@title='"+nomeconversa+"']"
        conversa_search = encontrar(pathconversa)
        time.sleep(0.5)
        conversa_search.click()
    except:
        print("\nConversa não encontrada!")

def coletardados(service,sheet):
    j=0
    for i in pessoas:
        try:
            time.sleep(1)
            pathfoto = "//img[contains(@alt,'#"+i+"-/')]"
            fotobusca = encontrarvarios(pathfoto)

            nomearquivo = str(i) + "-Comprovante-"+ str(date.today())+".png"
            url = fotobusca[1].get_attribute("src")
            text = fotobusca[1].get_attribute("alt")
            bytes = getpng(url)
            valor = text[len(i)+3:len(text)]
            try:
                valor = float(valor)
            except:
                print("\nErro ao achar valor: "+valor)
            with open(nomearquivo, 'wb') as file:
                file.write(bytes)
            link=uploadimage(service, nomearquivo,j)
            coletarplanilia(sheet,i,valor,link)
        except:
            print("\nNão foi encontrado: "+ i)
        j+=1

def uploadimage(drive_service, nomearquivo,j):
    file_metadata = {'name': nomearquivo,
                      'parents': ['15xlD4tRXVDXNT4lFdGlQLbGQBmUuSg7V']}
    media = MediaFileUpload(nomearquivo,
                            mimetype='image/png')
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id'
                                        ).execute()
    try:
        return("https://drive.google.com/file/d/"+file.get('id')+"/view?usp=sharing")
    except:
        print("ID não encontrado")
        return("")

def coletarplanilia(sheet,aux,valor,link):
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID[aux],
                                range=SAMPLE_RANGE_NAME).execute()
    lista = result.get('values', [])

    for i in range(1,len(lista)):
        if lista[i][1] != "R$ 6,40":
            lastmonth = i
            if lista[i][1] != "R$ 0,00":
                valor+=float(lista[lastmonth][1][3::].replace(",",".")) #valor = 6.4
            break
    quantidadepago = int(valor//6.4) # 1 mes
    restopago="{0:.2f}".format(valor % 6.4) # 0

    penultimomes = lastmonth+quantidadepago-1 # = 2

    for i in range(lastmonth-1,penultimomes):
        lista[i+1][1]='R$ 6,40'

    lista[penultimomes+1][1]='R$ '+str(restopago).replace(".",",")
    lista[penultimomes+1].append(str(link))

    replace = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID[aux],range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED",body ={'values': lista}).execute()

def desconectar():
    pathbotao= "//div[@title='Mais opções']"
    botao = encontrar(pathbotao)
    botao.click()

    pathdesconectar="//div[@aria-label='Desconectar']"
    desconectar=encontrar(pathdesconectar)
    desconectar.click()

if __name__ == '__main__':
    main()