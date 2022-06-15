from typing import Text
from urllib.request import Request, urlopen
import time
import pyperclip as pc

inicio = time.time()


def takenp(cscode):
  hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

  codtraduzido=cscode.replace(":","%3A")

  finderurl = "https://www.steamidfinder.com/lookup/"+codtraduzido

  reqf = Request(finderurl, headers=hdr)

  try:
      page = urlopen(reqf)
  except:
      print('Finder Block')

  htmlfinder = page.read()
  htmlfinder = htmlfinder.decode('utf-8')

  s64 = "steamID64 (Dec): "
  len64 = len(s64)

  pos64=(htmlfinder.index(s64))
  posf64 = pos64+len64+6

  publiccode=(htmlfinder[posf64:pos64+40])

  statussite = 'https://csgostats.gg/player/'+publiccode

  req = Request(statussite, headers=hdr)

  try:
      page = urlopen(req)
  except:
      print('Status Block')


  htmlstatus = page.read()
  htmlstatus = htmlstatus.decode('utf-8')

  #?Pegar Nick
  player = "player-name"
  lenplayer = len(player)

  posplayer = (htmlstatus.index(player))+13

  j=0
  for i in htmlstatus[posplayer+1:posplayer+80]:
    j +=1
    if i == "<":
      posfplayer = posplayer + j
      break

  nick=(htmlstatus[posplayer:posfplayer]) + ">"

  #?Pegar rank l
  try:
    rank="https://static.csgostats.gg/images/ranks/"
    lenrank= len(rank)

    posp=(htmlstatus.index(rank))
    posf =posp+lenrank

    ptt=(htmlstatus[posf:posf+2])

    patents = {
    1:'Prata I',
    2:'Prata II',
    3:'Prata III',
    4:'Prata IV',
    5:'Prata V',
    6:'Prata VI',
    7: 'Ouro I',
    8: 'Ouro II',
    9: 'Ouro III',
    10:'Ouro IV',
    11:'AK I',
    12:'AK II',
    13:'AK X',
    14:'Xeriff',
    15:'Aguia I',
    16:'Aguia II',
    17:'Supremo',
    18:'Globo Rural'
    }
    patente = patents[int(ptt)]
  except:
    patente = ""

  #?Pegar rank H
  try:
    rank2a="Best:"
    lenrank2a= len(rank2a)

    posba=(htmlstatus.index(rank2a))
    posbfa =posba+lenrank2a

    ptt2 = htmlstatus[posbfa:posbfa+100]

    posp2=(ptt2.index(rank))
    posf2 =posp2+lenrank

    patente2=(ptt2[posf2:posf2+2])

    patente2 = ": Best: " + patents[int(patente2)] + "."

  except:
    patente2 = ""

  #?Pegar Comp Wins
  try:
    CompW = "Comp. Wins"
    lenCompW = len(CompW)

    posCompW1 = (htmlstatus.index(CompW))

    ComWText = htmlstatus[posCompW1:posCompW1+300]

    seach ="font-weight:bold"
    posiCompW2 = ((ComWText.index(seach))+len(seach))+3

    j=0
    for i in ComWText[posiCompW2:posiCompW2+20]:
      j +=1
      if i == "<":
        posfCompW = posiCompW2 + j
        break

    CompWins = ComWText[posiCompW2:posfCompW-1]+" wins: "
    Nvitorias = int(ComWText[posiCompW2:posfCompW-1])
  except:
    CompWins = ""
    Nvitorias=0

  #?Pegar stats
  try:
    Statstx = "og:description"
    lenStats = len(Statstx)

    posStats = (htmlstatus.index(Statstx))

    StatsText = htmlstatus[posStats:posStats+300]

    seachS ="Win"
    posiStats = (StatsText.index(seachS))

    j=0
    for i in StatsText[posiStats:posiStats+50]:
      j +=1
      if i == "\\":
        posfStats = posiStats + j
        break

    Stats = StatsText[posiStats:posfStats-1] + ":"
  except:
    Stats = ": Sem informacoes :-:"

  
  return(nick+Stats+CompWins+patente+patente2)

#End
def pegarCodigo(txt):
  possteamcode=txt.index("STEAM")
  j=0
  for i in txt[possteamcode+1:possteamcode+80]:
    j +=1
    if i == " ":
      possteamcodefinal = possteamcode + j
      break
  cscode=(txt[possteamcode:possteamcodefinal])
  return(takenp(cscode))


import keyboard
import winsound

winsound.Beep(2500,300)
opentxt = pc.paste()
jogador = []

for i in opentxt.split('\n'):
  try:
    jogador.append(pegarCodigo(i))
    print("200")
  except:
    print("404")


text="clear\n"
for i in jogador:
  text+=("ECHO "+i+"\n")
text += "\n"
j=0
for i in jogador:
  j+=1
  text+=("alias \"statussay"+str(j)+"\" \"say "+i+";bind q statussay"+str(j+1)+"\"\n")
text += "\nbind q statussay1"


text = text.encode('utf-8').decode('ascii', 'ignore')
with open('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\mc-matchstatus-by-ehpsker.cfg', 'w') as conf:
  txt = conf.write(text)

winsound.Beep(1000,500)