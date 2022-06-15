
lista = [
['Mês',        'Valor',     'Comprovante'],
['01/01/2022', 'R$ 6,40','https://drive.google.com/file/d/1mvNMyGST5t5GS60HciKvFOD4rIRh5mUN/view?usp=sharing'],
['01/02/2022', 'R$ 6,00'],
['01/03/2022', 'R$ 0,00'],
['01/04/2022', 'R$ 0,00'],
['01/05/2022', 'R$ 0,00'],
['01/06/2022', 'R$ 0,00'],
['01/07/2022', 'R$ 0,00'],
['01/08/2022', 'R$ 0,00'],
['01/09/2022', 'R$ 0,00'],
['01/10/2022', 'R$ 0,00'],
['01/11/2022', 'R$ 0,00'],
['01/12/2022', 'R$ 0,00']]

#lista[mes][0=data 1=valorpago 2=comprovantelink]

valor = 15

for i in range(1,len(lista)):
  if lista[i][1] != "R$ 6,40":
    lastmonth = i
    print(lastmonth)
    if lista[i][1] != "R$ 0,00":
      valor+=float(lista[lastmonth][1][3::].replace(",",".")) #valor = 6.4
    print(valor)
    break

quantidadepago = int(valor//6.4) # 1 mes
restopago="{0:.2f}".format(valor % 6.4) # 0

print(quantidadepago,restopago)

penultimomes = lastmonth+quantidadepago-1 # = 2

for i in range(lastmonth-1,penultimomes):
  print(i)
  lista[i+1][1]='R$ 6,40'

lista[penultimomes+1][1]='R$ '+str(restopago).replace(".",",")

print(lista)