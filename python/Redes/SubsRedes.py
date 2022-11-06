def classeA(n):
  nredes = 2**n
  salto = 2**(8-n)
  j=0
  for i in range(0,nredes):
      listaredes.append([ips[0],j,0,0])
      listabroad.append([ips[1],j+salto-1,255,255])
      j+=salto
  
def classeB(n):
    nredes = 2**n
    salto = 2**(8-n)
    j=0
    for i in range(0,nredes):
        listaredes.append([ips[0],ips[1],j,0])
        listabroad.append([ips[0],ips[1],j+salto-1,255])
        j+=salto

def classeC(n):
  nredes = 2**n
  salto = 2**(8-n)
  j=0
  for i in range(0,nredes):
    listaredes.append([ips[0],ips[1],ips[2],j])
    listabroad.append([ips[0],ips[1],ips[2],j+salto-1])
    j+=salto
      

ip, subr = "191.41.35.112/18".split("/")
subr=int(subr)
ips = [int(i) for i in ip.split(".")]

listaredes=[]
listabroad=[]

if ips[0] < 128:
    classeA(subr-8)
    
elif ips[0] < 192:
    classeB(subr-16)

else: 
    classeC(subr-24)

print("Ip:", ip, "/", subr)
for i in range(len(listaredes)):
  print("   Rede " , i+1 , ": " , listaredes[i][0],".",listaredes[i][1],".",listaredes[i][2],".",listaredes[i][3], "  Broad cast: " , listabroad[i][0],".",listabroad[i][1],".",listabroad[i][2],".",listabroad[i][3])