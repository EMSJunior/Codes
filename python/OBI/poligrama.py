N = int(input())
Ip = input()

P = sorted(list(set(Ip)))
quant = []

for i in P:
    quant.append(Ip.count(i))
repet = sum((int(i/sorted(quant)[0])) for i in (quant))

resp = (Ip[0: repet])

if (len(quant) / N == 1):
    resp = "*"

print(resp)